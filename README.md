# Academic Research Agent

論文サーチ＆エビデンスベースレポート自動生成システム。

ユーザーの研究テーマに対して、複数の学術APIから論文を自動収集し、Claude自身がスクリーニング・分析・統合を実行してPRISMA準拠の構造化レポートを生成します。

## セットアップ

### 1. 前提条件

- Python 3.10+
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI

### 2. インストール

```bash
git clone <repository-url>
cd academic-research-agent_v1
pip install -r requirements.txt
```

### 3. 環境変数（オプション）

`.env` ファイルを作成し、APIキーを設定すると検索の安定性が向上します。

```bash
# Semantic Scholar（レート制限緩和）
SEMANTIC_SCHOLAR_API_KEY=your_key_here

# OpenAlex（polite pool: 優先キュー）
OPENALEX_EMAIL=your_email@example.com
```

APIキーがなくても動作しますが、Semantic Scholar は 100 requests/5min の制限があります。

## 使い方

### スラッシュコマンド（Claude Code CLI内）

```bash
# フル論文サーチ＆レポート生成（5フェーズ）
/research 大規模言語モデルのハルシネーション低減手法

# 簡易版（検索→上位10本で即レポート）
/research-quick RAGの最新動向

# 論文リスト取得のみ
/search-only transformer architecture improvements
```

### Python CLI（直接実行）

```bash
# 各APIクライアント単体テスト
python -m src.apis.semantic_scholar "large language model"
python -m src.apis.arxiv_client "retrieval augmented generation"
python -m src.apis.openalex_client "hallucination detection"

# 統合論文収集
python src/collectors/paper_collector.py \
  --queries "LLM hallucination" "RAG faithfulness" \
  --years 2022-2026 \
  --max-results 50 \
  --output outputs/my_session/02_raw_papers.json
```

## ワークフロー（5フェーズ）

```
Phase 1: 検索戦略立案    → outputs/{session}/01_search_plan.md
Phase 2: 論文収集        → outputs/{session}/02_raw_papers.json
Phase 3: スクリーニング  → outputs/{session}/03_screening.md
Phase 4: エビデンス統合  → outputs/{session}/04_synthesis.md
Phase 5: レポート生成    → outputs/{session}/05_report.md
```

| フェーズ | 実行者 | 説明 |
|---------|--------|------|
| Phase 1 | Claude | テーマ分析、検索クエリ生成 |
| Phase 2 | Python | 3 API並列検索、重複排除 |
| Phase 3 | Claude | 関連性・影響度・エビデンスレベル評価 |
| Phase 4 | Claude | 個別要約、クロス分析、比較テーブル |
| Phase 5 | Claude | PRISMA準拠レポート生成 |

## プロジェクト構造

```
academic-research-agent_v1/
├── src/
│   ├── apis/
│   │   ├── semantic_scholar.py   # Semantic Scholar API
│   │   ├── arxiv_client.py       # arXiv API
│   │   └── openalex_client.py    # OpenAlex API
│   ├── collectors/
│   │   └── paper_collector.py    # 統合収集エンジン
│   ├── utils/
│   │   ├── deduplicator.py       # DOI/タイトル重複排除
│   │   └── session_manager.py    # セッション管理
│   └── config.py                 # 設定・定数
├── templates/
│   └── report_template.md        # PRISMAレポートテンプレート
├── .claude/skills/               # スラッシュコマンド定義
│   ├── research/
│   ├── research-quick/
│   └── search-only/
├── outputs/                      # 生成成果物（gitignore対象）
├── requirements.txt
└── CLAUDE.md                     # プロジェクト設定
```

## 対応API

| API | 特徴 | レート制限 |
|-----|------|-----------|
| Semantic Scholar | TLDR・被引用数・著者情報 | 100 req/5min（キーなし） |
| arXiv | プレプリント・最新研究 | 3秒間隔 |
| OpenAlex | 被引用数ソート・フルメタデータ | 制限なし（polite pool推奨） |

## 出力フォーマット

論文は以下の統一フォーマットで管理されます：

```json
{
  "title": "論文タイトル",
  "authors": ["Author1", "Author2"],
  "year": 2024,
  "abstract": "要旨...",
  "citation_count": 150,
  "doi": "10.xxxx/yyyy",
  "url": "https://...",
  "source": "semantic_scholar|arxiv|openalex",
  "tldr": "1文要約...",
  "evidence_level": null
}
```
