# Phase 3: スクリーニング結果

**セッション**: 20260401_235409_diabetes_drugs_healthy_nondiabetic  
**スクリーニング日**: 2026-04-02  
**総候補数**: 1,549件 → Tier 1: 20本 / Tier 2: 20本

---

## PRISMAフロー

```
検索ヒット（Semantic Scholar + OpenAlex + arXiv）: ~2,200件（バッチ1+2合算）
    ↓ 重複排除
ユニーク論文: 1,549件
    ↓ キーワードスコアリング（閾値スコア>12）
スコア通過: 532件
    ↓ タイトル・アブストラクト精査（研究デザイン・対象集団・関連性）
    ↓ 除外: 492件
        ├ 2型糖尿病患者のみ（体組成/老化データなし）: ~200件
        ├ ガイドライン・疾患管理の一般論: ~100件
        ├ 動物実験のみ（薬理機序参照に限定）: ~50件
        ├ 症例報告・N<50: ~80件
        └ その他（COVID-19、消化器疾患、心不全のみ）: ~62件
    ↓
Tier 1（コア論文）: 20本
Tier 2（補助論文）: 20本
```

---

## Tier 1: コア論文（詳細分析対象）

### カテゴリA: GLP-1受容体作動薬 — 非糖尿病者の体重・体組成・内臓脂肪

| # | 著者(年) | タイトル | デザイン | N | 選定理由 |
|---|---------|---------|---------|---|---------|
| T1-1 | Rubino et al. (2022) | Effect of Weekly Subcutaneous Semaglutide vs Daily Liraglutide on Body Weight in Adults With Overweight or Obesity Without Diabetes | RCT | 338 | JAMA掲載、非糖尿病者へのsemaglutide vs liraglutide直接比較、被引用815 |
| T1-2 | Liu et al. (2023) | The Weight-loss Effect of GLP-1RAs in Non-diabetic Individuals with Overweight or Obesity: A Systematic Review with Meta-Analysis | SR+MA | ~2,500 | 非糖尿病者限定の最も包括的MA、体重・体脂肪効果量を定量化 |
| T1-3 | Guo et al. (2022) | The Antiobesity Effect and Safety of GLP-1 Receptor Agonist in Overweight/Obese Patients without Diabetes | SR+MA | ~1,800 | 非糖尿病者の安全性・有効性を包括評価 |
| T1-4 | Silver et al. (2023) | Effect of liraglutide vs caloric restriction on body fat distribution and cardiometabolic biomarkers: RCT in adults with obesity and prediabetes | RCT | 60 | 体脂肪分布（内臓vs皮下）を直接比較、前糖尿病者 |
| T1-5 | Rochira et al. (2024) | The Effect of Tirzepatide on Body Composition in People with Overweight and Obesity | SR | ~3,500 | チルゼパチドの体組成（除脂肪体重vs脂肪量）SR |
| T1-6 | Moiz et al. (2025) | Efficacy and Safety of GLP-1 Receptor Agonists for Weight Loss Among Adults Without Diabetes | MA | ~12,000 | 非糖尿病者限定の最新大規模MA（2025年）、RCT統合 |

### カテゴリB: GLP-1受容体作動薬 — 非糖尿病者の心血管アウトカム

| # | 著者(年) | タイトル | デザイン | N | 選定理由 |
|---|---------|---------|---------|---|---------|
| T1-7 | Deanfield et al. (2024) | Semaglutide and cardiovascular outcomes in patients with obesity and prevalent heart failure: SELECT trial prespecified analysis | RCT (prespecified) | 17,604 | SELECT試験（非糖尿病）のLancet発表、MACE低下20%、最重要エビデンス |
| T1-8 | Stefanou et al. (2024) | Risk of MACE and all-cause mortality under GLP-1 RAs/tirzepatide in non-diabetic overweight/obese adults | SR+MA | ~25,000 | 非糖尿病限定MACE MA、tirzepatide含む最新統合 |
| T1-9 | Tom-Ayegunle et al. (2026) | Long-Term Cardiovascular Outcomes of GLP-1 Receptor Agonists in Non-diabetic Obesity: A SR and MA | SR+MA | ~30,000 | 2026年最新MA、非糖尿病者の長期CV転帰 |
| T1-10 | Abdeen et al. (2025) | Cardiovascular Effects of GLP-1 Receptor Agonists in Non-Diabetic Adults With Obesity: A Systematic Literature Review | SLR | — | 非糖尿病者限定のCV効果系統的文献レビュー |

### カテゴリC: GLP-1受容体作動薬 — 癌リスク

| # | 著者(年) | タイトル | デザイン | N | 選定理由 |
|---|---------|---------|---------|---|---------|
| T1-11 | Wang et al. (2024) | Glucagon-Like Peptide 1 Receptor Agonists and 13 Obesity-Associated Cancers in T2D | コホート | ~1M | 被引用219、13種の肥満関連癌リスク変化を定量 |
| T1-12 | Dai et al. (2025) | GLP-1 Receptor Agonists and Cancer Risk in Adults With Obesity (with and without diabetes) | Target trial emulation | 大規模 | 非糖尿病者含む癌リスクのtarget trial emulation |
| T1-13 | Ismaiel et al. (2025) | Gastrointestinal adverse events associated with GLP-1 RA in non-diabetic patients with overweight or obesity | SR+network MA | ~15,000 | 非糖尿病者のGI副作用をnetwork MAで定量 |

### カテゴリD: メトホルミン — アンチエイジング・寿命

| # | 著者(年) | タイトル | デザイン | N | 選定理由 |
|---|---------|---------|---------|---|---------|
| T1-14 | Mohammed et al. (2021) | A Critical Review of the Evidence That Metformin Is a Putative Anti-Aging Drug | SR | — | 被引用254、メトホルミン抗老化の最も包括的レビュー |
| T1-15 | Chen et al. (2022) | Metformin in aging and aging-related diseases: clinical applications and relevant mechanisms | Review | — | 被引用169、加齢関連疾患（AD・CVD・癌）への臨床応用 |
| T1-16 | Zhang et al. (2025) | The Anti-Aging Mechanism of Metformin: From Molecular Insights to Clinical Applications | Review | — | 被引用32、AMPK-mTOR経路の最新分子メカニズム+臨床 |
| T1-17 | Vujović et al. (2026) | From Metabolism to Longevity: Molecular Mechanisms Underlying Metformin's Anticancer and Anti-Aging Effects | Review | — | 2026年最新、癌・老化への機序を網羅的評価 |

### カテゴリE: SGLT2阻害薬 — アンチエイジング

| # | 著者(年) | タイトル | デザイン | N | 選定理由 |
|---|---------|---------|---------|---|---------|
| T1-18 | Scisciola et al. (2023) | On the wake of metformin: Do anti-diabetic SGLT2 inhibitors exert anti-aging effects? | Review | — | 被引用26、SGLT2阻害薬の抗老化効果をメトホルミンと比較 |

### カテゴリF: GLP-1 — 神経保護・認知症

| # | 著者(年) | タイトル | デザイン | N | 選定理由 |
|---|---------|---------|---------|---|---------|
| T1-19 | DiGiovanni et al. (2025) | Utility of Pharmacological Agents for Diabetes in Prevention of Alzheimer's Disease: Metformin, GLP-1 Agonists, Insulin, Sulfonylureas | Review | — | メトホルミン+GLP-1のAD予防を総合比較 |
| T1-20 | Penteado et al. (2025) | GLP-1 and neuroprotection in Alzheimer's disease: a systematic review of randomized clinical trials | SR of RCTs | — | GLP-1神経保護効果のRCT限定SR |

---

## Tier 2: 補助論文（参照用）

| # | 著者(年) | タイトル | 補助理由 |
|---|---------|---------|---------|
| T2-1 | Nauck & Müller-Wieland (2022) | Tirzepatide, a dual GIP/GLP-1 receptor co-agonist | Tirzepatide機序・臨床エビデンス概観（被引用327）|
| T2-2 | Bergmann et al. (2022) | Semaglutide for the treatment of overweight and obesity: A review | Semaglutide包括レビュー（被引用212）|
| T2-3 | Gourdy et al. (2023) | Combining GLP-1RAs and SGLT2is in patients with T2DM | GLP-1+SGLT2併用の相乗効果 |
| T2-4 | Cesaro et al. (2023) | Visceral adipose tissue and residual cardiovascular risk | 内臓脂肪とCVDリスクの病態機序（被引用117）|
| T2-5 | Xie et al. (2024) | Seven GLP-1 RAs and polyagonists for weight loss: network MA | Network MAで各薬剤の体重減少効果をランク付け |
| T2-6 | Levy et al. (2024) | Differential Effects of GLP-1 Receptor Agonists on Cancer Risk | 癌リスクの薬剤間差異（natural experiment study）|
| T2-7 | Laeeq et al. (2024) | Role of SGLT2 Inhibitors, DPP-4 Inhibitors, and Metformin in Pancreatic Cancer Prevention | 3薬剤クラスの膵癌予防 |
| T2-8 | Turczynowski et al. (2026) | Impact of GLP-1 RAs on Body Composition and Physical Performance | 体組成・身体能力への包括レビュー |
| T2-9 | Quarenghi et al. (2025) | Weight Regain After Liraglutide, Semaglutide or Tirzepatide Interruption | 薬剤中止後のリバウンド（実臨床の重要課題）|
| T2-10 | Lu et al. (2025) | Effects of GLP-1 RAs on Body Composition in T2D, Overweight or Obesity: MA | T2D含む体組成MAで基準値提供 |
| T2-11 | West et al. (2025) | Are GLP-1 RAs Central Nervous System Penetrant? | CNS移行性レビュー（神経保護の前提） |
| T2-12 | Bhandarkar et al. (2025) | Effect of GLP-1 receptor agonists on body composition | 体組成変化（除脂肪量保護の観点）|
| T2-13 | Khawaji et al. (2025) | Weight Loss Efficacy of Tirzepatide vs Placebo or GLP-1 RAs | Tirzepatide体重減少効果MA |
| T2-14 | Kasagga et al. (2025) | Dose-Dependent Efficacy and Safety of Tirzepatide for Weight Loss in Non-diabetic | Tirzepatide非糖尿病者での用量別効果 |
| T2-15 | Miranda et al. (2025) | Impact of Semaglutide on Lipid Profiles in Overweight and Obese Non-Diabetic Adults | Semaglutide脂質プロファイルへの影響 |
| T2-16 | Dai et al. (2025) | GLP-1 Receptor Agonists and Cancer Risk in Adults With Obesity (JAMA) | 肥満成人の癌リスク（被引用30）|
| T2-17 | Saliev et al. (2025) | Targeting Senescence: Senolytics and Senomorphics in Anti-Aging Interventions | セネセンス標的治療との比較文脈 |
| T2-18 | Hölscher (2025) | Incretin Hormones GLP-1 and GIP Normalize Energy Utilization and Reduce Inflammation in Neurodegeneration | GLP-1/GIPの神経変性疾患への作用 |
| T2-19 | Ismaiel A81 (2025) | GI Adverse Events Associated with GLP-1RA in Non-Diabetic Patients | GI副作用追加データ |
| T2-20 | Uriti et al. (2025) | Systemic Effects of GLP-1 and Dual GIP/GLP-1 Receptor Agonism in Obesity, CV, and Neurodegeneration | GLP-1/GIPの全身効果包括レビュー |

---

## 除外の主な理由別内訳

| 除外理由 | 推定件数 |
|---------|---------|
| 2型糖尿病患者のみ（体組成・老化データなし） | ~200 |
| ガイドライン・一般的疾患管理論 | ~100 |
| 動物実験のみ | ~50 |
| 症例報告・小規模（N<50） | ~80 |
| 関連疾患のみ（心不全・CKD・NAFLD の薬理） | ~62 |
| **合計除外** | **~492** |
