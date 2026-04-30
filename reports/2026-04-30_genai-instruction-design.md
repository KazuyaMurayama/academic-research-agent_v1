# 生成AIツール活用における効果的な指示設計ガイド
## 検証済み手法カタログ（定量評価・適用条件付き）

**作成日**: 2026-04-30
**レポートID**: R029
**手法総数**: 22手法（5カテゴリ）
**評価軸**: 8軸スコアリング（効果量 / 証拠強度 / 適用範囲 / コスト / 実装難度 / 適用条件 / 限界 / アクショナビリティ）
**関連レポート**: R001（LLMハルシネーション低減）— 本レポートはR001の「行為ベース手法カタログ」として差別化

---

## 目次

1. [エグゼクティブサマリー](#エグゼクティブサマリー)
2. [本レポートの使い方・R001との差別化](#本レポートの使い方r001との差別化)
3. [評価方法論（8軸スコアリング）](#評価方法論8軸スコアリング)
4. [プロンプトエンジニアリング](#プロンプトエンジニアリング)
5. [RAG精度向上技術](#rag精度向上技術)
6. [AIエージェントによるハルシネーション抑制](#aiエージェントによるハルシネーション抑制)
7. [Claude Codeの有効な使い方](#claude-codeの有効な使い方)
8. [その他のリスク低減・精度向上手法](#その他のリスク低減精度向上手法)
9. [手法選択フローチャート](#手法選択フローチャート)
10. [効果量サマリ表](#効果量サマリ表)
11. [アンチパターン集](#アンチパターン集)
12. [参考文献](#参考文献)

---

## エグゼクティブサマリー

<!-- S1_EXECUTIVE_SUMMARY_PLACEHOLDER -->

---

## 本レポートの使い方・R001との差別化

<!-- S2_INTRO_DIFFERENTIATION_PLACEHOLDER -->

---

## 評価方法論（8軸スコアリング）

<!-- S3_METHODOLOGY_PLACEHOLDER -->

---

## プロンプトエンジニアリング

<!-- P_SECTION_INTRO_PLACEHOLDER -->

### P-01 Chain-of-Thought（CoT）プロンプティング

<!-- P01_COT_PLACEHOLDER -->

### P-02 Self-Refine（反復的自己精錬）

<!-- P02_SELF_REFINE_PLACEHOLDER -->

### P-03 Few-shot プロンプティングと例選定

<!-- P03_FEW_SHOT_PLACEHOLDER -->

### P-04 役割プロンプティング（Role Prompting）

<!-- P04_ROLE_PROMPTING_PLACEHOLDER -->

### P-05 構造化プロンプト（XML / Markdown 区切り）

<!-- P05_STRUCTURED_PROMPT_PLACEHOLDER -->

---

## RAG精度向上技術

<!-- R_SECTION_INTRO_PLACEHOLDER -->

### R-01 Hybrid Retrieval（Dense + BM25）

<!-- R01_HYBRID_RETRIEVAL_PLACEHOLDER -->

### R-02 Cross-Encoder Reranking（二段階検索）

<!-- R02_CROSS_ENCODER_PLACEHOLDER -->

### R-03 Contextual Retrieval（Anthropic方式）

<!-- R03_CONTEXTUAL_RETRIEVAL_PLACEHOLDER -->

### R-04 HyDE（仮想ドキュメント埋め込み）

<!-- R04_HYDE_PLACEHOLDER -->

### R-05 チャンク設計・オーバーラップ最適化

<!-- R05_CHUNK_DESIGN_PLACEHOLDER -->

---

## AIエージェントによるハルシネーション抑制

<!-- A_SECTION_INTRO_PLACEHOLDER -->

### A-01 Multi-Agent Debate（多エージェント討論）

<!-- A01_MULTI_AGENT_DEBATE_PLACEHOLDER -->

### A-02 Planner-Executor-Critic分離パターン

<!-- A02_PLANNER_EXECUTOR_CRITIC_PLACEHOLDER -->

### A-03 ツール使用による事実照合（Tool-Augmented Grounding）

<!-- A03_TOOL_GROUNDING_PLACEHOLDER -->

### A-04 信頼度較正（Rewarding Doubt）

<!-- A04_CONFIDENCE_CALIBRATION_PLACEHOLDER -->

---

## Claude Codeの有効な使い方

<!-- C_SECTION_INTRO_PLACEHOLDER -->

### C-01 CLAUDE.md によるコンテキスト管理

<!-- C01_CLAUDE_MD_PLACEHOLDER -->

### C-02 サブエージェント活用パターン

<!-- C02_SUBAGENT_PLACEHOLDER -->

### C-03 コンテキスト管理コマンド（/clear・/compact）

<!-- C03_CONTEXT_MGMT_PLACEHOLDER -->

### C-04 5コアワークフローパターン

<!-- C04_WORKFLOW_PATTERNS_PLACEHOLDER -->

### C-05 プロンプト設計：ビジネスゴール × ユーザーコンテキスト × 成功基準

<!-- C05_PROMPT_DESIGN_PLACEHOLDER -->

---

## その他のリスク低減・精度向上手法

<!-- O_SECTION_INTRO_PLACEHOLDER -->

### O-01 構造化出力・Constrained Decoding

<!-- O01_STRUCTURED_OUTPUT_PLACEHOLDER -->

### O-02 ガードレール（NeMo Guardrails・Llama Guard）

<!-- O02_GUARDRAILS_PLACEHOLDER -->

### O-03 Human-in-the-Loop設計

<!-- O03_HITL_PLACEHOLDER -->

---

## 手法選択フローチャート

<!-- S9_FLOWCHART_PLACEHOLDER -->

---

## 効果量サマリ表

<!-- S10_SUMMARY_TABLE_PLACEHOLDER -->

---

## アンチパターン集

<!-- S11_ANTIPATTERNS_PLACEHOLDER -->

---

## 参考文献

<!-- S12_REFERENCES_PLACEHOLDER -->
