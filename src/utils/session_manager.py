"""セッション管理モジュール。

研究セッションのIDを生成し、出力ディレクトリを管理する。
各セッションは outputs/{session_id}/ にフェーズごとの成果物を保存する。
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from src.config import OUTPUTS_DIR


def create_session(theme: str) -> dict[str, Any]:
    """新しい研究セッションを作成する。

    Args:
        theme: ユーザーの研究テーマ。

    Returns:
        セッション情報の辞書:
        {
            "session_id": "20260227_143052_llm_hallucination",
            "theme": "LLM hallucination detection",
            "output_dir": Path("outputs/20260227_143052_llm_hallucination"),
            "created_at": "2026-02-27T14:30:52"
        }
    """
    session_id = _generate_session_id(theme)
    output_dir = OUTPUTS_DIR / session_id
    output_dir.mkdir(parents=True, exist_ok=True)

    session_info = {
        "session_id": session_id,
        "theme": theme,
        "output_dir": str(output_dir),
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }

    # セッション情報を保存
    meta_path = output_dir / "session_meta.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(session_info, f, ensure_ascii=False, indent=2)

    return session_info


def get_session_dir(session_id: str) -> Path:
    """セッションの出力ディレクトリを取得する。

    Args:
        session_id: セッションID。

    Returns:
        出力ディレクトリの Path。
    """
    return OUTPUTS_DIR / session_id


def list_sessions() -> list[dict[str, Any]]:
    """既存のセッション一覧を取得する。

    Returns:
        セッション情報のリスト（新しい順）。
    """
    sessions = []
    if not OUTPUTS_DIR.exists():
        return sessions

    for d in sorted(OUTPUTS_DIR.iterdir(), reverse=True):
        if not d.is_dir():
            continue
        meta_path = d / "session_meta.json"
        if meta_path.exists():
            with open(meta_path, encoding="utf-8") as f:
                sessions.append(json.load(f))
        else:
            # メタ情報がない場合は最低限の情報
            sessions.append({
                "session_id": d.name,
                "theme": "(unknown)",
                "output_dir": str(d),
            })

    return sessions


def get_phase_path(session_id: str, phase: int) -> Path:
    """フェーズの出力ファイルパスを取得する。

    Args:
        session_id: セッションID。
        phase: フェーズ番号（1-5）。

    Returns:
        出力ファイルの Path。
    """
    filenames = {
        1: "01_search_plan.md",
        2: "02_raw_papers.json",
        3: "03_screening.md",
        4: "04_synthesis.md",
        5: "05_report.md",
        6: "06_notion_url.txt",
    }
    if phase not in filenames:
        raise ValueError(f"Invalid phase: {phase}. Must be 1-6.")

    return get_session_dir(session_id) / filenames[phase]


def _generate_session_id(theme: str) -> str:
    """テーマからセッションIDを生成する。

    フォーマット: YYYYMMDD_HHMMSS_slug
    slug はテーマの英数字のみ（スネークケース、最大30文字）

    Args:
        theme: 研究テーマ。

    Returns:
        セッションID文字列。
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = _slugify(theme)
    return f"{timestamp}_{slug}"


def _slugify(text: str, max_length: int = 30) -> str:
    """テキストをURL/ファイル名用のスラッグに変換する。

    Args:
        text: 変換するテキスト。
        max_length: スラッグの最大文字数。

    Returns:
        スラッグ文字列。
    """
    # 小文字化
    text = text.lower()
    # 英数字とスペース以外を除去
    text = re.sub(r"[^a-z0-9\s]", "", text)
    # スペースをアンダースコアに
    text = re.sub(r"\s+", "_", text).strip("_")
    # 最大長で切る
    if len(text) > max_length:
        text = text[:max_length].rstrip("_")
    return text or "research"
