# FILE_INDEX.md — プロジェクト全ファイルマップ

> **新セッション開始時に必ずこのファイルを読む。**
> ファイル追加・削除時は必ずこのファイルを更新してコミットすること。
> 最終更新: 2026-04-21

---

## 📋 最初に読むべきファイル（優先順位順）

| 優先度 | ファイル | 内容 |
|---|---|---|
| ★★★ | `FILE_INDEX.md`（本ファイル） | プロジェクト全ファイルマップ |
| ★★★ | `tasks.md` | 未完了タスク・引き継ぎ情報 |
| ★★★ | `reports/INDEX.md` | 全レポートカタログ（R001〜、次はR025） |
| ★★ | `CLAUDE.md` | 最重要ルール・スキル一覧 |
| ★ | `.claude/rules/git-rules.md` | Git操作詳細ルール |
| ★ | `.claude/rules/output-rules.md` | 成果物・報告詳細ルール |
| ★ | `.claude/rules/model-selection.md` | Opus/Sonnet使い分けルール |

---

## 🗂️ ディレクトリ構造

```
academic-research-agent_v1/
├── CLAUDE.md                    ← 最重要ルール（軽量版）
├── FILE_INDEX.md                ← 本ファイル（全体マップ）
├── tasks.md                     ← タスク管理
├── README.md                    ← プロジェクト説明
├── collect_no_ss.py             ← SS障害時フォールバック収集スクリプト
├── requirements.txt             ← Python依存関係
├── .env.example                 ← 環境変数サンプル
├── .gitignore                   ← outputs/等を除外
│
├── reports/                     ← ★ 全レポートの正本（master必須）
│   ├── INDEX.md                 ← レポートカタログ（R001〜R024、次はR025）
│   └── YYYY-MM-DD_slug.md       ← 個別レポート（24本）
│
├── .claude/
│   ├── settings.json            ← Claude Code設定
│   ├── rules/                   ← ★ 詳細ルールファイル群
│   │   ├── git-rules.md
│   │   ├── output-rules.md
│   │   └── model-selection.md
│   └── skills/                  ← スラッシュコマンド定義
│       ├── research/SKILL.md
│       ├── research-quick/SKILL.md
│       └── search-only/SKILL.md
│
├── src/                         ← Pythonソースコード（データ収集・連携）
│   ├── config.py
│   ├── notion_client.py         ← Notion API連携クライアント
│   ├── apis/
│   │   ├── arxiv_client.py
│   │   ├── openalex_client.py
│   │   └── semantic_scholar.py
│   ├── collectors/
│   │   └── paper_collector.py   ← メイン収集スクリプト
│   └── utils/
│       ├── deduplicator.py
│       └── session_manager.py
│
├── prompts/                     ← プロンプトテンプレート置き場（現在空）
│
├── templates/
│   └── report_template.md       ← レポート雛形
│
└── outputs/                     ← gitignore済み（セッション一時ファイル）
    └── {session_id}/
        ├── 01_search_plan.md
        ├── 02_raw_papers.json
        ├── 03_screening.md
        ├── 04_synthesis.md
        └── 05_report.md
```

---

## 📄 reports/ — レポート一覧（R001〜R024）

> 詳細カタログは `reports/INDEX.md` を参照。このテーブルは構造把握用。

| ID | ファイル名 | テーマ | 更新日 |
|---|---|---|---|
| R001 | `2026-02-28_llm-hallucination-reduction.md` | LLMハルシネーション低減 | 2026-02-28 |
| R002 | `2026-02-28_vision-loss-dry-eye-prevention.md` | 視力低下・ドライアイ | 2026-02-28 |
| R003 | `2026-02-28_healthy-lifestyle-habits.md` | 健康習慣 | 2026-02-28 |
| R004 | `2026-02-28_happiness-wellbeing-habits.md` | 幸福度・ウェルビーイング | 2026-02-28 |
| R005 | `2026-03-01_grip-strength-training.md` | 握力トレーニング | 2026-03-01 |
| R006 | `2026-03-02_eye-fatigue-vision-protection.md` | 目の疲労・視力保護 | 2026-03-02 |
| R007 | `2026-03-02_kettlebell-training-effects.md` | ケトルベルトレーニング | 2026-03-02 |
| R008 | `2026-03-03_antiaging-longevity-interventions.md` | アンチエイジング・長寿 | 2026-03-03 |
| R009 | `2026-04-06_四時間労働の効果_幸福度・認知・健康・文化.md` | 4時間労働 | 2026-04-06 |
| R010 | `2026-03-11_8exercises-comparison.md` | 8運動エビデンス比較 | 2026-03-11 |
| R011 | `2026-03-12_low-back-pain-prevention.md` | 腰痛予防 | 2026-03-12 |
| R012 | `2026-03-14_collagen-peptide-supplement.md` | コラーゲンペプチド | 2026-03-14 |
| R013 | `2026-03-15_creatine-supplement.md` | クレアチン | 2026-03-15 |
| R014 | `2026-03-15_resistant-dextrin.md` | 難消化性デキストリン | 2026-03-15 |
| R015 | `2026-03-22_fasting-health-effects.md` | 断食・ファスティング | 2026-03-22 |
| R016 | `2026-03-23_bath-co2-effects.md` | 炭酸ガス入浴（バブ） | 2026-03-23 |
| R017 | `2026-03-27_immunity-boost.md` | 免疫力強化 | 2026-03-27 |
| R018 | `2026-03-28_visceral-fat-reduction.md` | 内臓脂肪 ※Section14追記 | 2026-04-13 |
| R019 | `2026-03-30_pediatric-constipation-fiber.md` | 小児便秘・食物繊維 ※Section11追記 | 2026-04-13 |
| R020 | `2026-03-31_neck-pain-stretching-exercise.md` | 首の痛み・ストレートネック | 2026-03-31 |
| R021 | `2026-04-01_scalp-care-hair-maintenance.md` | 頭皮ケア・毛髪維持 | 2026-04-01 |
| R022 | `2026-04-02_diabetes-drugs-nondiabetic.md` | 糖尿病薬の健常者使用 | 2026-04-02 |
| R023 | `2026-04-03_infant-gut-microbiome.md` | 乳幼児腸内環境 | 2026-04-03 |
| R024 | `2026-04-13_hayfever-supplements-vs-drugs.md` | 花粉症×サプリvs薬100点 | 2026-04-13 |
| R025 | `2026-04-21_gastric-cancer-prevention-scoring.md` | 胃がん予防介入スコアリング | 2026-04-21 |
| R026 | `2026-04-28_supplement-drug-risk-analysis.md` | 40代男性サプリ＆処方薬リスク分析 | 2026-04-28 |

**次のレポートID: R027**

---

## ⚙️ src/ — ソースコードファイル

| ファイル | 役割 | 備考 |
|---|---|---|
| `src/config.py` | API設定・年範囲デフォルト値 | 検索年範囲変更はここ |
| `src/notion_client.py` | Notion API連携クライアント | レポート自動保存用（467行） |
| `src/collectors/paper_collector.py` | メイン論文収集スクリプト | `--queries`, `--years`, `--max-results`, `--output` |
| `collect_no_ss.py` | SS障害時フォールバック | Semantic Scholar除外版 |
| `src/apis/arxiv_client.py` | arXiv API クライアント | 3秒間隔制限あり |
| `src/apis/openalex_client.py` | OpenAlex API クライアント | 被引用数降順ソート |
| `src/apis/semantic_scholar.py` | Semantic Scholar クライアント | タイムアウト多発→フォールバック推奨 |
| `src/utils/deduplicator.py` | DOIベース重複排除 | |
| `src/utils/session_manager.py` | セッションID管理 | |

---

## 🤖 .claude/ — Claude Code設定

| ファイル | 役割 |
|---|---|
| `.claude/settings.json` | Claude Code全体設定 |
| `.claude/rules/git-rules.md` | Git操作ルール詳細 |
| `.claude/rules/output-rules.md` | 成果物・報告ルール詳細 |
| `.claude/rules/model-selection.md` | Opus/Sonnet使い分け詳細 |
| `.claude/skills/research/SKILL.md` | `/research` コマンド定義（5フェーズ） |
| `.claude/skills/research-quick/SKILL.md` | `/research-quick` コマンド定義 |
| `.claude/skills/search-only/SKILL.md` | `/search-only` コマンド定義 |

---

## 🔖 ファイル更新ルール

1. **新ファイル追加時**: このファイルの該当セクションに1行追加
2. **ファイル削除・移動時**: 該当行を削除または更新
3. **レポート追加時**: `reports/` テーブルに1行追加（`reports/INDEX.md` も必ず更新）
4. **更新後は必ずコミット**: `git add FILE_INDEX.md && git commit -m "docs: FILE_INDEX.md更新"`
5. **masterへpush**: `git push origin HEAD:master`
