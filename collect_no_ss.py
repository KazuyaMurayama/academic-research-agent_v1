"""Semantic Scholarをスキップした論文収集スクリプト（OpenAlex + arXivのみ）"""
import asyncio
import json
import sys
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).parent))

from src.apis import arxiv_client, openalex_client
from src.collectors.paper_collector import deduplicate


async def collect(queries: list[str], year_range: str, max_results: int, output: str):
    all_papers = []
    async with httpx.AsyncClient(timeout=30.0) as client:
        for query in queries:
            print(f"[QUERY] {query}", flush=True)
            try:
                oa = await openalex_client.search_papers(
                    query, year_range=year_range, max_results=max_results, client=client
                )
                print(f"  OpenAlex: {len(oa)}", flush=True)
                all_papers.extend(oa)
            except Exception as e:
                print(f"  OpenAlex error: {e}", flush=True)
            try:
                ax = await arxiv_client.search_papers(
                    query, year_range=year_range, max_results=max_results, client=client
                )
                print(f"  arXiv: {len(ax)}", flush=True)
                all_papers.extend(ax)
            except Exception as e:
                print(f"  arXiv error: {e}", flush=True)

    unique = deduplicate(all_papers)
    unique.sort(key=lambda p: p.get("citation_count", 0), reverse=True)
    result = {
        "metadata": {
            "queries": queries,
            "year_range": year_range,
            "total_collected": len(all_papers),
            "total_unique": len(unique),
        },
        "papers": unique,
    }
    Path(output).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"[DONE] {len(unique)} unique papers saved to {output}", flush=True)


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--queries", nargs="+", required=True)
    p.add_argument("--years", default="2015-2026")
    p.add_argument("--max-results", type=int, default=15)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    asyncio.run(collect(args.queries, args.years, args.max_results, args.output))
