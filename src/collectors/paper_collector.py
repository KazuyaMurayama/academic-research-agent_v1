"""統合論文収集エンジン。

3つの学術API（Semantic Scholar, arXiv, OpenAlex）から非同期並列で論文を収集し、
DOIベースの重複排除後、被引用数でソートして統一フォーマットで出力する。

CLI使用例:
    python src/collectors/paper_collector.py \
        --queries "LLM hallucination" "large language model faithfulness" \
        --years 2022-2025 \
        --max-results 50 \
        --output outputs/test/02_raw_papers.json
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path
from typing import Any

import httpx

# プロジェクトルートをパスに追加（CLI直接実行用）
_project_root = Path(__file__).resolve().parent.parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from src.apis import arxiv_client, openalex_client, semantic_scholar
from src.utils.deduplicator import deduplicate

logger = logging.getLogger(__name__)


async def collect_papers(
    queries: list[str],
    *,
    year_range: str | None = None,
    max_results: int = 100,
) -> dict[str, Any]:
    """複数のクエリ・APIから論文を収集し、重複排除・ソートして返す。

    Args:
        queries: 検索クエリのリスト。
        year_range: 出版年範囲（例: "2020-2025"）。
        max_results: API ごとの最大取得件数。

    Returns:
        メタデータと論文リストを含む辞書:
        {
            "metadata": { ... },
            "papers": [ ... ]
        }
    """
    all_papers: list[dict[str, Any]] = []
    api_stats: dict[str, int] = {
        "semantic_scholar": 0,
        "arxiv": 0,
        "openalex": 0,
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        for query in queries:
            logger.info("検索クエリ: %r", query)

            # 3つのAPIを並列実行
            results = await asyncio.gather(
                _safe_search(
                    semantic_scholar.search_papers,
                    query,
                    year_range=year_range,
                    max_results=max_results,
                    client=client,
                ),
                _safe_search(
                    arxiv_client.search_papers,
                    query,
                    year_range=year_range,
                    max_results=max_results,
                    client=client,
                ),
                _safe_search(
                    openalex_client.search_papers,
                    query,
                    year_range=year_range,
                    max_results=max_results,
                    client=client,
                ),
            )

            for source_name, papers in zip(api_stats.keys(), results):
                api_stats[source_name] += len(papers)
                all_papers.extend(papers)

    total_before = len(all_papers)
    unique_papers = deduplicate(all_papers)
    total_after = len(unique_papers)

    # 被引用数でソート（降順）
    unique_papers.sort(key=lambda p: p.get("citation_count", 0), reverse=True)

    logger.info(
        "収集完了: 総数 %d → 重複排除後 %d（除去: %d）",
        total_before, total_after, total_before - total_after,
    )

    return {
        "metadata": {
            "queries": queries,
            "year_range": year_range,
            "max_results_per_api": max_results,
            "total_collected": total_before,
            "duplicates_removed": total_before - total_after,
            "unique_papers": total_after,
            "api_stats": api_stats,
        },
        "papers": unique_papers,
    }


async def _safe_search(search_fn: Any, *args: Any, **kwargs: Any) -> list[dict[str, Any]]:
    """API検索をエラーハンドリング付きで実行する。

    Args:
        search_fn: 検索関数。
        *args: 位置引数。
        **kwargs: キーワード引数。

    Returns:
        論文リスト。エラー時は空リスト。
    """
    try:
        return await search_fn(*args, **kwargs)
    except Exception as e:
        logger.error("API検索エラー (%s): %s", search_fn.__module__, e)
        return []


def save_results(data: dict[str, Any], output_path: str | Path) -> Path:
    """収集結果をJSONファイルに保存する。

    Args:
        data: 収集結果の辞書。
        output_path: 出力ファイルパス。

    Returns:
        保存先の Path オブジェクト。
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logger.info("結果を保存: %s", path)
    return path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """CLI引数をパースする。

    Args:
        argv: コマンドライン引数（テスト用にオプション）。

    Returns:
        パース済み引数。
    """
    parser = argparse.ArgumentParser(
        description="複数の学術APIから論文を収集する統合検索エンジン",
    )
    parser.add_argument(
        "--queries",
        nargs="+",
        required=True,
        help="検索クエリ（複数指定可）",
    )
    parser.add_argument(
        "--years",
        type=str,
        default=None,
        help="出版年範囲（例: 2020-2025）",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=100,
        help="APIごとの最大取得件数（デフォルト: 100）",
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="出力JSONファイルパス",
    )
    return parser.parse_args(argv)


async def _async_main(args: argparse.Namespace) -> None:
    """非同期メインルーチン。"""
    data = await collect_papers(
        queries=args.queries,
        year_range=args.years,
        max_results=args.max_results,
    )

    save_results(data, args.output)

    meta = data["metadata"]
    print(f"\n{'='*60}")
    print(f"論文収集完了")
    print(f"{'='*60}")
    print(f"クエリ: {', '.join(meta['queries'])}")
    print(f"年範囲: {meta['year_range'] or '制限なし'}")
    print(f"\nAPI別取得数:")
    for api, count in meta["api_stats"].items():
        print(f"  - {api}: {count} 件")
    print(f"\n総収集数: {meta['total_collected']} 件")
    print(f"重複排除: {meta['duplicates_removed']} 件")
    print(f"最終結果: {meta['unique_papers']} 件")
    print(f"\n出力: {args.output}")

    # 上位5件を表示
    if data["papers"]:
        print(f"\n--- 被引用数上位5件 ---")
        for i, p in enumerate(data["papers"][:5], 1):
            print(f"[{i}] {p['title']}")
            authors = p['authors'][:3]
            suffix = '...' if len(p['authors']) > 3 else ''
            print(f"    {', '.join(authors)}{suffix} ({p['year']})")
            print(f"    Citations: {p['citation_count']}  Source: {p['source']}")


def main() -> None:
    """CLIエントリポイント。"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    args = parse_args()
    asyncio.run(_async_main(args))


if __name__ == "__main__":
    main()
