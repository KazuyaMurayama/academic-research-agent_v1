# スクリーニング結果: 大規模言語モデルのハルシネーション低減手法

**実施日**: 2026-02-28
**対象論文数**: 222件（重複排除後）
**バッチ処理**: 10本 × 23バッチ

---

## 評価基準

| 基準 | 説明 |
|------|------|
| 関連性 | テーマ（LLMハルシネーション低減手法）との直接的関連度 |
| 影響度 | 被引用数 × 出版年の新しさ |
| エビデンスレベル | Oxford CEBM準拠（サーベイ/ベンチマーク > 実験研究 > 提案手法） |
| 研究デザイン | サーベイ / ベンチマーク / 手法提案 / 実験評価 |

---

## Tier 1: コア論文（10本）— 詳細分析対象

### T1-1. A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges
- **著者**: Huang et al. (2024)
- **被引用数**: 1,038
- **関連性**: High — LLMハルシネーションの原理・分類体系・課題を包括的にサーベイ
- **エビデンスレベル**: 1a（系統的レビュー）
- **選定理由**: 本テーマの最も包括的なサーベイ論文。ハルシネーションの分類体系と低減手法を体系的に整理

### T1-2. Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models
- **著者**: Zhang et al. (2023)
- **被引用数**: 876
- **関連性**: High — LLMハルシネーションのサーベイ、検出・低減手法を包括
- **エビデンスレベル**: 1a（系統的レビュー）
- **選定理由**: ハルシネーションの定義・原因・対策を体系化した重要サーベイ

### T1-3. Retrieval-Augmented Generation for Large Language Models: A Survey
- **著者**: Gao et al. (2023)
- **被引用数**: 599
- **関連性**: High — RAGによるハルシネーション低減の主要手法をサーベイ
- **エビデンスレベル**: 1a（系統的レビュー）
- **選定理由**: ハルシネーション低減の最も実用的なアプローチであるRAGの包括的レビュー

### T1-4. Benchmarking Large Language Models in Retrieval-Augmented Generation
- **著者**: Chen et al. (2023)
- **被引用数**: 485
- **関連性**: High — RAGにおけるLLMのハルシネーション低減効果をベンチマーク
- **エビデンスレベル**: 2b（ベンチマーク評価研究）
- **選定理由**: RAGがハルシネーション低減にどの程度効果的かを定量的に評価

### T1-5. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative LLMs
- **著者**: Manakul et al. (2023)
- **被引用数**: 259
- **関連性**: High — 外部リソース不要のハルシネーション検出手法
- **エビデンスレベル**: 2b（実験研究）
- **選定理由**: ゼロリソースでのハルシネーション検出という独自のアプローチ。検出→低減パイプラインの基盤

### T1-6. Chain-of-Verification Reduces Hallucination in Large Language Models
- **著者**: Dhuliawala et al. (2023)
- **被引用数**: 39
- **関連性**: High — CoT検証によるハルシネーション低減の直接的手法
- **エビデンスレベル**: 2b（実験研究）
- **選定理由**: 自己検証メカニズムによるハルシネーション低減の代表的手法

### T1-7. Verify-and-Edit: A Knowledge-Enhanced Chain-of-Thought Framework
- **著者**: Zhao et al. (2023)
- **被引用数**: 201
- **関連性**: High — 知識強化型CoTフレームワークで事実性を向上
- **エビデンスレベル**: 2b（実験研究）
- **選定理由**: 外部知識による検証・編集でCoTの事実精度を向上させる手法

### T1-8. WikiChat: Stopping the Hallucination of LLM Chatbots by Few-Shot Grounding
- **著者**: Semnani et al. (2023)
- **被引用数**: 104
- **関連性**: High — Wikipediaベースのグラウンディングでハルシネーションを低減
- **エビデンスレベル**: 2b（実験研究）
- **選定理由**: 少数ショットグラウンディングによるハルシネーション低減の実践的手法

### T1-9. RARR: Researching and Revising What Language Models Say, Using Language Models
- **著者**: Gao et al. (2023)
- **被引用数**: 81
- **関連性**: High — LLMの出力を自動的にリサーチ・修正する事後修正手法
- **エビデンスレベル**: 2b（実験研究）
- **選定理由**: 生成後の自動修正という独自アプローチで事実性を向上

### T1-10. Contrastive Learning Reduces Hallucination in Conversations
- **著者**: Sun et al. (2023)
- **被引用数**: 56
- **関連性**: High — 対照学習によるハルシネーション低減
- **エビデンスレベル**: 2b（実験研究）
- **選定理由**: 学習段階での対照学習という低減アプローチの代表的研究

---

## Tier 2: 補助論文（15本）— 参照用

| # | タイトル | 著者(年) | 被引用数 | 関連性 | 選定理由 |
|---|---------|----------|---------|--------|---------|
| T2-1 | HaluEval: A Large-Scale Hallucination Evaluation Benchmark | Li et al. (2023) | 197 | High | ハルシネーション評価ベンチマーク |
| T2-2 | The Dawn After the Dark: Empirical Study on Factuality Hallucination | Chern et al. (2024) | 119 | High | 事実性ハルシネーションの体系的実証研究 |
| T2-3 | Reducing hallucination in structured outputs via RAG | Ke et al. (2024) | 134 | High | 構造化出力でのRAGによるハルシネーション低減 |
| T2-4 | LLM Hallucinations in Practical Code Generation | Tian et al. (2024) | 96 | Medium | コード生成でのハルシネーション研究 |
| T2-5 | Graph RAG: Graph Neural Retrieval for LLM Reasoning | Mavromatis et al. (2024) | 153 | Medium | グラフベースRAGの推論改善 |
| T2-6 | A Survey on RAG Meeting LLMs | Fan et al. (2024) | 408 | High | RAG+LLMの包括サーベイ |
| T2-7 | Boosting Language Models Reasoning with Chain-of-Knowledge | Li et al. (2023) | 113 | Medium | 知識連鎖によるLLM推論強化 |
| T2-8 | TruthfulQA: Measuring How Models Mimic Human Falsehoods | Lin et al. (2022) | 468 | High | 事実性評価の標準ベンチマーク |
| T2-9 | Logic-LM: Empowering LLMs with Symbolic Solvers | Pan et al. (2023) | 81 | Medium | 記号的推論による忠実性向上 |
| T2-10 | Mitigating LLM Hallucinations via Autonomous KG-Based RAG | Bayazit et al. (2024) | 53 | High | 知識グラフベースRAGによる低減 |
| T2-11 | Medical Hallucinations in Foundation Models | Shusterman et al. (2025) | 77 | Medium | 医療分野でのハルシネーション影響 |
| T2-12 | Trustworthiness in RAG Systems: A Survey | Wu et al. (2024) | 87 | Medium | RAGの信頼性体系的サーベイ |
| T2-13 | Active Retrieval Augmented Generation | Jiang et al. (2023) | 274 | Medium | 能動的検索によるRAG改善 |
| T2-14 | Good Parenting is all you need - Multi-agentic LLM Hallucination Mitigation | Leite et al. (2024) | 8 | High | マルチエージェント型ハルシネーション低減 |
| T2-15 | AlignScore: Evaluating Factual Consistency | Zha et al. (2023) | 32 | Medium | 事実一貫性の統一評価関数 |

---

## 除外論文の概要

| カテゴリ | 件数 | 理由 |
|---------|------|------|
| 一般LLM/ChatGPTサーベイ（テーマ外） | ~80 | ハルシネーション低減に直接関連しない |
| 医療/教育/法律分野応用（間接的） | ~45 | ドメイン応用が主でハルシネーション低減手法ではない |
| インフラ/効率化（vLLM等） | ~15 | メモリ管理等が主題でハルシネーション低減ではない |
| その他ノイズ（メタバース、感情分析等） | ~57 | テーマと無関連 |

---

## スクリーニング統計

- **総入力**: 222件
- **Tier 1（コア）**: 10件（4.5%）
- **Tier 2（補助）**: 15件（6.8%）
- **除外**: 197件（88.7%）
- **エビデンスレベル分布（Tier 1）**: 1a=3本, 2b=7本
