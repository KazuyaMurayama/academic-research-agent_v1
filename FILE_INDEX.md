# FILE INDEX - academic-research-agent_v1

> 最終更新: 2026-06-04 | ファイル数: 212（R042〜R046追加）

## ディレクトリ構造 (depth=5)

```
.
├── .claude/
│   ├── rules/
│   │   ├── git-rules.md
│   │   ├── model-selection.md
│   │   ├── output-rules.md
│   │   └── timeout-prevention.md
│   ├── settings.json
│   └── skills/
│       ├── research/
│       │   └── SKILL.md
│       ├── research-quick/
│       │   └── SKILL.md
│       └── search-only/
│           └── SKILL.md
├── .env.example
├── .gitignore
├── CLAUDE.md
├── FILE_INDEX.md
├── README.md
├── collect_no_ss.py
├── outputs/  (gitignore対象)
├── prompts/
│   └── .gitkeep
├── reports/
│   ├── [R001-R046 レポートファイル群]
│   └── INDEX.md
├── requirements.txt
├── src/
│   ├── apis/
│   ├── collectors/
│   ├── config.py
│   ├── notion_client.py
│   └── utils/
├── tasks.md
└── templates/
    └── report_template.md
```

## カテゴリ別ファイル一覧

### Documentation (主要ファイル)

| ファイルパス | 説明 | 最終更新 | 優先度 |
|---|---|---|---|
| `CLAUDE.md` | プロジェクト運用ルール（最重要） | 2026-05-15 | 高 |
| `tasks.md` | タスク管理 | 2026-06-04 | 高 |
| `FILE_INDEX.md` | このファイル（ファイルインデックス） | 2026-06-04 | 高 |
| `reports/INDEX.md` | レポートカタログ（R001〜R046） | 2026-06-04 | 高 |
| `.claude/rules/git-rules.md` | Git操作ルール | 2026-05-15 | 高 |
| `.claude/rules/output-rules.md` | 成果物・報告ルール | 2026-05-15 | 高 |
| `.claude/rules/timeout-prevention.md` | タイムアウト防止・大ファイル生成ルール | 2026-05-15 | 高 |
| `.claude/rules/model-selection.md` | モデル使い分けルール | 2026-05-15 | 中 |
| `.claude/skills/research/SKILL.md` | /research スキル定義 | 2026-05-15 | 中 |
| `.claude/skills/research-quick/SKILL.md` | /research-quick スキル定義 | 2026-05-15 | 中 |
| `.claude/skills/search-only/SKILL.md` | /search-only スキル定義 | 2026-05-15 | 中 |
| `README.md` | プロジェクト概要 | 2026-04 | 低 |
| `templates/report_template.md` | レポートテンプレート | 2026-04 | 低 |

### Reports (レポートファイル R001〜R046)

| ファイルパス | レポートID | テーマ | 作成日 |
|---|---|---|---|
| `reports/2026-02-28_llm-hallucination-reduction.md` | R001 | LLMハルシネーション低減 | 2026-02-28 |
| `reports/2026-02-28_vision-loss-dry-eye-prevention.md` | R002 | 視力低下・ドライアイ改善 | 2026-02-28 |
| `reports/2026-02-28_healthy-lifestyle-habits.md` | R003 | 健康になるための習慣 | 2026-02-28 |
| `reports/2026-02-28_happiness-wellbeing-habits.md` | R004 | 幸福度を高めるための習慣 | 2026-02-28 |
| `reports/2026-03-01_grip-strength-training.md` | R005 | 握力トレーニングの効果 | 2026-03-01 |
| `reports/2026-03-02_eye-fatigue-vision-protection.md` | R006 | 目の疲労改善・視力低下防止 | 2026-03-02 |
| `reports/2026-03-02_kettlebell-training-effects.md` | R007 | ケトルベルトレーニングの効果 | 2026-03-02 |
| `reports/2026-03-03_antiaging-longevity-interventions.md` | R008 | アンチエイジング・長寿介入 | 2026-03-03 |
| `reports/2026-04-06_四時間労働の効果_幸福度・認知・健康・文化.md` | R009 | 1日4時間以内労働時間制限 | 2026-04-06 |
| `reports/2026-03-11_8exercises-comparison.md` | R010 | 注目すべき8つの運動の効果比較 | 2026-03-11 |
| `reports/2026-03-12_low-back-pain-prevention.md` | R011 | 腰痛を防ぐために有効な方法 | 2026-03-12 |
| `reports/2026-03-14_collagen-peptide-supplement.md` | R012 | コラーゲンペプチドサプリの効果 | 2026-03-14 |
| `reports/2026-03-15_creatine-supplement.md` | R013 | クレアチンサプリの健康効果 | 2026-03-15 |
| `reports/2026-03-15_resistant-dextrin.md` | R014 | 難消化性デキストリンの健康効果 | 2026-03-15 |
| `reports/2026-03-22_fasting-health-effects.md` | R015 | 断食（ファスティング）の健康効果 | 2026-03-22 |
| `reports/2026-03-23_bath-co2-effects.md` | R016 | 入浴剤バブ（炭酸ガス入浴）の効果 | 2026-03-23 |
| `reports/2026-03-27_immunity-boost.md` | R017 | 免疫力を高める方法 | 2026-03-27 |
| `reports/2026-03-28_visceral-fat-reduction.md` | R018 | 内臓脂肪を減らす・増やす要因 | 2026-03-28 |
| `reports/2026-03-30_pediatric-constipation-fiber.md` | R019 | 小児の便秘改善における食物繊維4種 | 2026-03-30 |
| `reports/2026-03-31_neck-pain-stretching-exercise.md` | R020 | ストレートネック・首の痛み改善 | 2026-03-31 |
| `reports/2026-04-01_scalp-care-hair-maintenance.md` | R021 | 40代男性のための頭皮ケア・毛髪維持 | 2026-04-01 |
| `reports/2026-04-02_diabetes-drugs-nondiabetic.md` | R022 | 糖尿病薬の健常者への使用効果 | 2026-04-02 |
| `reports/2026-04-03_infant-gut-microbiome.md` | R023 | 赤ちゃん・幼児の腸内環境と発達 | 2026-04-03 |
| `reports/2026-04-13_hayfever-supplements-vs-drugs.md` | R024 | 花粉症・黄砂×サプリvs薬 | 2026-04-13 |
| `reports/2026-04-21_gastric-cancer-prevention-scoring.md` | R025 | 胃がん予防介入スコアリング | 2026-04-21 |
| `reports/2026-04-28_supplement-drug-risk-analysis.md` | R026 | 40代男性サプリ＆処方薬リスク分析 | 2026-04-28 |
| `reports/2026-04-28_immunity-boost-v2.md` | R027 | 免疫力強化v2: 16介入スコアリング | 2026-04-28 |
| `reports/2026-04-30_cold-remedy-evidence.md` | R028 | 風邪介入エビデンス評価 | 2026-04-30 |
| `reports/2026-04-30_genai-instruction-design.md` | R029 | 生成AIツール活用・指示設計ガイド | 2026-04-30 |
| `reports/2026-05-05_soy-intake-health-effects-men.md` | R030 | 豆製品摂取と男性健康影響 | 2026-05-05 |
| `reports/2026-05-07_hq-vs-niacinamide-concentration-efficacy.md` | R031 | HQ vs ナイアシンアミド美白比較 | 2026-05-07 |
| `reports/2026-05-09_pediatric-constipation-pdx-vs-peg-vs-lactulose.md` | R032 | 小児便秘 PDX vs PEG vs ラクツロース | 2026-05-09 |
| `reports/2026-05-13_brain-health-factcheck.md` | R033 | 脳神経科学ファクトチェック | 2026-05-13 |
| `reports/2026-05-15_cbt-effects.md` | R034 | 認知行動療法（CBT）エビデンスレビュー | 2026-05-15 |
| `reports/2026-05-07_gachirack-dokkatsu-kakkonto-evidence.md` | R035 | ガチラック（独活葛根湯）エビデンス | 2026-05-07 |
| `reports/2026-05-07_neck-shoulder-stiffness-ingredients-comprehensive.md` | R036 | 肩こり・首こり改善成分18種 | 2026-05-07 |
| `reports/2026-05-08_cooking-oils-5way-comparison.md` | R037 | 食用油5種健康効果比較 | 2026-05-08 |
| `reports/2026-05-09_loxoprofen-LX-tape-evaluation.md` | R038 | リフェンダーLXテープ評価 | 2026-05-09 |
| `reports/2026-05-14_tetris-effects-comparison.md` | R039 | テトリスの科学的効果比較 | 2026-05-14 |
| `reports/2026-05-15_adult-constipation-interventions.md` | R040 | 成人便秘解消16介入スコアリング | 2026-05-15 |
| （R041欠番 — NY1301をR040に統合） | — | — | — |
| `reports/2026-05-20_nsaids-doms-muscle-hypertrophy.md` | R042 | NSAIDs筋肥大・筋力影響レビュー | 2026-05-20 |
| `reports/2026-05-20_alcohol-wine-health-effects-bias-corrected.md` | R043 | アルコール・ワイン健康影響レビュー | 2026-05-20 |
| `reports/2026-06-01_hair-quality-improvement-ingredients.md` | R044 | 髪質改善有効成分エビデンスガイド | 2026-06-01 |
| `reports/2026-06-04_supplement-evidence-review-sleep-stress-4products.md` | R045 | iHerbサプリ4種エビデンス評価 | 2026-06-04 |
| `reports/2026-06-04_supplement-product-search-optimized-dose.md` | R046 | サプリ代替製品コスパサーチ（用量改善） | 2026-06-04 |

### Code (13件)

| ファイルパス | サイズ(bytes) | SHA |
|---|---|---|
| `collect_no_ss.py` | 2229 | 6968e6c |
| `src/__init__.py` | 0 | e69de29 |
| `src/apis/__init__.py` | 190 | 662d929 |
| `src/apis/arxiv_client.py` | 7639 | 730a49d |
| `src/apis/openalex_client.py` | 6216 | c7f5e14 |
| `src/apis/semantic_scholar.py` | 6484 | 2db79e0 |
| `src/collectors/__init__.py` | 156 | 5a7d1f5 |
| `src/collectors/paper_collector.py` | 9234 | c3d10a4 |
| `src/config.py` | 3667 | f94f8ed |
| `src/notion_client.py` | 15101 | faff83b |
| `src/utils/__init__.py` | 262 | 2ea1101 |
| `src/utils/deduplicator.py` | 3258 | 19175ad |
| `src/utils/session_manager.py` | 4284 | 45b1bd7 |

### Config / Other

| ファイルパス | 説明 | 優先度 |
|---|---|---|
| `.claude/settings.json` | Claude Code設定 | 中 |
| `.gitignore` | Git除外設定 | 中 |
| `.env.example` | 環境変数テンプレート | 低 |
| `requirements.txt` | Pythonパッケージ依存関係 | 低 |
| `outputs/` | 中間出力（gitignore対象） | 低 |
