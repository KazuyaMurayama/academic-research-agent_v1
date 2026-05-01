# 生成AIツール活用における効果的な指示設計ガイド v2
## 厳選7手法・コピペ即使用リファレンス

**作成日**: 2026-04-30 / **改訂**: 2026-05-01（v2: 22手法→7手法に厳選）
**レポートID**: R029
**関連**: R001（LLMハルシネーション低減 — 理論・原因論はR001参照）

---

## 目次

1. [TL;DR — 今すぐ使える7手法](#tldr--今すぐ使える7手法)
2. [本レポートの使い方](#本レポートの使い方)
3. [手法選択フローチャート](#手法選択フローチャート)
4. [手法カード](#手法カード)
   - [M-01 Chain-of-Thought（CoT）](#m-01-chain-of-thoughtcot)
   - [M-02 Few-shot + 例選定最適化](#m-02-few-shot--例選定最適化)
   - [M-03 Hybrid Retrieval + Reranking](#m-03-hybrid-retrieval--reranking)
   - [M-04 Contextual Retrieval](#m-04-contextual-retrieval)
   - [M-05 Tool-Augmented Grounding](#m-05-tool-augmented-grounding)
   - [M-06 Constrained Decoding / JSON Mode](#m-06-constrained-decoding--json-mode)
   - [M-07 Claude Code 実践セット](#m-07-claude-code-実践セット)
5. [アンチパターン集](#アンチパターン集)
6. [廃止手法早見表（v1との差分）](#廃止手法早見表v1との差分)
7. [参考文献](#参考文献)
8. [更新履歴](#更新履歴)

---

## TL;DR — 今すぐ使える7手法

<!-- S1_EXEC_SUMMARY_PLACEHOLDER -->

---

## 本レポートの使い方

<!-- S2_USAGE_PLACEHOLDER -->

---

## 手法選択フローチャート

<!-- S3_FLOWCHART_PLACEHOLDER -->

---

## 手法カード

> **カードの読み方**: 各カードは「いつ使うか → 実装コード → コツ → 落とし穴」の順。
> バッジ表記: **効果** = 代表メトリクス | **証拠** ★〜★★★ | **コスト** ×N | **実装難度** ★〜★★★

---

### M-01 Chain-of-Thought（CoT）

<!-- CARD_01_COT_PLACEHOLDER -->

---

### M-02 Few-shot + 例選定最適化

<!-- CARD_02_FEWSHOT_PLACEHOLDER -->

---

### M-03 Hybrid Retrieval + Reranking

<!-- CARD_03_HYBRID_RAG_PLACEHOLDER -->

---

### M-04 Contextual Retrieval

<!-- CARD_04_CONTEXTUAL_PLACEHOLDER -->

---

### M-05 Tool-Augmented Grounding

<!-- CARD_05_TOOL_GROUNDING_PLACEHOLDER -->

---

### M-06 Constrained Decoding / JSON Mode

<!-- CARD_06_JSON_MODE_PLACEHOLDER -->

---

### M-07 Claude Code 実践セット

<!-- CARD_07_CLAUDE_CODE_PLACEHOLDER -->

---

## アンチパターン集

<!-- S4_ANTIPATTERNS_PLACEHOLDER -->

---

## 廃止手法早見表（v1との差分）

<!-- S5_DEPRECATED_PLACEHOLDER -->

---

## 参考文献

<!-- S6_REFERENCES_PLACEHOLDER -->

---

## 更新履歴

| バージョン | 日付 | 変更内容 |
|---|---|---|
| v1.0 | 2026-04-30 | 初版作成（22手法・5カテゴリ・8軸スコアリング） |
| v1.1 | 2026-05-01 | ファクトチェック修正（arXiv ID、年号、数値帰属の誤り7件修正） |
| v2.0 | 2026-05-01 | 大幅改訂: 22手法→7手法に厳選。カード形式リライト。具体例・コード充実 |
