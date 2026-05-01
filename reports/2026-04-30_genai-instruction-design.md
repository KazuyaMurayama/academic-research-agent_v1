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

| # | 手法 | 効果（代表値） | 証拠 | コスト | 実装難度 |
|---|---|---|---|---|---|
| 1 | **M-03 Hybrid Retrieval + Reranking** | RAG精度 **+15〜48%** | ★★★ | ×1.5〜2 | ★★ |
| 2 | **M-04 Contextual Retrieval** | 検索失敗率 **−67%**（+Reranking時） | ★★★ | ×1.3 | ★★ |
| 3 | **M-06 Constrained Decoding / JSON Mode** | スキーマ適合率 **99.5%** | ★★★★ | ×1 | ★ |
| 4 | **M-01 Chain-of-Thought（CoT）** | 数学・推論 **+15〜40%** | ★★★★ | ×1.5〜2 | ★ |
| 5 | **M-02 Few-shot + 例選定** | タスク精度 **+10〜50%**（例の質依存） | ★★★★ | ×1〜1.5 | ★ |
| 6 | **M-05 Tool-Augmented Grounding** | 事実QA精度 **+30%** | ★★★★ | ×1.5〜3 | ★★ |
| 7 | **M-07 Claude Code 実践セット** | コンテキスト汚染防止・再現性向上 | ★★★ | ×1 | ★ |

> **⚠️ 反直感的な発見（必読）**
> - **CoTは小モデルで逆効果**。7B以下のモデルでは推論ステップが誤りを増幅する場合あり
> - **プロンプトの複雑化 ≠ 性能向上**。例が多すぎると（over-prompting）精度が下がる（arXiv:2509.13196）
> - **Self-correction（自己修正）は万能でない**。初期プロンプトが既に強い場合は効果ほぼゼロ（Huang et al. ICLR 2024）
> - **HyDEは生成LLMが弱いと逆効果**（廃止理由参照。Contextual Retrievalを代わりに使う）

---

## 本レポートの使い方

1. §3「フローチャート」で自分のタスクに合う手法を絞り込む
2. 対象の手法カードを開き「いつ使うか」→「実装」→「落とし穴」の順に読む
3. コードをコピーして即試す。§5「アンチパターン集」で失敗を事前回避

**R001との違い**: R001はハルシネーションの原因・分類・理論。本レポートは**「何をどう実装するか」の実践カタログ**。ハルシネーション理論はR001参照。

**v1からの変更**: 22手法→7手法に厳選（廃止手法は§6参照）。8軸スコア表を廃止し読みやすいカード形式に変更。

---

## 手法選択フローチャート

```
課題は何か？
│
├─ 「AIの回答が論理的でない / 推論が浅い」
│      └─ → M-01 Chain-of-Thought
│
├─ 「出力の形式が安定しない / JSONが壊れる」
│      └─ → M-06 Constrained Decoding / JSON Mode
│
├─ 「特定タスクで精度が低い（分類・変換・要約など）」
│      └─ → M-02 Few-shot + 例選定
│
├─ 「社内ドキュメント・外部データを参照させたい（RAG）」
│      ├─ 検索ヒット率が低い → M-03 Hybrid Retrieval + Reranking
│      └─ ヒットするが内容理解が浅い → M-04 Contextual Retrieval
│
├─ 「最新情報・外部API・計算が必要」
│      └─ → M-05 Tool-Augmented Grounding
│
└─ 「Claude Codeのセッションが不安定 / コンテキストが汚染される」
       └─ → M-07 Claude Code 実践セット
```

> 複数の課題が重なる場合: **RAGタスクは M-03 → M-04 の順で積み上げ**が最も効果的。
> プロンプト系（M-01/M-02）はほぼ全タスクに追加コストほぼゼロで適用可。

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
