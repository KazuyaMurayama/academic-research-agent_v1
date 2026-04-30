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

### TL;DR — 今すぐ使える上位10手法

| 順位 | 手法 | カテゴリ | 効果量（代表値） | 実装難度 |
|---|---|---|---|---|
| 1 | Contextual Retrieval | RAG | 検索失敗率 **-67%**（+reranking） | ★★ |
| 2 | Cross-Encoder Reranking | RAG | nDCG@10 **+5〜15点** / 精度+40% | ★★ |
| 3 | Hybrid Retrieval (Dense+BM25) | RAG | 精度 **+15〜48%** | ★★ |
| 4 | Chain-of-Thought (CoT) | プロンプト | 数学・論理 **+15〜40%** | ★ |
| 5 | Multi-Agent Debate | エージェント | 事実性 **+85.5%**（フレームワーク依存） | ★★★ |
| 6 | CLAUDE.md コンテキスト管理 | Claude Code | コンテキスト汚染防止・セッション継続性 | ★ |
| 7 | Constrained Decoding / JSON Mode | その他 | スキーマ精度 **99.5%** | ★ |
| 8 | Few-shot + 例選定最適化 | プロンプト | **+10〜50%**（例の質依存） | ★ |
| 9 | HyDE（仮想ドキュメント埋め込み） | RAG | nDCG@10 **61.3 vs 44.5**（Contriever比） | ★★ |
| 10 | Self-Refine（反復精錬） | プロンプト | 人間評価で **+20%** 支持率向上 | ★ |

> **⚠️ 重要な反直感的発見（必読）**
> - **Self-correction（自己修正）は「初期プロンプトが弱い場合のみ」有効**（ICLR 2024）。強い初期プロンプトでは効果なし
> - **プロンプトの複雑化 ≠ 性能向上**。過剰な例（over-prompting）は逆にパフォーマンスを低下させる
> - **Self-Consistencyは期待外れ**。少数ショットCoTと単体比較で限定的な追加効果しかない
> - **HyDEは生成LLMが弱いと逆効果**。幻覚した仮想ドキュメントが検索精度を下げる場合がある
> - **ボーラス投与型ビタミンD（AI設計での類推）**: 一気に大量コンテキストを与えるより、継続的な少量更新（CLAUDE.md漸進更新）の方が効果的

---

## 本レポートの使い方・R001との差別化

### R001との関係

| 観点 | R001（LLMハルシネーション低減） | 本レポート（R029） |
|---|---|---|
| 主軸 | ハルシネーション「現象」の理論・分類整理 | 指示出し・設計「行為」を主軸にした手法カタログ |
| 構成原理 | 原因 → 検出 → 緩和の理論軸 | カテゴリ × 手法カード（8軸スコア） |
| 対象範囲 | LLM一般のハルシネーション | プロンプト / RAG / エージェント / Claude Code / その他 |
| 評価 | 緩和率中心 | 効果量・コスト・難度・適用条件すべて並列 |
| 用途 | 全体像の理解 | 実装時の即時参照・手法選択 |

本レポートはR001を既読済みの前提で書かれています。ハルシネーションの**理論的分類・原因論**はR001を参照してください。

### 本レポートの読み方

1. まず §10「効果量サマリ表」で全手法を俯瞰する
2. 自分のタスクに近い手法を §9「フローチャート」で絞り込む
3. 各手法カードで「適用条件」「限界」を必ず確認する
4. §11「アンチパターン集」で落とし穴を事前確認する

---

## 評価方法論（8軸スコアリング）

各手法は以下の8軸で評価します。**E1（効果量）とE2（証拠強度）の両方が基準を満たす手法のみを掲載しています。**

| 軸 | 内容 | スケール |
|---|---|---|
| E1 効果量 | 報告されたメトリクス改善幅（%・絶対値） | 数値 + メトリクス名 |
| E2 証拠強度 | 1=ブログ事例のみ / 2=arXiv単発 / 3=複数論文再現 / 4=査読済みメタ分析 | 1〜4 |
| E3 適用範囲 | タスク種別（reasoning / retrieval / coding / dialog / summarization） | タグ集合 |
| E4 コスト | 追加トークン・呼び出し回数の倍率 | ×1〜×N |
| E5 実装難度 | ★=プロンプト変更のみ / ★★=パイプライン追加 / ★★★=学習が必要 | ★〜★★★ |
| E6 適用条件 | 効く前提（モデルサイズ・ドメイン・入力長等） | テキスト |
| E7 限界・反例 | 効かない・逆効果になる条件 | テキスト |
| E8 アクショナビリティ | 1=理論のみ / 5=コピペ可能 | 1〜5 |

**採用閾値**: E1が報告あり、かつ E2≥2、かつ E8≥3 を満たす手法のみを本体に掲載。

---

## プロンプトエンジニアリング

プロンプトエンジニアリングは「追加コストゼロ」で最も即座に効果が出やすいカテゴリです。ただし**手法の効果はモデルサイズに大きく依存**します（小モデルではCoT逆効果の報告あり）。また **「複雑化すれば良い」という直感は誤り** です（§11参照）。

### P-01 Chain-of-Thought（CoT）プロンプティング

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 数学・論理タスク **+15〜40%** 正解率向上（GSM8K, MATH等）|
| **E2 証拠強度** | 4（Wei et al. 2022 NeurIPS + 多数の追証論文） |
| **E3 適用範囲** | reasoning, math, logic, multi-step QA |
| **E4 コスト** | ×1.5〜2（思考ステップ分トークン増） |
| **E5 実装難度** | ★（プロンプト末尾に "Let's think step by step" を追加するだけ） |
| **E6 適用条件** | **モデルサイズ≥7B以上が前提**（小モデルでは逆効果の報告あり）。複数ステップの推論が必要なタスクで特に有効 |
| **E7 限界・反例** | 単純なファクトルックアップタスクでは効果なし。RL強化済み推論モデル（DeepSeek-R1等）ではさらなる追加効果が小さい |
| **E8 アクショナビリティ** | 5 |

**今すぐできるアクション**:
```
# Zero-shot CoT（最小実装）
prompt = user_input + "\n\nLet's think step by step."

# Few-shot CoT（推奨）
examples = [
  {"question": "...", "reasoning": "Step 1: ... Step 2: ... Answer: 42"},
  ...
]
```
出典: [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)（Wei et al. 2022）、[ICLR 2024 CorrectBench](https://www.emergentmind.com/topics/correctbench)

### P-02 Self-Refine（反復的自己精錬）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 人間評価での支持率 **+20%**（GPT-4含む複数モデルで確認）|
| **E2 証拠強度** | 3（Madaan et al. 2023 NeurIPS + 独立追証） |
| **E3 適用範囲** | summarization, code generation, dialog, creative writing |
| **E4 コスト** | ×2〜3（フィードバック生成 + 再生成分） |
| **E5 実装難度** | ★（プロンプトパターンの組み合わせのみ） |
| **E6 適用条件** | 初期出力の品質を具体的な基準でフィードバックできるタスク向け。**外部基準（テストケース・スキーマ等）があると効果が大きい** |
| **E7 限界・反例** | ⚠️ **初期プロンプトが強い場合は改善幅が小さい**（ICLR 2024）。フィードバックが曖昧だと改悪も起こる。クローズドループでは同じ誤りを繰り返す |
| **E8 アクショナビリティ** | 4 |

**今すぐできるアクション**:
```
# 3ステップ Self-Refine
# Step 1: 初期生成
output1 = llm(prompt)
# Step 2: 自己フィードバック（具体的な評価基準を渡す）
feedback = llm(f"以下の出力を評価してください。[評価基準:明確さ/正確さ/完全性]\n{output1}")
# Step 3: 改善版生成
output2 = llm(f"以下のフィードバックを踏まえて改善してください:\n{feedback}\n元の出力:\n{output1}")
```
出典: [arXiv:2303.17651](https://arxiv.org/abs/2303.17651)（Madaan et al. 2023）、[ICLR 2024 - Large Language Models Cannot Self-Correct](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf)

### P-03 Few-shot プロンプティングと例選定

| 軸 | 内容 |
|---|---|
| **E1 効果量** | **+10〜50%**（例の品質・タスク種別による）。例選定最適化（TF-IDF）で macro F1 **+16.6%** vs ランダム選定 |
| **E2 証拠強度** | 4（Brown et al. 2020 GPT-3論文 + 多数追証） |
| **E3 適用範囲** | 分類 / 情報抽出 / 翻訳 / コード生成 / すべてのタスク |
| **E4 コスト** | ×1.2〜2（例の数に応じてトークン増） |
| **E5 実装難度** | ★（プロンプトに例を追加するだけ） |
| **E6 適用条件** | **例の品質・代表性が効果を決定**。数より質が重要。TF-IDF的な関連度で例を選ぶと有効 |
| **E7 限界・反例** | ⚠️ **Over-prompting**: 例数が多すぎると逆にパフォーマンス低下。ドメイン特化型の過剰な例は一部LLMで逆効果。ラベル分布・出力形式に過剰適合するリスク |
| **E8 アクショナビリティ** | 5 |

**今すぐできるアクション**:
```
# 例選定のベストプラクティス
# 1. 多様性: 例はタスクの異なるパターンを網羅する（同じパターンを複数入れない）
# 2. 関連度: クエリと意味的に近い例を選ぶ（TF-IDFまたは埋め込み類似度で）
# 3. 最適数: 2〜8例が最も安定（10+は要注意）
# 4. フォーマット統一: 全例で同じ入力→出力形式を維持する

few_shot_template = """
例1:
入力: {ex1_input}
出力: {ex1_output}

例2:
入力: {ex2_input}
出力: {ex2_output}

タスク:
入力: {user_input}
出力:"""
```
出典: [Brown et al. 2020](https://arxiv.org/abs/2005.14165)、[The Few-shot Dilemma: Over-prompting LLMs (2025)](https://arxiv.org/html/2509.13196v1)

### P-04 役割プロンプティング（Role Prompting）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | AQUA数学データセット: **53%→63%**（GPT-3.5でロールプレイ導入、+10pp）|
| **E2 証拠強度** | 2（PromptHub 2024実験 + 複数事例報告） |
| **E3 適用範囲** | 専門ドメイン回答（医療・法律・コード・数学）/ トーン制御 / 会話エージェント |
| **E4 コスト** | ×1.1〜1.3（役割定義分のトークン増） |
| **E5 実装難度** | ★ |
| **E6 適用条件** | 専門知識・特定のトーン・推論スタイルが必要な場面で有効。**システムプロンプトで役割を定義するのが最も効果的** |
| **E7 限界・反例** | **現代の大型モデル（Claude 3.5+, GPT-4+）ではすでに高品質な回答を生成するため追加効果が小さい**。過剰な役割設定はジェイルブレイクのリスクを高める |
| **E8 アクショナビリティ** | 5 |

**今すぐできるアクション**:
```
# 推奨テンプレート（システムプロンプト）
system_prompt = """あなたは{専門領域}の専門家です。
以下の原則で回答してください:
1. エビデンスに基づく事実のみを述べる
2. 不確実な場合は「確信度: 低」と明記する
3. 回答は{形式: 箇条書き/段落/JSON}で構造化する"""
```
出典: [PromptHub Role Prompting Study](https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference)、[arXiv:2406.00627](https://arxiv.org/pdf/2406.00627)

### P-05 構造化プロンプト（XML / Markdown 区切り）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 指示追従率・出力品質の改善（定量データは構造依存）。**Claude公式は「XMLタグを使うと解析精度が向上する」と明記** |
| **E2 証拠強度** | 3（Anthropic公式ドキュメント + 独立評価レポート） |
| **E3 適用範囲** | 長大なプロンプト / 複数指示を含む複雑なタスク / システムプロンプト設計 |
| **E4 コスト** | ×1.0（構造タグ自体はごく少量） |
| **E5 実装難度** | ★ |
| **E6 適用条件** | プロンプトが2段落以上になる場合。指示・コンテキスト・出力形式が混在する場合に特に有効 |
| **E7 限界・反例** | 単純なシングルターン質問では効果なし。タグが増えすぎると読みにくくなる |
| **E8 アクショナビリティ** | 5 |

**今すぐできるアクション**:
```xml
<!-- Claude向け推奨テンプレート -->
<task>
  <role>あなたはシニアデータサイエンティストです</role>
  <context>
    ユーザーは機械学習の初学者。Python歴3ヶ月。
  </context>
  <instructions>
    1. 技術用語は初めて登場する際に説明する
    2. コードは必ずコメント付きで提示する
    3. 回答は500字以内にまとめる
  </instructions>
  <input>{ユーザーの質問}</input>
  <output_format>
    説明: ...
    コード: ```python ... ```
    補足: ...
  </output_format>
</task>
```
出典: [Anthropic Claude Best Practices](https://claude.com/blog/best-practices-for-prompt-engineering)、[Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

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
