# 大規模言語モデルのハルシネーション低減手法: エビデンスベース論文サーチレポート

**作成日**: 2026-02-28
**検索実行者**: Academic Research Agent (Claude Code)
**検索方法論**: PRISMA 2020準拠

---

## 1. Executive Summary

大規模言語モデル（LLM）のハルシネーション低減は、AI安全性における最重要課題の一つである。本レポートでは、2022〜2026年の222件の論文を体系的にレビューし、25件を最終分析対象として選定した。分析の結果、ハルシネーション低減手法は主に4カテゴリに大別される：(1)検索拡張生成（RAG）、(2)自己検証・修正パイプライン、(3)サンプリングベース検出、(4)学習段階での対照学習。最も有望なアプローチはRAGと自己検証の組み合わせであり、WikiChatは事実正確性97.3%を達成した。一方、計算コスト、マルチモーダル対応、リアルタイム知識更新等の課題が残る。単一手法では完全解決が困難であり、多層防御アプローチが推奨される。

---

## 2. 研究背景と目的

大規模言語モデル（LLM）は自然言語処理において革命的な能力を示す一方、事実に基づかない情報を生成する「ハルシネーション」が深刻な課題となっている。医療、法律、教育等の高リスクドメインでは、ハルシネーションが誤診や法的問題を引き起こす可能性がある（Shusterman et al., 2025）。

ハルシネーションの原因は多層的であり、訓練データの品質（データ起因）、学習プロセスの限界（学習起因）、推論時のデコーディング戦略（推論起因）の3層にわたる（Zhang et al., 2023）。本レポートでは、これらの原因に対応する低減手法を体系的に整理し、現在のエビデンスに基づく推奨事項を提示する。

**目的**:
- LLMハルシネーション低減手法の現状を包括的に把握する
- 各手法の有効性・限界を比較評価する
- 実務への適用指針を提示する

---

## 3. 検索方法論

### 3.1 検索戦略
- **検索データベース**: Semantic Scholar, arXiv, OpenAlex
- **検索式**:
  1. `LLM hallucination mitigation`
  2. `large language model factual accuracy improvement`
  3. `retrieval augmented generation hallucination`
  4. `LLM grounding faithfulness`
  5. `chain of thought verification factuality`
- **検索期間**: 2022-2026年
- **言語**: 英語

### 3.2 選定基準
- **包含基準**: LLMのハルシネーション低減・検出・評価に直接関連する論文
- **除外基準**: 視覚的錯覚（optical illusion）、薬物誘発幻覚、ハルシネーションに言及のないLLM一般論文

### 3.3 PRISMAフロー（テキスト版）
```
検索ヒット数:      273件（3 API × 5クエリ）
  ↓ 重複排除
重複排除後:         222件（51件除去）
  ↓ スクリーニング
スクリーニング通過:  25件
  ↓ 分類
最終採用:           Tier 1 10件 + Tier 2 15件
```

---

## 4. エビデンス概要

### 4.1 検索拡張生成（RAG）ベースの手法

RAGは外部知識ベースから関連文書を検索し、LLMのプロンプトに付加することでハルシネーションを低減する最も実用的なアプローチである（Gao et al., 2023）。

**進化段階**:
- **Naive RAG**: 単純な検索→生成パイプライン。基本的だが効果的
- **Advanced RAG**: チャンク最適化、クエリリライト、リランキングにより検索品質を向上
- **Modular RAG**: 検索・生成・評価を独立モジュール化し柔軟に組み合わせ

**課題**: Chen et al. (2023)のベンチマークにより、ノイズ文書が混入するとむしろハルシネーションが増加することが判明。検索品質の担保が不可欠。

### 4.2 自己検証・修正パイプライン

LLM自身が生成結果を検証・修正するアプローチ。多段階パイプラインにより精度を向上させる。

- **Chain-of-Verification (CoVe)**: 生成→検証質問生成→独立回答→最終修正の4段階（Dhuliawala et al., 2023）
- **Verify-and-Edit**: CoTの各ステップを外部知識で検証し、不正確部分を編集（Zhao et al., 2023）
- **RARR**: 検索エンジンでエビデンスを取得し、LLM出力を事後的にリサーチ・修正（Gao et al., 2023）

### 4.3 サンプリングベース検出

- **SelfCheckGPT**: 同一プロンプトに対する複数サンプリングの一貫性を評価。外部リソース不要でハルシネーションを検出（Manakul et al., 2023）

### 4.4 学習段階での手法

- **対照学習**: 正例（事実に基づく応答）と負例（ハルシネーション応答）のペアでファインチューニング（Sun et al., 2023）
- **知識蒸留**: 高精度大型モデルの能力を小型モデルに蒸留。WikiChatはGPT-4の知見を7B LLaMAに蒸留し97.3%の精度を達成（Semnani et al., 2023）

---

## 5. 比較テーブル

| 著者(年) | 研究デザイン | アプローチ | 対象(N) | 主要結果 | エビデンスレベル | 備考 |
|----------|-------------|-----------|---------|---------|----------------|------|
| Huang et al. (2024) | 系統的レビュー | 包括的分類体系 | 200+論文 | 事実性/忠実性の2軸分類確立 | 1a | 最も引用数の多いサーベイ |
| Zhang et al. (2023) | 系統的レビュー | 原因・対策体系化 | 100+論文 | データ/学習/推論の3原因分類 | 1a | 初期の包括的サーベイ |
| Gao et al. (2023) | 系統的レビュー | RAGサーベイ | 150+論文 | RAG進化体系(Naive→Advanced→Modular) | 1a | RAGの標準的参照文献 |
| Chen et al. (2023) | ベンチマーク | RAGベンチマーク | 4タスク×6モデル | ノイズ文書がハルシネーション増加 | 2b | RAGの限界を示す重要知見 |
| Manakul et al. (2023) | 実験研究 | サンプリング一貫性 | GPT-3 WikiBio | ゼロリソース検出実現 | 2b | 外部知識不要の利点 |
| Dhuliawala et al. (2023) | 実験研究 | 自己検証(CoVe) | Llama/ChatGPT | リスト型Q&Aでハルシネーション大幅低減 | 2b | 計算コスト高 |
| Zhao et al. (2023) | 実験研究 | 知識強化CoT | マルチホップQA | CoT精度向上 | 2b | 外部KB依存 |
| Semnani et al. (2023) | 実験研究 | Wikiグラウンディング | GPT-4→7B蒸留 | 事実正確性97.3%(+12.6%pt) | 2b | 最高精度 |
| Gao et al. (2023) | 実験研究 | 事後リサーチ修正 | 複数ドメイン | 文体保持＋事実性向上 | 2b | 実用的アプローチ |
| Sun et al. (2023) | 実験研究 | 対照学習 | 知識型対話 | ハルシネーション率有意低減 | 2b | 学習段階の手法 |

---

## 6. 詳細分析

### 6.1 RAGの有効性と限界

Gao et al. (2023)のサーベイにより、RAGはLLMハルシネーション低減の最も実用的かつ広く採用されている手法であることが確認された。しかし、Chen et al. (2023)のベンチマーク評価は重要な注意点を明らかにした：

- **ノイズ耐性**: 検索結果にノイズ（無関連文書）が含まれると、LLMはそれに基づいたハルシネーションを生成する傾向がある
- **反事実耐性**: 検索結果が事実と矛盾する情報を含む場合、LLMは検索結果を優先する傾向がある
- **情報統合**: 複数の検索結果を統合する際にハルシネーションが発生しやすい

**実務的示唆**: RAGの導入時には、検索品質の確保（高品質なリトリーバーとリランキングモデル）が不可欠であり、単純なRAG導入だけでは不十分。

### 6.2 自己検証手法の比較

| 手法 | 段階数 | 外部知識要否 | 計算コスト | 精度改善 |
|------|--------|------------|-----------|---------|
| CoVe | 4段階 | 不要 | 高（4× 推論） | リスト型Q&Aで顕著 |
| Verify-and-Edit | 3段階 | 必要（KB） | 中〜高 | マルチホップで効果的 |
| RARR | 3段階 | 必要（検索） | 高 | 汎用的に効果的 |
| WikiChat | 7段階 | 必要（Wikipedia） | 最高 | 事実正確性97.3% |

WikiChatが最高精度を達成したが、7段階パイプラインの計算コストが課題。CoVeは外部知識不要で導入容易だが、精度はWikiChatに劣る。用途に応じた選択が必要。

### 6.3 検出と低減のギャップ

SelfCheckGPT（Manakul et al., 2023）は外部知識なしでハルシネーションを検出できる画期的な手法だが、検出結果を自動的に修正に活用するパイプラインはまだ発展途上。検出→修正の自動化が今後の重要課題。

---

## 7. エビデンスギャップと今後の研究課題

1. **マルチモーダルハルシネーション低減**: テキスト以外のモダリティ（画像、音声、動画）を含むマルチモーダルLLMでの低減手法は研究初期段階
2. **リアルタイム知識更新**: 静的知識ベースに依存するRAGは、急速に変化する情報に追従できない。動的知識更新メカニズムの研究が必要
3. **低コスト多段階検証**: CoVeやWikiChatの有効性は確認されているが、計算コストの削減が実用化の鍵
4. **ドメイン特化型評価**: 医療・法律等の高リスクドメインに特化したハルシネーション評価ベンチマークと低減手法の体系的検証が不足
5. **長文生成での累積ハルシネーション**: 長い文書生成における累積的なハルシネーションの低減手法は未確立
6. **多言語対応**: 英語以外の言語でのハルシネーション低減手法の有効性検証がほぼ空白

---

## 8. 実務への示唆（Practical Implications）

### 即座に導入可能な手法

| 手法 | 導入難易度 | コスト | 推奨シーン |
|------|-----------|--------|-----------|
| 基本RAG | 低 | 低 | 社内ドキュメント検索、FAQ自動応答 |
| SelfCheckGPT | 中 | 中 | 生成結果の品質フィルタリング |
| プロンプトエンジニアリング | 低 | 最低 | 全般的なLLM活用 |

### 高精度が必要な場合

| 手法 | 導入難易度 | コスト | 推奨シーン |
|------|-----------|--------|-----------|
| Advanced RAG + リランキング | 中〜高 | 中 | 医療情報、法律相談 |
| CoVe/Verify-and-Edit | 高 | 高 | 意思決定支援、レポート生成 |
| WikiChat型パイプライン | 最高 | 最高 | ファクトチェック、ジャーナリズム支援 |

### 推奨アクション

1. **段階的導入**: まず基本RAGを導入し、精度不足が判明した場合にAdvanced RAGやCoVeを追加
2. **検出の組み込み**: SelfCheckGPT等の検出機能を品質ゲートとして組み込み、低信頼度の応答をフィルタリング
3. **ドメイン知識ベースの構築**: 業務固有の高品質な知識ベースを構築し、RAGの検索品質を向上
4. **人間によるレビュー**: 高リスクドメインでは、LLM出力を必ず人間がレビューするプロセスを維持

---

## 9. 参考文献

Chen, J., Lin, H., Han, X., & Sun, L. (2023). Benchmarking large language models in retrieval-augmented generation. *Proceedings of AAAI*. https://doi.org/10.48550/arXiv.2309.01431

Dhuliawala, S., Komeili, M., Xu, J., Raileanu, R., Li, X., Celikyilmaz, A., & Weston, J. (2023). Chain-of-verification reduces hallucination in large language models. *arXiv preprint*. https://arxiv.org/abs/2309.11495

Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., ... & Wang, H. (2023). Retrieval-augmented generation for large language models: A survey. *arXiv preprint*. https://doi.org/10.48550/arxiv.2312.10997

Gao, L., Dai, Z., Pasupat, P., Chen, A., Chaganty, A. T., Fan, Y., ... & Kelham, C. (2023). RARR: Researching and revising what language models say, using language models. *Proceedings of ACL*. https://doi.org/10.18653/v1/2023.acl-long.910

Huang, L., Yu, W., Ma, W., Zhong, W., Feng, Z., Wang, H., ... & Liu, T. (2024). A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions. *ACM Computing Surveys*. https://doi.org/10.1145/3703155

Li, J., Cheng, X., Zhao, W. X., Nie, J. Y., & Wen, J. R. (2023). HaluEval: A large-scale hallucination evaluation benchmark for large language models. *Proceedings of EMNLP*. https://doi.org/10.18653/v1/2023.emnlp-main.397

Lin, S., Hilton, J., & Evans, O. (2022). TruthfulQA: Measuring how models mimic human falsehoods. *Proceedings of ACL*. https://doi.org/10.18653/v1/2022.acl-long.229

Manakul, P., Liusie, A., & Gales, M. J. (2023). SelfCheckGPT: Zero-resource black-box hallucination detection for generative large language models. *Proceedings of EMNLP*. https://doi.org/10.18653/v1/2023.emnlp-main.557

Semnani, S. J., Yao, V., Zhang, H., & Lam, M. S. (2023). WikiChat: Stopping the hallucination of large language model chatbots by few-shot grounding on Wikipedia. *Findings of EMNLP*. https://doi.org/10.18653/v1/2023.findings-emnlp.157

Shusterman, M., et al. (2025). Medical hallucinations in foundation models and their impact on healthcare. *Nature Medicine*. https://doi.org/10.1038/s41591-025-03507-w

Sun, Z., Shen, S., Cao, S., Liu, H., Li, C., Shen, Y., ... & Yang, N. (2023). Contrastive learning reduces hallucination in conversations. *Proceedings of AAAI*. https://doi.org/10.1609/aaai.v37i11.26577

Zhang, Y., Li, Y., Cui, L., Cai, D., Liu, L., Fu, T., ... & Shi, S. (2023). Siren's song in the AI ocean: A survey on hallucination in large language models. *Computational Linguistics*. https://doi.org/10.1162/coli.a.16

Zhao, R., Li, X., Joty, S., Qin, C., & Bing, L. (2023). Verify-and-edit: A knowledge-enhanced chain-of-thought framework. *Proceedings of ACL*. https://doi.org/10.18653/v1/2023.acl-long.292

---

## 付録

### A. 全スクリーニング結果

| # | Tier | タイトル | 著者(年) | 被引用数 | エビデンスレベル |
|---|------|---------|----------|---------|----------------|
| 1 | T1 | A Survey on Hallucination in LLMs | Huang et al. (2024) | 1,038 | 1a |
| 2 | T1 | Siren's Song: Survey on Hallucination | Zhang et al. (2023) | 876 | 1a |
| 3 | T1 | RAG for LLMs: A Survey | Gao et al. (2023) | 599 | 1a |
| 4 | T1 | Benchmarking LLMs in RAG | Chen et al. (2023) | 485 | 2b |
| 5 | T1 | SelfCheckGPT | Manakul et al. (2023) | 259 | 2b |
| 6 | T1 | Verify-and-Edit | Zhao et al. (2023) | 201 | 2b |
| 7 | T1 | WikiChat | Semnani et al. (2023) | 104 | 2b |
| 8 | T1 | RARR | Gao et al. (2023) | 81 | 2b |
| 9 | T1 | Contrastive Learning Reduces Hallucination | Sun et al. (2023) | 56 | 2b |
| 10 | T1 | Chain-of-Verification | Dhuliawala et al. (2023) | 39 | 2b |
| 11 | T2 | A Survey on RAG Meeting LLMs | Fan et al. (2024) | 408 | 1a |
| 12 | T2 | TruthfulQA | Lin et al. (2022) | 468 | 2b |
| 13 | T2 | Active Retrieval Augmented Generation | Jiang et al. (2023) | 274 | 2b |
| 14 | T2 | HaluEval | Li et al. (2023) | 197 | 2b |
| 15 | T2 | Graph RAG | Mavromatis et al. (2024) | 153 | 2b |
| 16 | T2 | Reducing hallucination via RAG | Ke et al. (2024) | 134 | 2b |
| 17 | T2 | Factuality Hallucination (HaluEval 2.0) | Chern et al. (2024) | 119 | 2b |
| 18 | T2 | Chain-of-Knowledge Prompting | Li et al. (2023) | 113 | 2b |
| 19 | T2 | LLM Hallucinations in Code Generation | Tian et al. (2024) | 96 | 2b |
| 20 | T2 | Trustworthiness in RAG Systems | Wu et al. (2024) | 87 | 1a |
| 21 | T2 | Logic-LM | Pan et al. (2023) | 81 | 2b |
| 22 | T2 | Medical Hallucinations | Shusterman et al. (2025) | 77 | 2b |
| 23 | T2 | KG-Based RAG for Hallucination Mitigation | Bayazit et al. (2024) | 53 | 2b |
| 24 | T2 | AlignScore | Zha et al. (2023) | 32 | 2b |
| 25 | T2 | Multi-agentic LLM Hallucination Mitigation | Leite et al. (2024) | 8 | 2b |

### B. 検索クエリ詳細

| # | クエリ | S2取得数 | arXiv取得数 | OA取得数 | 合計 |
|---|--------|---------|------------|---------|------|
| 1 | LLM hallucination mitigation | 30 | 2 | 30 | 62 |
| 2 | large language model factual accuracy improvement | 30 | 0 | 30 | 60 |
| 3 | retrieval augmented generation hallucination | 30 | 1 | 30 | 61 |
| 4 | LLM grounding faithfulness | 0* | 0 | 30 | 30 |
| 5 | chain of thought verification factuality | 30 | 0 | 30 | 60 |
| - | **合計** | **120** | **3** | **150** | **273** |

*S2 = Semantic Scholar, OA = OpenAlex。*クエリ4のS2は429レート制限により取得失敗（フォールバック動作）
