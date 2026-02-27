"""arXiv API クライアント。

arXiv の Atom フィード API を使用して学術論文を検索する。
リクエスト間隔3秒以上のレート制限を遵守する。
"""

from __future__ import annotations

import asyncio
import logging
import re
import sys
from typing import Any

import httpx
import xmltodict

from src.config import ARXIV_API_URL, ARXIV_REQUEST_INTERVAL

logger = logging.getLogger(__name__)

# arXiv カテゴリマッピング
CATEGORY_MAP: dict[str, str] = {
    "cs.AI": "Artificial Intelligence",
    "cs.CL": "Computation and Language",
    "cs.LG": "Machine Learning",
    "cs.CV": "Computer Vision",
    "stat.ML": "Machine Learning (Statistics)",
    "q-bio": "Quantitative Biology",
}

_last_request_time: float = 0.0


async def search_papers(
    query: str,
    *,
    year_range: str | None = None,
    max_results: int = 100,
    categories: list[str] | None = None,
    client: httpx.AsyncClient | None = None,
) -> list[dict[str, Any]]:
    """arXiv で論文を検索する。

    Args:
        query: 検索クエリ文字列。
        year_range: 出版年の範囲（例: "2020-2025"）。フィルタリングに使用。
        max_results: 取得する最大論文数。
        categories: arXiv カテゴリフィルタ（例: ["cs.AI", "cs.CL"]）。
        client: 既存の httpx.AsyncClient（指定しなければ内部で生成）。

    Returns:
        統一フォーマットに正規化された論文辞書のリスト。
    """
    global _last_request_time

    search_query = _build_query(query, categories)

    own_client = client is None
    if own_client:
        client = httpx.AsyncClient(timeout=30.0)

    papers: list[dict[str, Any]] = []
    start = 0
    batch_size = min(max_results, 100)

    try:
        while start < max_results:
            current_batch = min(batch_size, max_results - start)
            params = {
                "search_query": search_query,
                "start": start,
                "max_results": current_batch,
                "sortBy": "relevance",
                "sortOrder": "descending",
            }

            # レート制限遵守: 3秒以上の間隔
            now = asyncio.get_event_loop().time()
            elapsed = now - _last_request_time
            if elapsed < ARXIV_REQUEST_INTERVAL and _last_request_time > 0:
                await asyncio.sleep(ARXIV_REQUEST_INTERVAL - elapsed)

            try:
                resp = await client.get(ARXIV_API_URL, params=params)
                _last_request_time = asyncio.get_event_loop().time()
                resp.raise_for_status()
            except httpx.HTTPError as e:
                logger.error("arXiv request error: %s", e)
                break

            parsed = xmltodict.parse(resp.text)
            feed = parsed.get("feed", {})
            entries = feed.get("entry", [])

            # 単一結果の場合、xmltodict は dict を返す
            if isinstance(entries, dict):
                entries = [entries]

            if not entries:
                break

            # 年範囲フィルタ
            year_start, year_end = _parse_year_range(year_range)

            for entry in entries:
                paper = _normalize(entry)
                if year_start and paper["year"] and paper["year"] < year_start:
                    continue
                if year_end and paper["year"] and paper["year"] > year_end:
                    continue
                papers.append(paper)

            start += len(entries)
            if len(entries) < current_batch:
                break

    finally:
        if own_client:
            await client.aclose()

    logger.info("arXiv: %d 件取得 (query=%r)", len(papers), query)
    return papers


def _build_query(query: str, categories: list[str] | None = None) -> str:
    """arXiv 検索クエリ文字列を構築する。

    Args:
        query: ユーザーの検索クエリ。
        categories: カテゴリフィルタリスト。

    Returns:
        arXiv API 用のクエリ文字列。
    """
    # 複数語の場合はダブルクォートで囲んでフレーズ検索にする
    escaped = query.strip()
    if " " in escaped:
        escaped = f'"{escaped}"'
    search_part = f"all:{escaped}"

    if categories:
        cat_parts = [f"cat:{cat}" for cat in categories]
        cat_query = " OR ".join(cat_parts)
        return f"({search_part}) AND ({cat_query})"

    return search_part


def _parse_year_range(year_range: str | None) -> tuple[int | None, int | None]:
    """年範囲文字列をパースする。

    Args:
        year_range: "2020-2025" 形式の文字列。

    Returns:
        (開始年, 終了年) のタプル。
    """
    if not year_range:
        return None, None
    parts = year_range.split("-")
    if len(parts) == 2:
        try:
            return int(parts[0]), int(parts[1])
        except ValueError:
            return None, None
    return None, None


def _normalize(entry: dict[str, Any]) -> dict[str, Any]:
    """arXiv のエントリを統一フォーマットに正規化する。

    Args:
        entry: xmltodict でパースした arXiv エントリ。

    Returns:
        統一フォーマットの論文辞書。
    """
    # タイトル
    title = entry.get("title", "")
    if isinstance(title, dict):
        title = title.get("#text", "")
    title = re.sub(r"\s+", " ", title).strip()

    # 著者
    authors_raw = entry.get("author", [])
    if isinstance(authors_raw, dict):
        authors_raw = [authors_raw]
    authors = [a.get("name", "") for a in authors_raw if isinstance(a, dict)]

    # 年（published フィールドから抽出）
    published = entry.get("published", "")
    year = None
    if published:
        match = re.match(r"(\d{4})", published)
        if match:
            year = int(match.group(1))

    # Abstract
    summary = entry.get("summary", "")
    if isinstance(summary, dict):
        summary = summary.get("#text", "")
    abstract = re.sub(r"\s+", " ", summary).strip()

    # URL と arXiv ID
    arxiv_id = entry.get("id", "")
    url = arxiv_id

    # DOI（arXiv エントリ内のリンクから取得）
    doi = None
    links = entry.get("link", [])
    if isinstance(links, dict):
        links = [links]
    for link in links:
        if isinstance(link, dict) and link.get("@title") == "doi":
            href = link.get("@href", "")
            doi_match = re.search(r"(10\.\d{4,}/\S+)", href)
            if doi_match:
                doi = doi_match.group(1)

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "abstract": abstract,
        "citation_count": 0,  # arXiv API は被引用数を提供しない
        "doi": doi,
        "url": url,
        "source": "arxiv",
        "tldr": "",
        "evidence_level": None,
    }


async def _main(query: str) -> None:
    """CLI動作確認用のエントリポイント。"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    papers = await search_papers(query, max_results=5)
    print(f"\n=== arXiv: {len(papers)} 件取得 ===\n")
    for i, p in enumerate(papers, 1):
        print(f"[{i}] {p['title']}")
        print(f"    Authors: {', '.join(p['authors'][:3])}{'...' if len(p['authors']) > 3 else ''}")
        print(f"    Year: {p['year']}  DOI: {p['doi'] or 'N/A'}")
        print(f"    URL: {p['url']}")
        print()


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "large language model"
    asyncio.run(_main(query))
