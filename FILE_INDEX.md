# FILE_INDEX — academic-research-agent_v1

> ⚠️ このファイルは自動生成です。手動編集は次回更新で上書きされます。

| 項目 | 値 |
|---|---|
| リポジトリ | KazuyaMurayama/academic-research-agent_v1 |
| ブランチ | master |
| 総ファイル数 | 191 |
| 最終更新 | 2026-05-02 |
| 管理者 | 男座員也（Kazuya Oza） |

---

## カテゴリ別サマリー

| カテゴリ | ファイル数 |
|---|---|
| Documentation | 136 |
| Code | 13 |
| Data | 34 |
| Config | 3 |
| Other | 5 |

---

## ディレクトリ構成

```
.
├── .claude/
│   ├── rules/
│   │   ├── git-rules.md
│   │   ├── model-selection.md
│   │   ├── output-rules.md
│   │   └── timeout-prevention.md
│   ├── skills/
│   │   ├── research/
│   │   │   ... (1 items)
│   │   ├── research-quick/
│   │   │   ... (1 items)
│   │   └── search-only/
│   │       ... (1 items)
│   └── settings.json
├── outputs/
│   ├── 20260228_100714_vision_loss_prevention_dry_eye/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   ├── 05_report.md
│   │   └── session_meta.json
│   ├── 20260228_102329_healthy_lifestyle_habits_longe/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   ├── 05_report.md
│   │   └── session_meta.json
│   ├── 20260228_104021_research/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   ├── 05_report.md
│   │   └── session_meta.json
│   ├── 20260301_222104_grip_strength_training_effecti/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   ├── 05_report.md
│   │   └── session_meta.json
│   ├── 20260302_070418_kettlebell_training_effects_co/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   ├── 05_report.md
│   │   └── session_meta.json
│   ├── 20260302_105343_eye_fatigue_vision_loss_preven/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   ├── 05_report.md
│   │   └── session_meta.json
│   ├── 20260303_005155_antiaging_longevity_evidenceba/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   ├── 05_report.md
│   │   └── session_meta.json
│   ├── 20260311_081644_7exercisescomparison/
│   │   ├── 02_bouldering.json
│   │   ├── 02_burpee.json
│   │   ├── 02_dumbbell.json
│   │   ├── 02_handstand.json
│   │   ├── 02_hiit_safety.json
│   │   ├── 02_hiit.json
│   │   ├── 02_kettlebell.json
│   │   ├── 02_pullup.json
│   │   ├── 02_pullup2.json
│   │   ├── 02_swimming.json
│   │   ├── 05_report.md
│   │   └── session_meta.json
│   ├── 20260312_lowbackpain_prevention/
│   │   ├── 01_search_plan.md
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   └── 05_report.md
│   ├── 20260314_collagen_peptide_supplement/
│   │   ├── 01_search_plan.md
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   └── 05_report.md
│   ├── 20260315_creatine_supplement/
│   │   ├── 01_search_plan.md
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   └── 05_report.md
│   ├── 20260315_resistant_dextrin/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   └── 05_report.md
│   ├── 20260320_fasting_health_effects/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   ├── 05_report_part1.md
│   │   ├── 05_report_part2.md
│   │   ├── report_sec1.md
│   │   ├── report_sec3.md
│   │   ├── report_sec4.md
│   │   ├── report_sec5a.md
│   │   ├── report_sec5b.md
│   │   ├── report_sec5c.md
│   │   ├── report_sec5d.md
│   │   ├── report_sec6.md
│   │   ├── report_sec7.md
│   │   └── report_sec8.md
│   ├── 20260322_recovery_wear_health_effects/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   ├── 05_report_part1.md
│   │   ├── 05_report_part2.md
│   │   ├── part2_sec10.md
│   │   ├── part2_sec6.md
│   │   ├── part2_sec7.md
│   │   ├── part2_sec8.md
│   │   └── part2_sec9.md
│   ├── 20260323_anemia_types_treatment/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   └── 05_report.md
│   ├── 20260401_235409_diabetes_drugs_healthy_nondiabetic/
│   │   ├── 01_search_plan.md
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   ├── 05_report.md
│   │   └── session_meta.json
│   ├── 20260402_231819_infant_gut_microbiome/
│   │   ├── 01_search_plan.md
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   └── 05_report.md
│   ├── 20260403_hiit_20min_protocol/
│   │   └── 05_report.md
│   ├── 20260403_peanut_daily_intake/
│   │   ├── 02_raw_papers.json
│   │   └── 05_report.md
│   ├── pediatric_constipation_dietary/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   └── 05_report.md
│   ├── test_run/
│   │   ├── 01_search_plan.md
│   │   ├── 02_raw_papers.json
│   │   ├── 03_screening.md
│   │   ├── 04_synthesis.md
│   │   └── 05_report.md
│   └── .gitkeep
├── prompts/
│   └── .gitkeep
├── reports/
│   ├── 2026-02-28_happiness-wellbeing-habits.md
│   ├── 2026-02-28_healthy-lifestyle-habits.md
│   ├── 2026-02-28_llm-hallucination-reduction.md
│   ├── 2026-02-28_vision-loss-dry-eye-prevention.md
│   ├── 2026-03-01_grip-strength-training.md
│   ├── 2026-03-02_eye-fatigue-vision-protection.md
│   ├── 2026-03-02_kettlebell-training-effects.md
│   ├── 2026-03-03_antiaging-longevity-interventions.md
│   ├── 2026-03-11_8exercises-comparison.md
│   ├── 2026-03-12_low-back-pain-prevention.md
│   ├── 2026-03-14_collagen-peptide-supplement.md
│   ├── 2026-03-15_creatine-supplement.md
│   ├── 2026-03-15_resistant-dextrin.md
│   ├── 2026-03-22_fasting-health-effects.md
│   ├── 2026-03-23_bath-co2-effects.md
│   ├── 2026-03-27_immunity-boost.md
│   ├── 2026-03-28_visceral-fat-reduction.md
│   ├── 2026-03-30_pediatric-constipation-fiber.md
│   ├── 2026-03-31_neck-pain-stretching-exercise.md
│   ├── 2026-04-01_scalp-care-hair-maintenance.md
│   ├── 2026-04-02_diabetes-drugs-nondiabetic.md
│   ├── 2026-04-03_infant-gut-microbiome.md
│   ├── 2026-04-06_四時間労働の効果_幸福度・認知・健康・文化.md
│   ├── 2026-04-13_hayfever-supplements-vs-drugs.md
│   ├── 2026-04-21_gastric-cancer-prevention-scoring.md
│   ├── 2026-04-28_immunity-boost-v2.md
│   ├── 2026-04-28_supplement-drug-risk-analysis.md
│   ├── 2026-04-30_cold-remedy-evidence.md
│   ├── 2026-04-30_genai-instruction-design.md
│   └── INDEX.md
├── src/
│   ├── apis/
│   │   ├── __init__.py
│   │   ├── .gitkeep
│   │   ├── arxiv_client.py
│   │   ├── openalex_client.py
│   │   └── semantic_scholar.py
│   ├── collectors/
│   │   ├── __init__.py
│   │   ├── .gitkeep
│   │   └── paper_collector.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── .gitkeep
│   │   ├── deduplicator.py
│   │   └── session_manager.py
│   ├── __init__.py
│   ├── config.py
│   └── notion_client.py
├── templates/
│   └── report_template.md
├── .env.example
├── .gitignore
├── CLAUDE.md
├── collect_no_ss.py
├── FILE_INDEX.md
├── README.md
├── REPORT_INDEX.md
├── requirements.txt
├── tasks.md
└── Timeout_Prevention.md
```

---

## ファイル詳細

### Documentation (136件)

<details>
<summary>クリックして展開 (136件)</summary>

| ファイル | サイズ | 説明 |
|---|---|---|
| `.claude/rules/git-rules.md` | 1.7 KB | Claude Code 設定・スキル |
| `.claude/rules/model-selection.md` | 1.2 KB | Claude Code 設定・スキル |
| `.claude/rules/output-rules.md` | 1.8 KB | Claude Code 設定・スキル |
| `.claude/rules/timeout-prevention.md` | 12.7 KB | Claude Code 設定・スキル |
| `.claude/skills/research-quick/SKILL.md` | 1.1 KB | スキル定義ファイル |
| `.claude/skills/research/SKILL.md` | 8.1 KB | スキル定義ファイル |
| `.claude/skills/search-only/SKILL.md` | 433 B | スキル定義ファイル |
| `CLAUDE.md` | 4.6 KB | Claude Code プロジェクト設定・命名ルール |
| `FILE_INDEX.md` | 8.7 KB | （このファイル）全ファイルインデックス |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/01_search_plan.md` | 2.2 KB | リサーチ出力データ |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/03_screening.md` | 8.0 KB | リサーチ出力データ |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/04_synthesis.md` | 12.9 KB | リサーチ出力データ |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/05_report.md` | 17.5 KB | リサーチ出力データ |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/01_search_plan.md` | 1.4 KB | リサーチ出力データ |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/03_screening.md` | 8.9 KB | リサーチ出力データ |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/04_synthesis.md` | 20.0 KB | リサーチ出力データ |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/05_report.md` | 27.5 KB | リサーチ出力データ |
| `outputs/20260228_104021_research/01_search_plan.md` | 1.7 KB | リサーチ出力データ |
| `outputs/20260228_104021_research/03_screening.md` | 8.9 KB | リサーチ出力データ |
| `outputs/20260228_104021_research/04_synthesis.md` | 20.2 KB | リサーチ出力データ |
| `outputs/20260228_104021_research/05_report.md` | 28.5 KB | リサーチ出力データ |
| `outputs/20260301_222104_grip_strength_training_effecti/01_search_plan.md` | 1.8 KB | リサーチ出力データ |
| `outputs/20260301_222104_grip_strength_training_effecti/03_screening.md` | 8.4 KB | リサーチ出力データ |
| `outputs/20260301_222104_grip_strength_training_effecti/04_synthesis.md` | 17.5 KB | リサーチ出力データ |
| `outputs/20260301_222104_grip_strength_training_effecti/05_report.md` | 24.9 KB | リサーチ出力データ |
| `outputs/20260302_070418_kettlebell_training_effects_co/01_search_plan.md` | 2.5 KB | リサーチ出力データ |
| `outputs/20260302_070418_kettlebell_training_effects_co/03_screening.md` | 10.6 KB | リサーチ出力データ |
| `outputs/20260302_070418_kettlebell_training_effects_co/04_synthesis.md` | 17.2 KB | リサーチ出力データ |
| `outputs/20260302_070418_kettlebell_training_effects_co/05_report.md` | 23.4 KB | リサーチ出力データ |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/01_search_plan.md` | 2.8 KB | リサーチ出力データ |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/03_screening.md` | 3.8 KB | リサーチ出力データ |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/04_synthesis.md` | 4.9 KB | リサーチ出力データ |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/05_report.md` | 24.4 KB | リサーチ出力データ |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/01_search_plan.md` | 3.0 KB | リサーチ出力データ |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/03_screening.md` | 6.6 KB | リサーチ出力データ |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/04_synthesis.md` | 16.5 KB | リサーチ出力データ |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/05_report.md` | 31.3 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/05_report.md` | 34.0 KB | リサーチ出力データ |
| `outputs/20260312_lowbackpain_prevention/01_search_plan.md` | 1.4 KB | リサーチ出力データ |
| `outputs/20260312_lowbackpain_prevention/03_screening.md` | 3.4 KB | リサーチ出力データ |
| `outputs/20260312_lowbackpain_prevention/04_synthesis.md` | 4.9 KB | リサーチ出力データ |
| `outputs/20260312_lowbackpain_prevention/05_report.md` | 19.9 KB | リサーチ出力データ |
| `outputs/20260314_collagen_peptide_supplement/01_search_plan.md` | 2.7 KB | リサーチ出力データ |
| `outputs/20260314_collagen_peptide_supplement/03_screening.md` | 8.4 KB | リサーチ出力データ |
| `outputs/20260314_collagen_peptide_supplement/04_synthesis.md` | 12.8 KB | リサーチ出力データ |
| `outputs/20260314_collagen_peptide_supplement/05_report.md` | 17.9 KB | リサーチ出力データ |
| `outputs/20260315_creatine_supplement/01_search_plan.md` | 1.5 KB | リサーチ出力データ |
| `outputs/20260315_creatine_supplement/03_screening.md` | 5.6 KB | リサーチ出力データ |
| `outputs/20260315_creatine_supplement/04_synthesis.md` | 4.5 KB | リサーチ出力データ |
| `outputs/20260315_creatine_supplement/05_report.md` | 29.1 KB | リサーチ出力データ |
| `outputs/20260315_resistant_dextrin/01_search_plan.md` | 3.8 KB | リサーチ出力データ |
| `outputs/20260315_resistant_dextrin/03_screening.md` | 4.5 KB | リサーチ出力データ |
| `outputs/20260315_resistant_dextrin/04_synthesis.md` | 9.4 KB | リサーチ出力データ |
| `outputs/20260315_resistant_dextrin/05_report.md` | 29.0 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/01_search_plan.md` | 2.3 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/03_screening.md` | 6.9 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/04_synthesis.md` | 14.7 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/05_report_part1.md` | 21.3 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/05_report_part2.md` | 12.4 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/report_sec1.md` | 4.2 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/report_sec3.md` | 2.8 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/report_sec4.md` | 4.3 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/report_sec5a.md` | 2.3 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/report_sec5b.md` | 2.4 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/report_sec5c.md` | 2.5 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/report_sec5d.md` | 2.7 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/report_sec6.md` | 3.0 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/report_sec7.md` | 3.0 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/report_sec8.md` | 6.4 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/01_search_plan.md` | 2.6 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/03_screening.md` | 4.8 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/04_synthesis.md` | 15.2 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/05_report_part1.md` | 17.7 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/05_report_part2.md` | 16.5 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/part2_sec10.md` | 5.3 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/part2_sec6.md` | 3.8 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/part2_sec7.md` | 2.4 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/part2_sec8.md` | 2.6 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/part2_sec9.md` | 2.4 KB | リサーチ出力データ |
| `outputs/20260323_anemia_types_treatment/01_search_plan.md` | 1.9 KB | リサーチ出力データ |
| `outputs/20260323_anemia_types_treatment/03_screening.md` | 5.8 KB | リサーチ出力データ |
| `outputs/20260323_anemia_types_treatment/04_synthesis.md` | 5.2 KB | リサーチ出力データ |
| `outputs/20260323_anemia_types_treatment/05_report.md` | 16.5 KB | リサーチ出力データ |
| `outputs/20260401_235409_diabetes_drugs_healthy_nondiabetic/01_search_plan.md` | 3.5 KB | リサーチ出力データ |
| `outputs/20260401_235409_diabetes_drugs_healthy_nondiabetic/03_screening.md` | 10.1 KB | リサーチ出力データ |
| `outputs/20260401_235409_diabetes_drugs_healthy_nondiabetic/04_synthesis.md` | 13.3 KB | リサーチ出力データ |
| `outputs/20260401_235409_diabetes_drugs_healthy_nondiabetic/05_report.md` | 24.2 KB | リサーチ出力データ |
| `outputs/20260402_231819_infant_gut_microbiome/01_search_plan.md` | 2.5 KB | リサーチ出力データ |
| `outputs/20260402_231819_infant_gut_microbiome/03_screening.md` | 7.8 KB | リサーチ出力データ |
| `outputs/20260402_231819_infant_gut_microbiome/04_synthesis.md` | 9.8 KB | リサーチ出力データ |
| `outputs/20260402_231819_infant_gut_microbiome/05_report.md` | 22.0 KB | リサーチ出力データ |
| `outputs/20260403_hiit_20min_protocol/05_report.md` | 20.6 KB | リサーチ出力データ |
| `outputs/20260403_peanut_daily_intake/05_report.md` | 15.2 KB | リサーチ出力データ |
| `outputs/pediatric_constipation_dietary/01_search_plan.md` | 1.7 KB | リサーチ出力データ |
| `outputs/pediatric_constipation_dietary/03_screening.md` | 4.8 KB | リサーチ出力データ |
| `outputs/pediatric_constipation_dietary/04_synthesis.md` | 11.2 KB | リサーチ出力データ |
| `outputs/pediatric_constipation_dietary/05_report.md` | 43.8 KB | リサーチ出力データ |
| `outputs/test_run/01_search_plan.md` | 1.5 KB | リサーチ出力データ |
| `outputs/test_run/03_screening.md` | 7.8 KB | リサーチ出力データ |
| `outputs/test_run/04_synthesis.md` | 10.5 KB | リサーチ出力データ |
| `outputs/test_run/05_report.md` | 16.4 KB | リサーチ出力データ |
| `README.md` | 4.4 KB | リポジトリ概要・セットアップ手順 |
| `REPORT_INDEX.md` | 7.8 KB | リサーチレポート一覧インデックス |
| `reports/2026-02-28_happiness-wellbeing-habits.md` | 28.5 KB | Markdown ドキュメント |
| `reports/2026-02-28_healthy-lifestyle-habits.md` | 27.5 KB | Markdown ドキュメント |
| `reports/2026-02-28_llm-hallucination-reduction.md` | 16.4 KB | Markdown ドキュメント |
| `reports/2026-02-28_vision-loss-dry-eye-prevention.md` | 17.5 KB | Markdown ドキュメント |
| `reports/2026-03-01_grip-strength-training.md` | 24.9 KB | Markdown ドキュメント |
| `reports/2026-03-02_eye-fatigue-vision-protection.md` | 24.4 KB | Markdown ドキュメント |
| `reports/2026-03-02_kettlebell-training-effects.md` | 23.4 KB | Markdown ドキュメント |
| `reports/2026-03-03_antiaging-longevity-interventions.md` | 31.3 KB | Markdown ドキュメント |
| `reports/2026-03-11_8exercises-comparison.md` | 34.0 KB | Markdown ドキュメント |
| `reports/2026-03-12_low-back-pain-prevention.md` | 19.9 KB | Markdown ドキュメント |
| `reports/2026-03-14_collagen-peptide-supplement.md` | 17.9 KB | Markdown ドキュメント |
| `reports/2026-03-15_creatine-supplement.md` | 29.1 KB | Markdown ドキュメント |
| `reports/2026-03-15_resistant-dextrin.md` | 29.0 KB | Markdown ドキュメント |
| `reports/2026-03-22_fasting-health-effects.md` | 33.7 KB | Markdown ドキュメント |
| `reports/2026-03-23_bath-co2-effects.md` | 26.8 KB | Markdown ドキュメント |
| `reports/2026-03-27_immunity-boost.md` | 28.0 KB | Markdown ドキュメント |
| `reports/2026-03-28_visceral-fat-reduction.md` | 43.7 KB | Markdown ドキュメント |
| `reports/2026-03-30_pediatric-constipation-fiber.md` | 33.3 KB | Markdown ドキュメント |
| `reports/2026-03-31_neck-pain-stretching-exercise.md` | 25.6 KB | Markdown ドキュメント |
| `reports/2026-04-01_scalp-care-hair-maintenance.md` | 32.1 KB | Markdown ドキュメント |
| `reports/2026-04-02_diabetes-drugs-nondiabetic.md` | 24.2 KB | Markdown ドキュメント |
| `reports/2026-04-03_infant-gut-microbiome.md` | 22.0 KB | Markdown ドキュメント |
| `reports/2026-04-06_四時間労働の効果_幸福度・認知・健康・文化.md` | 43.0 KB | Markdown ドキュメント |
| `reports/2026-04-13_hayfever-supplements-vs-drugs.md` | 39.1 KB | Markdown ドキュメント |
| `reports/2026-04-21_gastric-cancer-prevention-scoring.md` | 32.9 KB | Markdown ドキュメント |
| `reports/2026-04-28_immunity-boost-v2.md` | 39.3 KB | Markdown ドキュメント |
| `reports/2026-04-28_supplement-drug-risk-analysis.md` | 15.0 KB | Markdown ドキュメント |
| `reports/2026-04-30_cold-remedy-evidence.md` | 48.2 KB | Markdown ドキュメント |
| `reports/2026-04-30_genai-instruction-design.md` | 29.8 KB | Markdown ドキュメント |
| `reports/INDEX.md` | 43.1 KB | Markdown ドキュメント |
| `tasks.md` | 3.3 KB | タスク管理・セッション履歴 |
| `templates/report_template.md` | 1.5 KB | Markdown ドキュメント |
| `Timeout_Prevention.md` | 9.9 KB | タイムアウト対策ガイド |

</details>

### Code (13件)

| ファイル | サイズ | 説明 |
|---|---|---|
| `collect_no_ss.py` | 2.2 KB | Python スクリプト |
| `src/__init__.py` | - | Python スクリプト |
| `src/apis/__init__.py` | 190 B | Python スクリプト |
| `src/apis/arxiv_client.py` | 7.5 KB | Python スクリプト |
| `src/apis/openalex_client.py` | 6.1 KB | Python スクリプト |
| `src/apis/semantic_scholar.py` | 6.3 KB | Python スクリプト |
| `src/collectors/__init__.py` | 156 B | Python スクリプト |
| `src/collectors/paper_collector.py` | 9.0 KB | Python スクリプト |
| `src/config.py` | 3.6 KB | Python スクリプト |
| `src/notion_client.py` | 14.7 KB | Python スクリプト |
| `src/utils/__init__.py` | 262 B | Python スクリプト |
| `src/utils/deduplicator.py` | 3.2 KB | Python スクリプト |
| `src/utils/session_manager.py` | 4.2 KB | Python スクリプト |

### Data (34件)

| ファイル | サイズ | 説明 |
|---|---|---|
| `.claude/settings.json` | 212 B | JSON データ |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/02_raw_papers.json` | 359.3 KB | リサーチ出力データ |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/session_meta.json` | 275 B | リサーチ出力データ |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/02_raw_papers.json` | 531.5 KB | リサーチ出力データ |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/session_meta.json` | 268 B | リサーチ出力データ |
| `outputs/20260228_104021_research/02_raw_papers.json` | 322.9 KB | リサーチ出力データ |
| `outputs/20260228_104021_research/session_meta.json` | 226 B | リサーチ出力データ |
| `outputs/20260301_222104_grip_strength_training_effecti/02_raw_papers.json` | 403.2 KB | リサーチ出力データ |
| `outputs/20260301_222104_grip_strength_training_effecti/session_meta.json` | 277 B | リサーチ出力データ |
| `outputs/20260302_070418_kettlebell_training_effects_co/02_raw_papers.json` | 478.6 KB | リサーチ出力データ |
| `outputs/20260302_070418_kettlebell_training_effects_co/session_meta.json` | 275 B | リサーチ出力データ |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/02_raw_papers.json` | 371.4 KB | リサーチ出力データ |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/session_meta.json` | 289 B | リサーチ出力データ |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/02_raw_papers.json` | 415.8 KB | リサーチ出力データ |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/session_meta.json` | 283 B | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/02_bouldering.json` | 343.3 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/02_burpee.json` | 356.0 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/02_dumbbell.json` | 271.8 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/02_handstand.json` | 335.3 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/02_hiit_safety.json` | 197.7 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/02_hiit.json` | 166.6 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/02_kettlebell.json` | 260.0 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/02_pullup.json` | 209.0 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/02_pullup2.json` | 491.2 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/02_swimming.json` | 493.1 KB | リサーチ出力データ |
| `outputs/20260311_081644_7exercisescomparison/session_meta.json` | 236 B | リサーチ出力データ |
| `outputs/20260315_resistant_dextrin/02_raw_papers.json` | 700.9 KB | リサーチ出力データ |
| `outputs/20260320_fasting_health_effects/02_raw_papers.json` | 755.6 KB | リサーチ出力データ |
| `outputs/20260322_recovery_wear_health_effects/02_raw_papers.json` | 819.2 KB | リサーチ出力データ |
| `outputs/20260323_anemia_types_treatment/02_raw_papers.json` | 559.7 KB | リサーチ出力データ |
| `outputs/20260401_235409_diabetes_drugs_healthy_nondiabetic/session_meta.json` | 518 B | リサーチ出力データ |
| `outputs/20260403_peanut_daily_intake/02_raw_papers.json` | 234.0 KB | リサーチ出力データ |
| `outputs/pediatric_constipation_dietary/02_raw_papers.json` | 277.6 KB | リサーチ出力データ |
| `outputs/test_run/02_raw_papers.json` | 402.6 KB | リサーチ出力データ |

### Config (3件)

| ファイル | サイズ | 説明 |
|---|---|---|
| `.env.example` | 255 B | 環境変数テンプレート |
| `.gitignore` | 33 B | Git 除外設定 |
| `requirements.txt` | 53 B | Python 依存パッケージリスト |

### Other (5件)

| ファイル | サイズ | 説明 |
|---|---|---|
| `outputs/.gitkeep` | - | ファイル |
| `prompts/.gitkeep` | - | ファイル |
| `src/apis/.gitkeep` | - | ファイル |
| `src/collectors/.gitkeep` | - | ファイル |
| `src/utils/.gitkeep` | - | ファイル |

---

_自動生成: 2026-05-02 | 管理者: 男座員也（Kazuya Oza）_
