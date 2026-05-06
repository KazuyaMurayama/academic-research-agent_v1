# FILE INDEX - academic-research-agent_v1

> 最終更新: 2026-05-06 | ファイル数: 192

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
├── REPORT_INDEX.md
├── Timeout_Prevention.md
├── collect_no_ss.py
├── outputs/
│   ├── .gitkeep
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
│   │   ├── 02_hiit.json
│   │   ├── 02_hiit_safety.json
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
│   └── test_run/
│       ├── 01_search_plan.md
│       ├── 02_raw_papers.json
│       ├── 03_screening.md
│       ├── 04_synthesis.md
│       └── 05_report.md
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
│   ├── 2026-05-05_soy-intake-health-effects-men.md
│   └── INDEX.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── apis/
│   │   ├── .gitkeep
│   │   ├── __init__.py
│   │   ├── arxiv_client.py
│   │   ├── openalex_client.py
│   │   └── semantic_scholar.py
│   ├── collectors/
│   │   ├── .gitkeep
│   │   ├── __init__.py
│   │   └── paper_collector.py
│   ├── config.py
│   ├── notion_client.py
│   └── utils/
│       ├── .gitkeep
│       ├── __init__.py
│       ├── deduplicator.py
│       └── session_manager.py
├── tasks.md
└── templates/
    └── report_template.md
```

## カテゴリ別ファイル一覧

### Documentation (138件)

<details><summary>138件（クリックして展開）</summary>

| ファイルパス | サイズ(bytes) | SHA |
|---|---|---|
| `.claude/rules/git-rules.md` | 1767 | 43fa9f7 |
| `.claude/rules/model-selection.md` | 1218 | 4a981e4 |
| `.claude/rules/output-rules.md` | 1819 | 991cd39 |
| `.claude/rules/timeout-prevention.md` | 12971 | 17f4938 |
| `.claude/skills/research-quick/SKILL.md` | 1109 | 50cc35d |
| `.claude/skills/research/SKILL.md` | 8279 | e256698 |
| `.claude/skills/search-only/SKILL.md` | 433 | da13274 |
| `CLAUDE.md` | 4695 | b73c6fd |
| `FILE_INDEX.md` | 28693 | 7a21a04 |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/01_search_plan.md` | 2248 | a099016 |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/03_screening.md` | 8144 | 3a9f6ea |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/04_synthesis.md` | 13232 | 9dfa415 |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/05_report.md` | 17933 | f0d9131 |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/01_search_plan.md` | 1416 | 0d70312 |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/03_screening.md` | 9109 | 9d74036 |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/04_synthesis.md` | 20467 | 6addb37 |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/05_report.md` | 28202 | b8f86c0 |
| `outputs/20260228_104021_research/01_search_plan.md` | 1755 | 9f4243c |
| `outputs/20260228_104021_research/03_screening.md` | 9146 | 7e7e90d |
| `outputs/20260228_104021_research/04_synthesis.md` | 20716 | 8a78a96 |
| `outputs/20260228_104021_research/05_report.md` | 29211 | 3af37f4 |
| `outputs/20260301_222104_grip_strength_training_effecti/01_search_plan.md` | 1841 | 3008915 |
| `outputs/20260301_222104_grip_strength_training_effecti/03_screening.md` | 8554 | fd7ffb5 |
| `outputs/20260301_222104_grip_strength_training_effecti/04_synthesis.md` | 17951 | fd953da |
| `outputs/20260301_222104_grip_strength_training_effecti/05_report.md` | 25521 | bc78f1b |
| `outputs/20260302_070418_kettlebell_training_effects_co/01_search_plan.md` | 2563 | b7d88b4 |
| `outputs/20260302_070418_kettlebell_training_effects_co/03_screening.md` | 10822 | 48b5da7 |
| `outputs/20260302_070418_kettlebell_training_effects_co/04_synthesis.md` | 17616 | f1ef637 |
| `outputs/20260302_070418_kettlebell_training_effects_co/05_report.md` | 24010 | 96409d5 |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/01_search_plan.md` | 2846 | 694d830 |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/03_screening.md` | 3849 | 2b74d95 |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/04_synthesis.md` | 5011 | 094bd89 |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/05_report.md` | 25021 | 82ecac9 |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/01_search_plan.md` | 3065 | 9965a33 |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/03_screening.md` | 6782 | 46a839c |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/04_synthesis.md` | 16902 | 43cede4 |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/05_report.md` | 32039 | e2c9cea |
| `outputs/20260311_081644_7exercisescomparison/05_report.md` | 34864 | 2aef6b9 |
| `outputs/20260312_lowbackpain_prevention/01_search_plan.md` | 1429 | de7cc23 |
| `outputs/20260312_lowbackpain_prevention/03_screening.md` | 3483 | b634d50 |
| `outputs/20260312_lowbackpain_prevention/04_synthesis.md` | 4985 | 86cb359 |
| `outputs/20260312_lowbackpain_prevention/05_report.md` | 20390 | be3cb65 |
| `outputs/20260314_collagen_peptide_supplement/01_search_plan.md` | 2765 | 619db44 |
| `outputs/20260314_collagen_peptide_supplement/03_screening.md` | 8582 | c17b176 |
| `outputs/20260314_collagen_peptide_supplement/04_synthesis.md` | 13115 | 74ca374 |
| `outputs/20260314_collagen_peptide_supplement/05_report.md` | 18346 | 4a75d5c |
| `outputs/20260315_creatine_supplement/01_search_plan.md` | 1514 | ba99946 |
| `outputs/20260315_creatine_supplement/03_screening.md` | 5735 | 483a2d5 |
| `outputs/20260315_creatine_supplement/04_synthesis.md` | 4636 | 3500699 |
| `outputs/20260315_creatine_supplement/05_report.md` | 29784 | a512289 |
| `outputs/20260315_resistant_dextrin/01_search_plan.md` | 3902 | 5634433 |
| `outputs/20260315_resistant_dextrin/03_screening.md` | 4564 | 976e410 |
| `outputs/20260315_resistant_dextrin/04_synthesis.md` | 9598 | 40b6c15 |
| `outputs/20260315_resistant_dextrin/05_report.md` | 29694 | 10f2be7 |
| `outputs/20260320_fasting_health_effects/01_search_plan.md` | 2392 | f4c0130 |
| `outputs/20260320_fasting_health_effects/03_screening.md` | 7107 | 0160f49 |
| `outputs/20260320_fasting_health_effects/04_synthesis.md` | 15098 | 4a3d68b |
| `outputs/20260320_fasting_health_effects/05_report_part1.md` | 21807 | 72d06d5 |
| `outputs/20260320_fasting_health_effects/05_report_part2.md` | 12688 | 003f6cc |
| `outputs/20260320_fasting_health_effects/report_sec1.md` | 4267 | 30acae4 |
| `outputs/20260320_fasting_health_effects/report_sec3.md` | 2884 | 87834f6 |
| `outputs/20260320_fasting_health_effects/report_sec4.md` | 4423 | b881b57 |
| `outputs/20260320_fasting_health_effects/report_sec5a.md` | 2397 | 929f35c |
| `outputs/20260320_fasting_health_effects/report_sec5b.md` | 2453 | 405c6e0 |
| `outputs/20260320_fasting_health_effects/report_sec5c.md` | 2586 | e5982d1 |
| `outputs/20260320_fasting_health_effects/report_sec5d.md` | 2797 | 1e2f20c |
| `outputs/20260320_fasting_health_effects/report_sec6.md` | 3075 | 347e675 |
| `outputs/20260320_fasting_health_effects/report_sec7.md` | 3081 | 1707c5e |
| `outputs/20260320_fasting_health_effects/report_sec8.md` | 6532 | f4486ec |
| `outputs/20260322_recovery_wear_health_effects/01_search_plan.md` | 2706 | 0c0ee93 |
| `outputs/20260322_recovery_wear_health_effects/03_screening.md` | 4920 | 9e74289 |
| `outputs/20260322_recovery_wear_health_effects/04_synthesis.md` | 15549 | cbebb3e |
| `outputs/20260322_recovery_wear_health_effects/05_report_part1.md` | 18143 | 4c4df7f |
| `outputs/20260322_recovery_wear_health_effects/05_report_part2.md` | 16878 | 3823c9a |
| `outputs/20260322_recovery_wear_health_effects/part2_sec10.md` | 5426 | 2c2f1bb |
| `outputs/20260322_recovery_wear_health_effects/part2_sec6.md` | 3880 | 5959d30 |
| `outputs/20260322_recovery_wear_health_effects/part2_sec7.md` | 2470 | 1b992d9 |
| `outputs/20260322_recovery_wear_health_effects/part2_sec8.md` | 2693 | 48fd092 |
| `outputs/20260322_recovery_wear_health_effects/part2_sec9.md` | 2409 | f19e813 |
| `outputs/20260323_anemia_types_treatment/01_search_plan.md` | 1946 | 7391e99 |
| `outputs/20260323_anemia_types_treatment/03_screening.md` | 5958 | 6088a15 |
| `outputs/20260323_anemia_types_treatment/04_synthesis.md` | 5323 | 4ae6900 |
| `outputs/20260323_anemia_types_treatment/05_report.md` | 16944 | b207ed0 |
| `outputs/20260401_235409_diabetes_drugs_healthy_nondiabetic/01_search_plan.md` | 3549 | 947050d |
| `outputs/20260401_235409_diabetes_drugs_healthy_nondiabetic/03_screening.md` | 10363 | 10b0e6b |
| `outputs/20260401_235409_diabetes_drugs_healthy_nondiabetic/04_synthesis.md` | 13580 | 528518f |
| `outputs/20260401_235409_diabetes_drugs_healthy_nondiabetic/05_report.md` | 24808 | d869ffe |
| `outputs/20260402_231819_infant_gut_microbiome/01_search_plan.md` | 2540 | b02c41e |
| `outputs/20260402_231819_infant_gut_microbiome/03_screening.md` | 7952 | b50c5eb |
| `outputs/20260402_231819_infant_gut_microbiome/04_synthesis.md` | 10020 | 13a0a18 |
| `outputs/20260402_231819_infant_gut_microbiome/05_report.md` | 22503 | 5db0d38 |
| `outputs/20260403_hiit_20min_protocol/05_report.md` | 21115 | 63f1b38 |
| `outputs/20260403_peanut_daily_intake/05_report.md` | 15562 | 5939b9c |
| `outputs/pediatric_constipation_dietary/01_search_plan.md` | 1784 | 3a2e5cc |
| `outputs/pediatric_constipation_dietary/03_screening.md` | 4930 | 0ea3921 |
| `outputs/pediatric_constipation_dietary/04_synthesis.md` | 11492 | 04233fd |
| `outputs/pediatric_constipation_dietary/05_report.md` | 44835 | ad84b27 |
| `outputs/test_run/01_search_plan.md` | 1571 | 21722cb |
| `outputs/test_run/03_screening.md` | 7981 | c8eb99e |
| `outputs/test_run/04_synthesis.md` | 10758 | 1389c9c |
| `outputs/test_run/05_report.md` | 16768 | 854ff8c |
| `README.md` | 4474 | c00cb24 |
| `REPORT_INDEX.md` | 7947 | 418c571 |
| `reports/2026-02-28_happiness-wellbeing-habits.md` | 29211 | 3af37f4 |
| `reports/2026-02-28_healthy-lifestyle-habits.md` | 28202 | b8f86c0 |
| `reports/2026-02-28_llm-hallucination-reduction.md` | 16768 | 854ff8c |
| `reports/2026-02-28_vision-loss-dry-eye-prevention.md` | 17933 | f0d9131 |
| `reports/2026-03-01_grip-strength-training.md` | 25521 | bc78f1b |
| `reports/2026-03-02_eye-fatigue-vision-protection.md` | 25021 | 82ecac9 |
| `reports/2026-03-02_kettlebell-training-effects.md` | 24010 | 96409d5 |
| `reports/2026-03-03_antiaging-longevity-interventions.md` | 32039 | e2c9cea |
| `reports/2026-03-11_8exercises-comparison.md` | 34864 | 2aef6b9 |
| `reports/2026-03-12_low-back-pain-prevention.md` | 20390 | be3cb65 |
| `reports/2026-03-14_collagen-peptide-supplement.md` | 18346 | 4a75d5c |
| `reports/2026-03-15_creatine-supplement.md` | 29784 | a512289 |
| `reports/2026-03-15_resistant-dextrin.md` | 29694 | 10f2be7 |
| `reports/2026-03-22_fasting-health-effects.md` | 34496 | a8354f8 |
| `reports/2026-03-23_bath-co2-effects.md` | 27447 | c43213d |
| `reports/2026-03-27_immunity-boost.md` | 28712 | 8931f6f |
| `reports/2026-03-28_visceral-fat-reduction.md` | 44745 | 8a5521f |
| `reports/2026-03-30_pediatric-constipation-fiber.md` | 34106 | 8e447e9 |
| `reports/2026-03-31_neck-pain-stretching-exercise.md` | 26189 | 462449e |
| `reports/2026-04-01_scalp-care-hair-maintenance.md` | 32827 | 51be284 |
| `reports/2026-04-02_diabetes-drugs-nondiabetic.md` | 24808 | d869ffe |
| `reports/2026-04-03_infant-gut-microbiome.md` | 22503 | 5db0d38 |
| `reports/2026-04-06_四時間労働の効果_幸福度・認知・健康・文化.md` | 43993 | fd9e91e |
| `reports/2026-04-13_hayfever-supplements-vs-drugs.md` | 40013 | a603d06 |
| `reports/2026-04-21_gastric-cancer-prevention-scoring.md` | 33697 | a1405d9 |
| `reports/2026-04-28_immunity-boost-v2.md` | 40278 | 67c21cc |
| `reports/2026-04-28_supplement-drug-risk-analysis.md` | 15318 | 76c04f4 |
| `reports/2026-04-30_cold-remedy-evidence.md` | 49306 | ddf21be |
| `reports/2026-04-30_genai-instruction-design.md` | 30493 | dc77e2f |
| `reports/2026-05-05_soy-intake-health-effects-men.md` | 19961 | 9c81ff3 |
| `reports/INDEX.md` | 44169 | 2644b3b |
| `requirements.txt` | 53 | b89f5a6 |
| `tasks.md` | 3371 | 0fcd446 |
| `templates/report_template.md` | 1567 | fc3476b |
| `Timeout_Prevention.md` | 10163 | a281ff4 |

</details>

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

### Data (34件)

| ファイルパス | サイズ(bytes) | SHA |
|---|---|---|
| `.claude/settings.json` | 212 | b8ff2ae |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/02_raw_papers.json` | 367914 | 00eefa1 |
| `outputs/20260228_100714_vision_loss_prevention_dry_eye/session_meta.json` | 275 | f35cd68 |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/02_raw_papers.json` | 544214 | 40432d0 |
| `outputs/20260228_102329_healthy_lifestyle_habits_longe/session_meta.json` | 268 | 4144eb6 |
| `outputs/20260228_104021_research/02_raw_papers.json` | 330675 | ebf93fc |
| `outputs/20260228_104021_research/session_meta.json` | 226 | 42a750e |
| `outputs/20260301_222104_grip_strength_training_effecti/02_raw_papers.json` | 412882 | 5e8b0b2 |
| `outputs/20260301_222104_grip_strength_training_effecti/session_meta.json` | 277 | dd6cc93 |
| `outputs/20260302_070418_kettlebell_training_effects_co/02_raw_papers.json` | 490088 | bfe829c |
| `outputs/20260302_070418_kettlebell_training_effects_co/session_meta.json` | 275 | ffc40fb |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/02_raw_papers.json` | 380265 | 3f46c21 |
| `outputs/20260302_105343_eye_fatigue_vision_loss_preven/session_meta.json` | 289 | b7af3cd |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/02_raw_papers.json` | 425804 | 87aa227 |
| `outputs/20260303_005155_antiaging_longevity_evidenceba/session_meta.json` | 283 | 5232285 |
| `outputs/20260311_081644_7exercisescomparison/02_bouldering.json` | 351521 | e694bc2 |
| `outputs/20260311_081644_7exercisescomparison/02_burpee.json` | 364498 | bfe7b77 |
| `outputs/20260311_081644_7exercisescomparison/02_dumbbell.json` | 278296 | 1a9659e |
| `outputs/20260311_081644_7exercisescomparison/02_handstand.json` | 343358 | faea9e9 |
| `outputs/20260311_081644_7exercisescomparison/02_hiit_safety.json` | 202469 | cbb867e |
| `outputs/20260311_081644_7exercisescomparison/02_hiit.json` | 170568 | f1307f3 |
| `outputs/20260311_081644_7exercisescomparison/02_kettlebell.json` | 266220 | 5d0f2b9 |
| `outputs/20260311_081644_7exercisescomparison/02_pullup.json` | 214067 | ee571ea |
| `outputs/20260311_081644_7exercisescomparison/02_pullup2.json` | 502989 | 1955c6a |
| `outputs/20260311_081644_7exercisescomparison/02_swimming.json` | 504936 | c428fe0 |
| `outputs/20260311_081644_7exercisescomparison/session_meta.json` | 236 | b7b08dd |
| `outputs/20260315_resistant_dextrin/02_raw_papers.json` | 717676 | dc57cfd |
| `outputs/20260320_fasting_health_effects/02_raw_papers.json` | 773731 | 8aa4af4 |
| `outputs/20260322_recovery_wear_health_effects/02_raw_papers.json` | 838903 | aa577bf |
| `outputs/20260323_anemia_types_treatment/02_raw_papers.json` | 573130 | 62ada62 |
| `outputs/20260401_235409_diabetes_drugs_healthy_nondiabetic/session_meta.json` | 518 | b32fec0 |
| `outputs/20260403_peanut_daily_intake/02_raw_papers.json` | 239605 | 18eea84 |
| `outputs/pediatric_constipation_dietary/02_raw_papers.json` | 284252 | 7567ba6 |
| `outputs/test_run/02_raw_papers.json` | 412272 | 4e52a77 |

### Config (1件)

| ファイルパス | サイズ(bytes) | SHA |
|---|---|---|
| `.gitignore` | 33 | 4f2b39b |

### Other (6件)

| ファイルパス | サイズ(bytes) | SHA |
|---|---|---|
| `.env.example` | 255 | d8e32a2 |
| `outputs/.gitkeep` | 0 | e69de29 |
| `prompts/.gitkeep` | 0 | e69de29 |
| `src/apis/.gitkeep` | 0 | e69de29 |
| `src/collectors/.gitkeep` | 0 | e69de29 |
| `src/utils/.gitkeep` | 0 | e69de29 |

