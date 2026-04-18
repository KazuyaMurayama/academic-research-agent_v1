"""Academic Research Agent の設定モジュール。

APIエンドポイント定義、デフォルトパラメータ、エビデンスレベル定義を管理する。
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# ─── プロジェクトパス ────────────────────────────────────────────
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent
OUTPUTS_DIR: Path = PROJECT_ROOT / "outputs"
TEMPLATES_DIR: Path = PROJECT_ROOT / "templates"

# ─── APIエンドポイント ───────────────────────────────────────────
SEMANTIC_SCHOLAR_API_URL: str = "https://api.semanticscholar.org/graph/v1"
ARXIV_API_URL: str = "https://export.arxiv.org/api/query"
OPENALEX_API_URL: str = "https://api.openalex.org"

# ─── APIキー（環境変数から読み込み） ──────────────────────────────
SEMANTIC_SCHOLAR_API_KEY: str | None = os.getenv("SEMANTIC_SCHOLAR_API_KEY") or None
OPENALEX_EMAIL: str | None = os.getenv("OPENALEX_EMAIL") or None

# ─── Notion API ──────────────────────────────────────────────────
NOTION_API_KEY: str | None = os.getenv("NOTION_API_KEY") or None
NOTION_DATABASE_ID: str | None = os.getenv("NOTION_DATABASE_ID") or None
NOTION_API_URL: str = "https://api.notion.com/v1"
NOTION_VERSION: str = "2022-06-28"

# ─── デフォルトパラメータ ────────────────────────────────────────
DEFAULT_YEAR_RANGE: str = "2021-2026"
DEFAULT_MAX_RESULTS: int = 100
BATCH_SIZE: int = 10  # コンテキスト窓対策: 論文を10本ずつ処理

# ─── レート制限 ──────────────────────────────────────────────────
SEMANTIC_SCHOLAR_RATE_LIMIT: int = 100  # requests per 5 min (without API key)
ARXIV_REQUEST_INTERVAL: float = 3.0  # seconds between requests

# ─── エビデンスレベル定義（Oxford CEBM） ─────────────────────────
EVIDENCE_LEVELS: dict[str, dict[str, str | int]] = {
    "1a": {"label": "SR of RCTs", "description": "Systematic Review of Randomized Controlled Trials", "rank": 1},
    "1b": {"label": "Individual RCT", "description": "Individual Randomized Controlled Trial", "rank": 2},
    "2a": {"label": "SR of Cohort", "description": "Systematic Review of Cohort Studies", "rank": 3},
    "2b": {"label": "Individual Cohort", "description": "Individual Cohort Study", "rank": 4},
    "3a": {"label": "SR of Case-Control", "description": "Systematic Review of Case-Control Studies", "rank": 5},
    "3b": {"label": "Individual Case-Control", "description": "Individual Case-Control Study", "rank": 6},
    "4": {"label": "Case Series", "description": "Case Series / Poor Quality Cohort or Case-Control", "rank": 7},
    "5": {"label": "Expert Opinion", "description": "Expert Opinion without Critical Appraisal", "rank": 8},
}

# ─── Semantic Scholar 取得フィールド ──────────────────────────────
SEMANTIC_SCHOLAR_FIELDS: list[str] = [
    "paperId",
    "title",
    "abstract",
    "authors",
    "year",
    "citationCount",
    "url",
    "venue",
    "publicationTypes",
    "externalIds",
]
