"""OpenAlex API クライアント。

OpenAlex REST API を使用して学術論文を検索する。
カーソルベースページネーションと polite pool（mailto）に対応。
"""

from __future__ import annotations

import asyncio
import logging
import sys
from typing import Any

import httpx

from src.config import OPENALEX_API_URL, OPENALEX_EMAIL

logger = logging.getLogger(__name__)


async def search_papers(
    query: str,
    *,
    year_range: str | None = None,
    max_results: int = 100,
    min_citations: int | None = None,
    client: httpx.AsyncClient | None = None,
) -> list[dict[str, Any]]:
    """OpenAlex で論文を検索する。

    Args:
        query: 検索クエリ文字列。
        year_range: 出版年の範囲（例: "2020-2025"）。
        max_results: 取得する最大論文数。
        min_citations: 最小被引用数フィルタ。
        client: 既存の httpx.AsyncClient（指定しなければ内部で生成）。

    Returns:
        統一フォーマットに正規化された論文辞書のリスト。
    """
    papers: list[dict[str, Any]] = []
    cursor = "*"

    own_client = client is None
    if own_client:
        client = httpx.AsyncClient(timeout=30.0)

    try:
        while len(papers) < max_results and cursor:
            per_page = min(50, max_results - len(papers))
            params: dict[str, Any] = {
                "search": query,
                "per_page": per_page,
                "cursor": cursor,
                "sort": "cited_by_count:desc",
                "select": "id,doi,title,display_name,publication_year,cited_by_count,authorships,abstract_inverted_index,primary_location,type",
            }

            # polite pool
            if OPENALEX_EMAIL:
                params["mailto"] = OPENALEX_EMAIL

            # フィルタ構築
            filters = _build_filters(year_range, min_citations)
            if filters:
                params["filter"] = filters

            try:
                resp = await client.get(f"{OPENALEX_API_URL}/works", params=params)
                resp.raise_for_status()
            except httpx.HTTPError as e:
                logger.error("OpenAlex request error: %s", e)
                break

            data = resp.json()
            results = data.get("results", [])
            if not results:
                break

            for raw in results:
                papers.append(_normalize(raw))

            # カーソルベースページネーション
            meta = data.get("meta", {})
            cursor = meta.get("next_cursor")
            if not cursor:
                break

    finally:
        if own_client:
            await client.aclose()

    logger.info("OpenAlex: %d 件取得 (query=%r)", len(papers), query)
    return papers


def _build_filters(
    year_range: str | None = None,
    min_citations: int | None = None,
) -> str:
    """OpenAlex のフィルタ文字列を構築する。

    Args:
        year_range: "2020-2025" 形式の年範囲。
        min_citations: 最小被引用数。

    Returns:
        カンマ区切りのフィルタ文字列。
    """
    parts: list[str] = []

    if year_range:
        years = year_range.split("-")
        if len(years) == 2:
            parts.append(f"publication_year:{years[0]}-{years[1]}")

    if min_citations is not None:
        parts.append(f"cited_by_count:>{min_citations}")

    return ",".join(parts)


def _normalize(raw: dict[str, Any]) -> dict[str, Any]:
    """OpenAlex の生データを統一フォーマットに正規化する。

    Args:
        raw: APIレスポンスの1論文分の辞書。

    Returns:
        統一フォーマットの論文辞書。
    """
    # 著者
    authorships = raw.get("authorships") or []
    authors = []
    for a in authorships:
        author_info = a.get("author", {})
        name = author_info.get("display_name", "")
        if name:
            authors.append(name)

    # DOI
    doi_raw = raw.get("doi") or ""
    doi = doi_raw.replace("https://doi.org/", "") if doi_raw else None

    # Abstract（inverted index から復元）
    abstract = _reconstruct_abstract(raw.get("abstract_inverted_index"))

    # URL
    url = ""
    primary_location = raw.get("primary_location") or {}
    landing_page = primary_location.get("landing_page_url")
    if landing_page:
        url = landing_page
    elif doi_raw:
        url = doi_raw

    return {
        "title": raw.get("display_name") or raw.get("title", ""),
        "authors": authors,
        "year": raw.get("publication_year"),
        "abstract": abstract,
        "citation_count": raw.get("cited_by_count", 0),
        "doi": doi,
        "url": url,
        "source": "openalex",
        "tldr": "",
        "evidence_level": None,
    }


def _reconstruct_abstract(inverted_index: dict[str, list[int]] | None) -> str:
    """OpenAlex の inverted index から abstract テキストを復元する。

    Args:
        inverted_index: {"word": [position1, position2, ...]} 形式の辞書。

    Returns:
        復元された abstract テキスト。
    """
    if not inverted_index:
        return ""

    word_positions: list[tuple[int, str]] = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))

    word_positions.sort(key=lambda x: x[0])
    return " ".join(word for _, word in word_positions)


async def _main(query: str) -> None:
    """CLI動作確認用のエントリポイント。"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    papers = await search_papers(query, max_results=5)
    print(f"\n=== OpenAlex: {len(papers)} 件取得 ===\n")
    for i, p in enumerate(papers, 1):
        print(f"[{i}] {p['title']}")
        print(f"    Authors: {', '.join(p['authors'][:3])}{'...' if len(p['authors']) > 3 else ''}")
        print(f"    Year: {p['year']}  Citations: {p['citation_count']}")
        print(f"    DOI: {p['doi'] or 'N/A'}")
        print()


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "large language model"
    asyncio.run(_main(query))
