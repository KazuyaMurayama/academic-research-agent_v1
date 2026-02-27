"""Semantic Scholar API クライアント。

Semantic Scholar Graph API を使用して学術論文を検索する。
レート制限ハンドリング（429時の指数バックオフ）とAPIキー対応を含む。
"""

from __future__ import annotations

import asyncio
import json
import logging
import sys
from typing import Any

import httpx

from src.config import (
    SEMANTIC_SCHOLAR_API_KEY,
    SEMANTIC_SCHOLAR_API_URL,
    SEMANTIC_SCHOLAR_FIELDS,
)

logger = logging.getLogger(__name__)

# tldr フィールドを追加（config の基本フィールド + tldr）
_SEARCH_FIELDS = SEMANTIC_SCHOLAR_FIELDS + ["tldr"]


async def search_papers(
    query: str,
    *,
    year_range: str | None = None,
    max_results: int = 100,
    client: httpx.AsyncClient | None = None,
) -> list[dict[str, Any]]:
    """Semantic Scholar で論文を検索する。

    Args:
        query: 検索クエリ文字列。
        year_range: 出版年の範囲（例: "2020-2025"）。
        max_results: 取得する最大論文数。
        client: 既存の httpx.AsyncClient（指定しなければ内部で生成）。

    Returns:
        統一フォーマットに正規化された論文辞書のリスト。
    """
    papers: list[dict[str, Any]] = []
    offset = 0
    limit = min(max_results, 100)

    own_client = client is None
    if own_client:
        client = httpx.AsyncClient(timeout=30.0)

    try:
        while offset < max_results:
            batch_limit = min(limit, max_results - offset)
            params: dict[str, Any] = {
                "query": query,
                "offset": offset,
                "limit": batch_limit,
                "fields": ",".join(_SEARCH_FIELDS),
            }
            if year_range:
                params["year"] = year_range

            headers: dict[str, str] = {}
            if SEMANTIC_SCHOLAR_API_KEY:
                headers["x-api-key"] = SEMANTIC_SCHOLAR_API_KEY

            response = await _request_with_backoff(
                client,
                f"{SEMANTIC_SCHOLAR_API_URL}/paper/search",
                params=params,
                headers=headers,
            )

            if response is None:
                logger.warning("Semantic Scholar: リクエスト失敗、取得中断")
                break

            data = response.json()
            batch = data.get("data", [])
            if not batch:
                break

            for raw in batch:
                papers.append(_normalize(raw))

            total_available = data.get("total", 0)
            offset += len(batch)
            if offset >= total_available:
                break

    finally:
        if own_client:
            await client.aclose()

    logger.info("Semantic Scholar: %d 件取得 (query=%r)", len(papers), query)
    return papers


async def _request_with_backoff(
    client: httpx.AsyncClient,
    url: str,
    *,
    params: dict[str, Any],
    headers: dict[str, str],
    max_retries: int = 5,
    initial_wait: float = 5.0,
    max_wait: float = 60.0,
) -> httpx.Response | None:
    """429 レート制限時に指数バックオフでリトライする。

    Args:
        client: HTTPクライアント。
        url: リクエストURL。
        params: クエリパラメータ。
        headers: リクエストヘッダー。
        max_retries: 最大リトライ回数。
        initial_wait: 初回待機秒数。
        max_wait: 最大待機秒数。

    Returns:
        成功時は httpx.Response、全リトライ失敗時は None。
    """
    wait = initial_wait
    for attempt in range(max_retries + 1):
        try:
            resp = await client.get(url, params=params, headers=headers)
            if resp.status_code == 429:
                if attempt < max_retries:
                    logger.warning(
                        "Semantic Scholar: 429 rate limited, waiting %.1fs (attempt %d/%d)",
                        wait, attempt + 1, max_retries,
                    )
                    await asyncio.sleep(wait)
                    wait = min(wait * 2, max_wait)
                    continue
                logger.error("Semantic Scholar: 429 rate limited, max retries exceeded")
                return None
            resp.raise_for_status()
            return resp
        except httpx.HTTPStatusError as e:
            logger.error("Semantic Scholar HTTP error: %s", e)
            return None
        except httpx.RequestError as e:
            logger.error("Semantic Scholar request error: %s", e)
            if attempt < max_retries:
                await asyncio.sleep(wait)
                wait = min(wait * 2, max_wait)
                continue
            return None
    return None


def _normalize(raw: dict[str, Any]) -> dict[str, Any]:
    """Semantic Scholar の生データを統一フォーマットに正規化する。

    Args:
        raw: APIレスポンスの1論文分の辞書。

    Returns:
        統一フォーマットの論文辞書。
    """
    authors = [a.get("name", "") for a in (raw.get("authors") or [])]
    external_ids = raw.get("externalIds") or {}
    doi = external_ids.get("DOI")
    tldr = raw.get("tldr")
    tldr_text = tldr.get("text", "") if isinstance(tldr, dict) else ""

    return {
        "title": raw.get("title", ""),
        "authors": authors,
        "year": raw.get("year"),
        "abstract": raw.get("abstract", ""),
        "citation_count": raw.get("citationCount", 0),
        "doi": doi,
        "url": raw.get("url", ""),
        "source": "semantic_scholar",
        "tldr": tldr_text,
        "evidence_level": None,
    }


async def _main(query: str) -> None:
    """CLI動作確認用のエントリポイント。"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    papers = await search_papers(query, max_results=5)
    print(f"\n=== Semantic Scholar: {len(papers)} 件取得 ===\n")
    for i, p in enumerate(papers, 1):
        print(f"[{i}] {p['title']}")
        print(f"    Authors: {', '.join(p['authors'][:3])}{'...' if len(p['authors']) > 3 else ''}")
        print(f"    Year: {p['year']}  Citations: {p['citation_count']}")
        print(f"    DOI: {p['doi'] or 'N/A'}")
        if p["tldr"]:
            print(f"    TLDR: {p['tldr'][:120]}...")
        print()


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "large language model"
    asyncio.run(_main(query))
