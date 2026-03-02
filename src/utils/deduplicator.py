"""論文の重複排除モジュール。

DOI完全一致 → DOIなしの場合はタイトル正規化後の完全一致で重複を検出する。
"""

from __future__ import annotations

import re
import unicodedata
from typing import Any


def deduplicate(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """論文リストから重複を排除する。

    重複判定の優先順:
    1. DOI 完全一致
    2. DOI がない場合: タイトル正規化後の完全一致

    重複がある場合、被引用数が多い方（または情報が豊富な方）を残す。

    Args:
        papers: 統一フォーマットの論文辞書リスト。

    Returns:
        重複排除済みの論文リスト。
    """
    seen_dois: dict[str, int] = {}
    seen_titles: dict[str, int] = {}
    unique: list[dict[str, Any]] = []

    for paper in papers:
        doi = paper.get("doi")
        normalized_title = _normalize_title(paper.get("title") or "")

        # DOI による重複チェック
        if doi:
            if doi in seen_dois:
                existing_idx = seen_dois[doi]
                if _should_replace(unique[existing_idx], paper):
                    unique[existing_idx] = paper
                continue
            seen_dois[doi] = len(unique)

        # タイトルによる重複チェック（DOI がない場合）
        if normalized_title:
            if normalized_title in seen_titles:
                existing_idx = seen_titles[normalized_title]
                if _should_replace(unique[existing_idx], paper):
                    unique[existing_idx] = paper
                continue
            seen_titles[normalized_title] = len(unique)

        unique.append(paper)

    return unique


def _normalize_title(title: str) -> str:
    """タイトルを正規化して比較用の文字列を生成する。

    Args:
        title: 論文タイトル。

    Returns:
        正規化されたタイトル文字列。
    """
    # Unicode正規化
    title = unicodedata.normalize("NFKC", title)
    # 小文字化
    title = title.lower()
    # 句読点・記号を除去
    title = re.sub(r"[^\w\s]", "", title)
    # 連続空白を1つに
    title = re.sub(r"\s+", " ", title).strip()
    return title


def _should_replace(existing: dict[str, Any], candidate: dict[str, Any]) -> bool:
    """既存の論文をcandidateで置き換えるべきか判定する。

    被引用数が多い方、abstract やDOI情報がある方を優先する。

    Args:
        existing: 既存の論文辞書。
        candidate: 候補の論文辞書。

    Returns:
        置き換えるべきなら True。
    """
    existing_score = _info_score(existing)
    candidate_score = _info_score(candidate)
    return candidate_score > existing_score


def _info_score(paper: dict[str, Any]) -> int:
    """論文の情報充実度スコアを算出する。

    Args:
        paper: 論文辞書。

    Returns:
        情報充実度スコア。
    """
    score = 0
    if paper.get("doi"):
        score += 10
    if paper.get("abstract"):
        score += 5
    if paper.get("tldr"):
        score += 3
    score += min(paper.get("citation_count", 0), 100)
    return score
