"""Notion API クライアント（MCPフォールバック用）。

Notion MCP Server が利用できない場合のフォールバックとして、
httpx を使用して直接 Notion API にリクエストを送信する。

Usage:
    python src/notion_client.py --session-id <session_id>
    python src/notion_client.py --test
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import httpx
from dotenv import load_dotenv

load_dotenv()

from src.config import (
    NOTION_API_KEY,
    NOTION_API_URL,
    NOTION_DATABASE_ID,
    NOTION_VERSION,
    OUTPUTS_DIR,
)

logger = logging.getLogger(__name__)

_MAX_RETRIES = 3
_RETRY_BASE_DELAY = 2.0  # seconds


async def post_to_notion(
    title: str,
    tags: list[str],
    summary: str,
    body_blocks: list[dict[str, Any]],
    *,
    source: str = "claude-code",
    status: str = "draft",
    report_date: str | None = None,
) -> dict[str, Any]:
    """Notionデータベースにレポートを投稿する。

    Args:
        title: レポートタイトル。
        tags: タグのリスト（例: ["ai-strategy", "python"]）。
        summary: 1-2文の要約。
        body_blocks: Notion Block形式の本文リスト。
        source: 出力元（デフォルト: claude-code）。
        status: ステータス（デフォルト: draft）。
        report_date: 日付（ISO 8601形式、デフォルト: 本日）。

    Returns:
        Notion API のレスポンス辞書。

    Raises:
        httpx.HTTPStatusError: API呼び出しが失敗した場合。
        ValueError: NOTION_API_KEY or NOTION_DATABASE_ID が未設定の場合。
    """
    if not NOTION_API_KEY:
        raise ValueError("NOTION_API_KEY is not set in .env")
    if not NOTION_DATABASE_ID:
        raise ValueError("NOTION_DATABASE_ID is not set in .env")

    headers = _build_headers()
    if report_date is None:
        report_date = str(date.today())

    data: dict[str, Any] = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "名前": {"title": [{"text": {"content": title}}]},
            "Tags": {"multi_select": [{"name": t} for t in tags]},
            "Source": {"select": {"name": source}},
            "Date": {"date": {"start": report_date}},
            "Status": {"select": {"name": status}},
            "Summary": {"rich_text": [{"text": {"content": summary}}]},
        },
        "children": body_blocks[:100],  # Notion API: max 100 blocks per request
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        result = await _request_with_retry(
            client, "POST", f"{NOTION_API_URL}/pages", json_body=data, headers=headers
        )

        # 100ブロックを超える場合は追加リクエスト
        page_id = result["id"]
        for i in range(100, len(body_blocks), 100):
            chunk = body_blocks[i : i + 100]
            await _request_with_retry(
                client,
                "PATCH",
                f"{NOTION_API_URL}/blocks/{page_id}/children",
                json_body={"children": chunk},
                headers=headers,
            )

    logger.info("Notion page created: %s", result.get("url", ""))
    return result


def markdown_to_notion_blocks(markdown_text: str) -> list[dict[str, Any]]:
    """MarkdownテキストをNotion Block形式に変換する。

    Args:
        markdown_text: Markdown形式のテキスト。

    Returns:
        Notion Block辞書のリスト。
    """
    blocks: list[dict[str, Any]] = []
    lines = markdown_text.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]

        # 空行はスキップ
        if not line.strip():
            i += 1
            continue

        # H2見出し
        if line.startswith("## "):
            blocks.append(_heading_block(2, line[3:].strip()))
            i += 1
            continue

        # H3見出し
        if line.startswith("### "):
            blocks.append(_heading_block(3, line[4:].strip()))
            i += 1
            continue

        # H1見出し（H2として扱う、Notionにはheading_1もあるが統一性のため）
        if line.startswith("# "):
            blocks.append(_heading_block(2, line[2:].strip()))
            i += 1
            continue

        # コードブロック
        if line.strip().startswith("```"):
            lang = line.strip()[3:].strip()
            code_lines: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # closing ```
            blocks.append(_code_block("\n".join(code_lines), lang or "plain text"))
            continue

        # テーブル行（| で始まる）
        if line.strip().startswith("|"):
            table_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                # セパレータ行（|---|---|）はスキップ
                if not re.match(r"^\|[\s\-:|]+\|$", lines[i].strip()):
                    table_lines.append(lines[i])
                i += 1
            # テーブルをパラグラフとして出力（Notion table APIは複雑なため簡略化）
            for tl in table_lines:
                blocks.append(_paragraph_block(tl.strip()))
            continue

        # 箇条書き
        if line.strip().startswith("- ") or line.strip().startswith("* "):
            text = re.sub(r"^[\s]*[-*]\s+", "", line)
            blocks.append(_bulleted_list_block(text.strip()))
            i += 1
            continue

        # 番号付きリスト
        if re.match(r"^\s*\d+\.\s+", line):
            text = re.sub(r"^\s*\d+\.\s+", "", line)
            blocks.append(_numbered_list_block(text.strip()))
            i += 1
            continue

        # 通常のパラグラフ（連続する非空行をまとめる）
        para_lines: list[str] = []
        while i < len(lines) and lines[i].strip() and not _is_special_line(lines[i]):
            para_lines.append(lines[i])
            i += 1
        if para_lines:
            # Notion APIのrich_text contentは2000文字制限
            content = " ".join(para_lines)
            for chunk in _chunk_text(content, 2000):
                blocks.append(_paragraph_block(chunk))

    return blocks


async def post_session_report(session_id: str) -> dict[str, Any]:
    """セッションのレポートをNotionに投稿する。

    Args:
        session_id: セッションID。

    Returns:
        Notion API のレスポンス辞書。

    Raises:
        FileNotFoundError: レポートファイルが見つからない場合。
    """
    session_dir = OUTPUTS_DIR / session_id
    report_path = session_dir / "05_report.md"
    meta_path = session_dir / "session_meta.json"

    if not report_path.exists():
        raise FileNotFoundError(f"Report not found: {report_path}")

    # メタ情報を読み込み
    theme = session_id
    if meta_path.exists():
        with open(meta_path, encoding="utf-8") as f:
            meta = json.load(f)
            theme = meta.get("theme", session_id)

    # レポートを読み込み
    report_text = report_path.read_text(encoding="utf-8")

    # Executive Summaryを抽出（レポートの最初のセクション）
    summary = _extract_summary(report_text)

    # タイトル生成
    today_str = date.today().strftime("%Y/%m/%d")
    title = f"{today_str} {theme}"

    # Markdown→Notionブロック変換
    body_blocks = markdown_to_notion_blocks(report_text)

    # 投稿
    result = await post_to_notion(
        title=title,
        tags=["research-summary", "knowledge-base"],
        summary=summary,
        body_blocks=body_blocks,
    )

    # Notion URLを保存
    notion_url = result.get("url", "")
    url_path = session_dir / "06_notion_url.txt"
    url_path.write_text(notion_url, encoding="utf-8")

    return result


# ─── Private helpers ──────────────────────────────────────────────


def _build_headers() -> dict[str, str]:
    """Notion API用HTTPヘッダーを構築する。"""
    return {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }


async def _request_with_retry(
    client: httpx.AsyncClient,
    method: str,
    url: str,
    *,
    json_body: dict[str, Any],
    headers: dict[str, str],
) -> dict[str, Any]:
    """指数バックオフ付きHTTPリクエスト。

    Args:
        client: httpx.AsyncClient。
        method: HTTPメソッド。
        url: リクエストURL。
        json_body: リクエストボディ。
        headers: HTTPヘッダー。

    Returns:
        レスポンスJSON辞書。

    Raises:
        httpx.HTTPStatusError: 最大リトライ後も失敗した場合。
    """
    for attempt in range(_MAX_RETRIES):
        response = await client.request(method, url, json=json_body, headers=headers)
        if response.status_code == 429:
            delay = _RETRY_BASE_DELAY * (2 ** attempt)
            logger.warning("Rate limited, retrying in %.1fs...", delay)
            await asyncio.sleep(delay)
            continue
        response.raise_for_status()
        return response.json()

    # 最終リトライ
    response = await client.request(method, url, json=json_body, headers=headers)
    response.raise_for_status()
    return response.json()


def _heading_block(level: int, text: str) -> dict[str, Any]:
    """見出しブロックを生成する。"""
    key = f"heading_{level}"
    return {
        "object": "block",
        "type": key,
        key: {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]},
    }


def _paragraph_block(text: str) -> dict[str, Any]:
    """パラグラフブロックを生成する。"""
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{"type": "text", "text": {"content": text[:2000]}}]
        },
    }


def _bulleted_list_block(text: str) -> dict[str, Any]:
    """箇条書きブロックを生成する。"""
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [{"type": "text", "text": {"content": text[:2000]}}]
        },
    }


def _numbered_list_block(text: str) -> dict[str, Any]:
    """番号付きリストブロックを生成する。"""
    return {
        "object": "block",
        "type": "numbered_list_item",
        "numbered_list_item": {
            "rich_text": [{"type": "text", "text": {"content": text[:2000]}}]
        },
    }


def _code_block(code: str, language: str = "plain text") -> dict[str, Any]:
    """コードブロックを生成する。"""
    return {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"type": "text", "text": {"content": code[:2000]}}],
            "language": language,
        },
    }


def _is_special_line(line: str) -> bool:
    """特殊行（見出し・リスト・コードブロック等）かどうかを判定する。"""
    stripped = line.strip()
    return (
        stripped.startswith("#")
        or stripped.startswith("- ")
        or stripped.startswith("* ")
        or stripped.startswith("```")
        or stripped.startswith("|")
        or bool(re.match(r"^\d+\.\s+", stripped))
    )


def _chunk_text(text: str, max_length: int) -> list[str]:
    """テキストを指定長で分割する。"""
    if len(text) <= max_length:
        return [text]
    chunks: list[str] = []
    while text:
        chunks.append(text[:max_length])
        text = text[max_length:]
    return chunks


def _extract_summary(report_text: str) -> str:
    """レポートからExecutive Summaryを抽出する。

    Args:
        report_text: レポート全文。

    Returns:
        Executive Summary テキスト（最大300文字）。
    """
    # "Executive Summary" セクションを探す
    match = re.search(
        r"(?:##?\s*(?:1\.\s*)?Executive Summary[^\n]*)\n(.*?)(?=\n##?\s|\Z)",
        report_text,
        re.DOTALL | re.IGNORECASE,
    )
    if match:
        summary = match.group(1).strip()
        # Markdown記法を除去
        summary = re.sub(r"[*_`#]", "", summary)
        summary = re.sub(r"\n+", " ", summary)
        return summary[:300]

    # フォールバック: 最初の段落を使用
    lines = [l.strip() for l in report_text.split("\n") if l.strip() and not l.startswith("#")]
    if lines:
        return " ".join(lines[:3])[:300]
    return "（要約なし）"


# ─── CLI ──────────────────────────────────────────────────────────


def main() -> None:
    """CLIエントリポイント。"""
    parser = argparse.ArgumentParser(description="Notion レポート投稿ツール")
    parser.add_argument("--session-id", help="投稿するセッションID")
    parser.add_argument("--test", action="store_true", help="テスト投稿を実行")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    if args.test:
        asyncio.run(_run_test())
    elif args.session_id:
        result = asyncio.run(post_session_report(args.session_id))
        print(f"✅ 投稿成功: {result.get('url', '')}")
    else:
        parser.print_help()
        sys.exit(1)


async def _run_test() -> None:
    """テスト投稿を実行する。"""
    today_str = date.today().strftime("%Y/%m/%d")
    test_blocks = [
        _heading_block(2, "テスト目的"),
        _paragraph_block(
            "Claude CodeからNotion APIを経由したレポート自動出力が正常に動作するか確認する。"
        ),
        _heading_block(2, "確認項目"),
        _bulleted_list_block("タイトルが正しく設定されること"),
        _bulleted_list_block("Tags（multi_select）が複数付与されること"),
        _bulleted_list_block("Source, Date, Status, Summaryが正しく設定されること"),
        _bulleted_list_block("本文がNotion blocksとして構造化されること"),
        _heading_block(2, "結果"),
        _paragraph_block("このページが正しく表示されていれば成功。"),
    ]
    result = await post_to_notion(
        title=f"{today_str} フォールバックテスト",
        tags=["automation", "python", "how-to"],
        summary="Pythonスクリプトによるフォールバック投稿のテスト",
        body_blocks=test_blocks,
    )
    print(f"✅ テスト投稿成功: {result.get('url', '')}")


if __name__ == "__main__":
    main()
