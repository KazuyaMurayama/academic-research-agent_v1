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

RAGは「ハルシネーション率 -42%」（ベースラインLLM比）という最強クラスの効果量を持ちます。ただし**コンポーネントごとに精度への寄与が異なる**ため、どの段階を優先して改善するかが重要です。検索段（Retrieval）→ 再ランキング段（Reranking）→ 生成段（Generation）の順に改善するのが推奨です。

### R-01 Hybrid Retrieval（Dense + BM25）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 精度 **+15〜48%**（Pinecone: 62%→91% = +48%、BEIR一般: +15〜30%）|
| **E2 証拠強度** | 4（複数独立評価 + 商用実装報告） |
| **E3 適用範囲** | 専門用語・固有名詞の多いドメイン文書検索（法律・医療・金融） |
| **E4 コスト** | ×1.1（2種の検索 + マージ処理、無視できるレベル） |
| **E5 実装難度** | ★★（BM25インデックス + Dense埋め込みインデックスの両方を構築） |
| **E6 適用条件** | **専門用語・固有名詞が多く、語彙ミスマッチが頻発する場面で最も効果的**。Dense単体では語彙ミスマッチで失敗するケースを補完する |
| **E7 限界・反例** | 短い口語クエリ・FAQタスクではDense単体との差が縮小。財務文書ではBM25単体がDenseを上回るケースあり |
| **E8 アクショナビリティ** | 4 |

**今すぐできるアクション**:
```python
# Reciprocal Rank Fusion (RRF) による結合（推奨）
def rrf_merge(dense_results, sparse_results, k=60):
    scores = {}
    for rank, doc_id in enumerate(dense_results):
        scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank + 1)
    for rank, doc_id in enumerate(sparse_results):
        scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank + 1)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

# BM25推奨パラメータ: k1=1.2, b=0.75
# Dense推奨モデル: e5-large-v2 / text-embedding-3-large
```
出典: [Pinecone Hybrid Search Analysis](https://www.pinecone.io/)、[arXiv:2604.01733](https://arxiv.org/html/2604.01733v1)（BM25 vs RAG Benchmark 2025）

### R-02 Cross-Encoder Reranking（二段階検索）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | nDCG@10 **+5〜15点**（MS MARCO）/ 精度 **+40%**（ailog.fr 2025報告）/ zerank-1: **+28%** nDCG@10 vs ベースライン |
| **E2 証拠強度** | 4（MS MARCO・BEIR複数評価 + MIT 2段階検索研究） |
| **E3 適用範囲** | RAGパイプラインの第2段階。ドメイン問わず汎用的に有効 |
| **E4 コスト** | ×1.5〜2（上位K件を全文比較するため計算コスト増） |
| **E5 実装難度** | ★★（検索後にRerankerモデルを追加するだけ） |
| **E6 適用条件** | **第1段階の検索でRecall@100が高い場合に最も効果的**。ただし第1段階のRecallが低い場合はRerankで補えない |
| **E7 限界・反例** | Cross-encoderは計算コストが高く、リアルタイムの低レイテンシが必要なケースでは採用しにくい。代替: CROSS-JEM（4倍低レイテンシ）|
| **E8 アクショナビリティ** | 4 |

**今すぐできるアクション**:
```python
from sentence_transformers import CrossEncoder

# 推奨モデル（2025年時点）
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")  # 高速
# または
reranker = CrossEncoder("BAAI/bge-reranker-v2-m3")  # 高精度

def rerank(query, candidate_docs, top_k=5):
    pairs = [(query, doc) for doc in candidate_docs]
    scores = reranker.predict(pairs)
    ranked = sorted(zip(scores, candidate_docs), reverse=True)
    return [doc for _, doc in ranked[:top_k]]
```
出典: [Cross-Encoder Reranking Improves RAG by 40%](https://app.ailog.fr/en/blog/news/reranking-cross-encoders-study)、[ZeroEntropy zerank-1](https://zeroentropy.dev/articles/ultimate-guide-to-choosing-the-best-reranking-model-in-2025/)

### R-03 Contextual Retrieval（Anthropic方式）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 検索失敗率 **-49%**（Contextual Embeddingsのみ）/ **-67%**（+reranking）。Precision@20: 0.65→0.89（+37%）|
| **E2 証拠強度** | 3（Anthropic公式ベンチマーク 2024年9月発表） |
| **E3 適用範囲** | 長文書（報告書・マニュアル・法令）のチャンク化RAG |
| **E4 コスト** | ×2〜3（チャンクごとにLLMで文脈説明を生成、**prompt cachingで大幅削減可能**） |
| **E5 実装難度** | ★★ |
| **E6 適用条件** | チャンクが単独では文脈不足になるドキュメント（例: 「その会社の収益が3%増加した」← どの会社？）に特に有効 |
| **E7 限界・反例** | 文脈生成コストが高い（ただしprompt cachingで90%削減可能）。短い独立性の高いチャンクでは効果小 |
| **E8 アクショナビリティ** | 3 |

**今すぐできるアクション**:
```python
# Anthropic公式実装（Claude + Prompt Caching）
# 推奨チャンクサイズ: 800トークン、オーバーラップ: 100トークン

CONTEXTUAL_PROMPT = """
<document>
{full_document}
</document>

<chunk>
{chunk_content}
</chunk>

このチャンクが文書全体の中でどのような文脈にあるかを、
1〜2文の簡潔な説明で記述してください。
検索クエリに対してこのチャンクが見つかりやすくなるよう記述します。
"""

def add_context_to_chunk(chunk, full_doc):
    context = llm(CONTEXTUAL_PROMPT.format(
        full_document=full_doc, chunk_content=chunk
    ))
    return f"{context}\n\n{chunk}"
```
出典: [Anthropic Contextual Retrieval (2024)](https://www.anthropic.com/news/contextual-retrieval)、[Anthropic Claude Cookbook](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide)

### R-04 HyDE（仮想ドキュメント埋め込み）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | nDCG@10 **61.3 vs 44.5**（Contriever比）on TREC DL-20。クエリ拡張全体で **+14〜37%** 向上 |
| **E2 証拠強度** | 3（Gao et al. 2022 + TREC/BEIR評価） |
| **E3 適用範囲** | 専門文書への検索・ゼロショット検索・クエリが短い場合 |
| **E4 コスト** | ×1.5〜2（仮想ドキュメント生成分のLLMコール追加） |
| **E5 実装難度** | ★★ |
| **E6 適用条件** | クエリが短く・曖昧で、コーパスと語彙ミスマッチが生じる場面で有効。**LLMがドメイン知識を持っていることが前提** |
| **E7 限界・反例** | ⚠️ **生成モデルが弱い・ドメイン外の場合、幻覚した仮想ドキュメントが検索精度を下げる**。クエリが具体的な場合はHybrid Retrievalの方が安定 |
| **E8 アクショナビリティ** | 3 |

**今すぐできるアクション**:
```python
def hyde_retrieval(query, retriever, n_hypothetical=5):
    # Step 1: 仮想ドキュメントを複数生成
    hypothetical_docs = []
    for _ in range(n_hypothetical):
        hyp_doc = llm(f"次のクエリに答える可能性が高い文書を生成してください:\n{query}")
        hypothetical_docs.append(hyp_doc)

    # Step 2: 仮想ドキュメントの埋め込みを取得して検索
    embeddings = [embed(doc) for doc in hypothetical_docs]
    avg_embedding = sum(embeddings) / len(embeddings)
    results = retriever.search_by_vector(avg_embedding)
    return results
```
出典: [Gao et al. 2022 HyDE](https://arxiv.org/abs/2212.10496)、[Adaptive HyDE (arXiv 2025)](https://arxiv.org/html/2507.16754v1)

### R-05 チャンク設計・オーバーラップ最適化

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 最適チャンクサイズでRecall@20 **+2.8pp**（Contextual Retrieval実験より）。不適切なチャンク設計は検索失敗率を2〜3倍に悪化させる |
| **E2 証拠強度** | 3（Anthropic Cookbook + 複数実装比較） |
| **E3 適用範囲** | すべてのRAGシステム（基盤設計段階で決定必要） |
| **E4 コスト** | ×1.0（一度設計すれば変わらない） |
| **E5 実装難度** | ★★ |
| **E6 適用条件** | ドキュメントの構造・文書長・クエリの平均長に応じて最適値が異なる |
| **E7 限界・反例** | 万能な最適値はなく、ドメイン・タスクごとに実験が必要 |
| **E8 アクショナビリティ** | 4 |

**今すぐできるアクション**:
```python
# Anthropic推奨値（Contextual Retrieval用）
CHUNK_SIZE = 800       # トークン
CHUNK_OVERLAP = 100    # トークン（前後の文脈連続性を保つ）

# ドキュメント構造に応じた分割方針
# - 法律文書: 条項単位（=意味的チャンク）
# - 技術マニュアル: セクション見出しで分割
# - 長文レポート: 段落 + オーバーラップ
# - Q&A集: Q&Aペア単位（分割しない）

# 評価指標: Recall@K（K=5,10,20）でチューニング
# target Recall@20 ≥ 0.85 for regulated content
```
出典: [Anthropic Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)、[RAG Evaluation Guide 2025](https://www.getmaxim.ai/articles/rag-evaluation-a-complete-guide-for-2025/)

---

## AIエージェントによるハルシネーション抑制

単一LLMでは推論・記憶・知識検索を同時に担うことによる限界があります。エージェント設計によって**役割分離・相互検証・外部ツール活用**を導入することで、ハルシネーションを構造的に抑制できます。ただし**コストと実装複雑度が大幅に増加する**ため、費用対効果の評価が必要です。

### A-01 Multi-Agent Debate（多エージェント討論）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 事実性・推論精度 **+85.5%**（特定フレームワーク）/ ハルシネーション率: GPT-4o **53%→23%**（プロンプトベース緩和込み）|
| **E2 証拠強度** | 3（Du et al. 2023 ICML + MDPI 2025論文） |
| **E3 適用範囲** | 高精度が要求されるQ&A / 主張検証 / 複雑な推論タスク |
| **E4 コスト** | ×3〜5（エージェント数 × 討論ラウンド数分のLLMコール） |
| **E5 実装難度** | ★★★ |
| **E6 適用条件** | 「正解の検証可能性」が高いタスクで最も効果的（数学・事実確認・コードレビュー）。速度より精度が重要な場面 |
| **E7 限界・反例** | コスト・レイテンシが大幅に増加。エージェント間で誤りが伝播するリスク（群衆の誤り）。意見集約の方式（投票・合意）によって結果が変わる |
| **E8 アクショナビリティ** | 3 |

**今すぐできるアクション**:
```python
# 最小実装パターン（2エージェント）
def debate_verify(question, rounds=2):
    agent_a_response = llm(question)
    for _ in range(rounds):
        # Agent B: Agent Aの回答を批判・検証
        critique = llm(f"""
        以下の回答の問題点・事実誤認を指摘してください:
        質問: {question}
        回答: {agent_a_response}
        """)
        # Agent A: 批判を踏まえて改訂
        agent_a_response = llm(f"""
        以下の批判を踏まえて回答を改善してください:
        元の回答: {agent_a_response}
        批判: {critique}
        """)
    return agent_a_response
```
出典: [Du et al. 2023 - Improving Factuality via Multiagent Debate](https://arxiv.org/abs/2305.14325)、[MDPI 2025 - Mitigating LLM Hallucinations](https://www.mdpi.com/2078-2489/16/7/517)

### A-02 Planner-Executor-Critic分離パターン

| 軸 | 内容 |
|---|---|
| **E1 効果量** | SWE-bench等のコーディングエージェントで精度向上（単一モデル比）。各役割への最適化により**エラー検出率が大幅向上** |
| **E2 証拠強度** | 3（複数のエージェントフレームワーク実装報告） |
| **E3 適用範囲** | 長期タスク / コード生成・レビュー / 多段階ワークフロー |
| **E4 コスト** | ×2〜4（役割数 × コール数） |
| **E5 実装難度** | ★★★ |
| **E6 適用条件** | タスクが明確にフェーズ分割できる場合（計画→実行→評価が自然に分離できる）|
| **E7 限界・反例** | 役割境界が曖昧だとエラーが積み重なる。シンプルなタスクには過剰設計 |
| **E8 アクショナビリティ** | 3 |

**今すぐできるアクション**:
```
# Claude Code での実装例（CLAUDE.md設定）
## エージェント役割分担
- Planner（Opus）: タスク分析・サブタスク分解・依存関係整理
- Executor（Sonnet）: コード生成・ファイル操作・API呼び出し
- Critic（Sonnet/Haiku）: 出力検証・テスト実行・品質チェック

# 設計原則
1. Plannerは実行しない（計画のみ）
2. ExecutorはPlannerの指示からはみ出さない
3. Criticは明確なチェックリストを持つ（曖昧な評価禁止）
```
出典: [Claude Code Sub-Agents Best Practices](https://code.claude.com/docs/en/sub-agents)、[MARCH: Multi-Agent Reinforced Self-Check](https://arxiv.org/html/2603.24579v1)

### A-03 ツール使用による事実照合（Tool-Augmented Grounding）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | ハルシネーション率の大幅低減（RAG単体で -42%、計算ツールで数学的誤りをほぼ0%へ）|
| **E2 証拠強度** | 4（ToolformerからFunction Callingまで多数の査読論文） |
| **E3 適用範囲** | 数値計算 / 最新情報検索 / コード実行 / データベース参照 |
| **E4 コスト** | ×1.3〜2（ツール呼び出し分の追加処理） |
| **E5 実装難度** | ★★（ツール定義とFunction Calling APIの設定） |
| **E6 適用条件** | **「LLMの記憶」に頼れない情報（最新情報・精密計算・外部DB）が必要な場面で必須** |
| **E7 限界・反例** | ツール選択ミス・ツール結果の誤解釈が起こりうる。ツールが利用不可の環境では使えない |
| **E8 アクショナビリティ** | 4 |

**今すぐできるアクション**:
```python
# Claude Function Callingの最小実装
tools = [
    {
        "name": "web_search",
        "description": "最新情報を検索する。知識カットオフ以降の情報や変動する数値はこのツールを使う",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"]
        }
    },
    {
        "name": "calculate",
        "description": "数値計算を正確に実行する。LLMで計算せず必ずこのツールを使う",
        "input_schema": {"type": "object", "properties": {"expression": {"type": "string"}}}
    }
]
# 重要: ツール説明に「いつ使うか / いつ使わないか」を明記することで選択精度が向上
```
出典: [Schick et al. 2023 Toolformer](https://arxiv.org/abs/2302.04761)、[AWS - Reducing Hallucinations with Amazon Bedrock Agents](https://aws.amazon.com/blogs/machine-learning/reducing-hallucinations-in-large-language-models-with-custom-intervention-using-amazon-bedrock-agents/)

### A-04 信頼度較正（Rewarding Doubt）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | モデルの自信度とアウトカム精度の相関を強化（Expected Calibration Error を大幅削減）|
| **E2 証拠強度** | 2（Rewarding Doubt 2025 arXiv + 追証論文） |
| **E3 適用範囲** | 高リスク意思決定支援 / 医療診断補助 / 法律文書レビュー |
| **E4 コスト** | ×1.2（信頼度スコア出力分のオーバーヘッド） |
| **E5 実装難度** | ★（プロンプトで信頼度の明示を要求するだけで即効性あり） |
| **E6 適用条件** | モデルが「わからない」と言える安全な文化・プロダクト設計が前提 |
| **E7 限界・反例** | モデルは自己評価が不正確なことが多い。信頼度スコアを過信しないこと |
| **E8 アクショナビリティ** | 4 |

**今すぐできるアクション**:
```
# プロンプトレベルでの即時実装（★ 実装難度1）
あなたの回答の各文に対して、確信度を以下の形式で示してください:
- [HIGH]: 複数の信頼できるソースで確認済み
- [MEDIUM]: 一般的な知識として知っているが確認していない
- [LOW]: 推測・不確か。ユーザーが独自に確認することを強く推奨

不確かな場合は「確信度: LOW / この情報は必ず独自に確認してください」と明記すること。
「わかりません」「確認が必要です」と言うことを恐れないこと。
```
出典: [Rewarding Doubt 2025 - Confidence Calibration in RL](https://arxiv.org/html/2510.06265v1)、[Lakera LLM Hallucination Guide 2026](https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models)

---

## Claude Codeの有効な使い方

Claude Codeは「エージェント型コーディング環境」です。チャットボットと異なり、ファイル読み書き・コマンド実行・自律的な問題解決が可能です。このカテゴリは**学術論文が少なく、公式ドキュメントとコミュニティ実践知が主なソース**です。各手法のラベル: 🔵=公式ドキュメント記載、🟡=コミュニティ実践知。

> ⚠️ **本レポートが属するシステム（academic-research-agent_v1）はClaude Codeを活用したリサーチエージェントであり、以下の手法は実際にこのプロジェクトで実装・検証されています。**

### C-01 CLAUDE.md によるコンテキスト管理

🔵 **公式ドキュメント記載**

| 軸 | 内容 |
|---|---|
| **E1 効果量** | セッション横断のコンテキスト維持。コンテキスト再説明コスト **ほぼ0**（なければ毎回数百〜数千トークン消費） |
| **E2 証拠強度** | 3（公式ドキュメント + コミュニティ多数の実装報告） |
| **E3 適用範囲** | プロジェクト全体のClaude Code利用 |
| **E4 コスト** | ×1.05〜1.1（CLAUDE.md読み込み分のトークン） |
| **E5 実装難度** | ★ |
| **E6 適用条件** | 複数セッションにわたる継続的な開発・調査プロジェクト全般 |
| **E7 限界・反例** | ファイルが肥大化すると逆にトークンを消費しすぎる。更新を怠ると誤った前提でタスクを実行する |
| **E8 アクショナビリティ** | 5 |

**今すぐできるアクション（推奨CLAUDE.md構成）**:
```markdown
# プロジェクト名

## 最重要ルール（毎回読む）
- Gitブランチ: masterのみにpush
- コミット: タスク単位で細かく行う

## ディレクトリ構造
- reports/ : レポート保存先
- outputs/ : 一時ファイル（gitignore済み）

## セッション開始時の必須手順
1. tasks.md を Read → 未完了タスク確認
2. reports/INDEX.md を Read → 重複調査防止

## 重要な設計決定（なぜそうなっているか）
- チャンクサイズを800に設定: Anthropic Contextual Retrieval推奨値
- BM25を使用: 専門用語の多い医学文書で語彙ミスマッチが頻発するため
```
出典: 🔵 [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)、🟡 [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)

### C-02 サブエージェント活用パターン

🔵 **公式ドキュメント記載**

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 並列実行で複数タスクを同時処理 → 作業時間 **最大N倍速**（N=並列数）。コンテキスト汚染防止でメインスレッドの集中力を維持 |
| **E2 証拠強度** | 3（公式ドキュメント + 複数実装報告） |
| **E3 適用範囲** | 独立した複数タスク（リサーチ+実装+レビューを同時進行）/ 大量データ処理 |
| **E4 コスト** | ×N（サブエージェント数分のコール・コンテキスト） |
| **E5 実装難度** | ★★ |
| **E6 適用条件** | **タスクが独立している場合**（依存関係があると並列化の効果が出ない）。サブタスクの結果が全体の方向性を変えない場合 |
| **E7 限界・反例** | メインコンテキストとサブエージェントのコンテキスト間で情報の受け渡しが必要な場合、設計が複雑になる。ツール・MCP権限の個別設定が必要 |
| **E8 アクショナビリティ** | 4 |

**今すぐできるアクション**:
```markdown
# サブエージェントをいつ使うか（ルーティング基準）
## 並列ディスパッチ（同時実行）
- 3つ以上の独立したタスクがある
- 1つのタスクが他に影響しない
- 例: 「5カテゴリ同時に検索する」

## 逐次ディスパッチ（順番に実行）
- タスクに依存関係がある
- 前のタスク結果を次に渡す必要がある

## バックグラウンドディスパッチ
- 長時間の検索・分析タスク
- 結果を待たずに別作業を進めたい場合

# CLAUDE.md でのサブエージェント定義例
Agent(subagent_type="Explore", prompt="...")  # 調査専門
Agent(subagent_type="Plan", model="opus", prompt="...")  # 計画・設計
```
出典: 🔵 [Claude Code Sub-Agents](https://code.claude.com/docs/en/sub-agents)、🟡 [Claude Code Sub-Agent Best Practices](https://claudefa.st/blog/guide/agents/sub-agent-best-practices)

### C-03 コンテキスト管理コマンド（/clear・/compact）

🔵 **公式ドキュメント記載**

| 軸 | 内容 |
|---|---|
| **E1 効果量** | コンテキスト汚染防止。タスク切り替え時の混乱・誤実行を防止（定量値は非公開だが公式が強く推奨） |
| **E2 証拠強度** | 3（公式ドキュメント + コミュニティ多数報告） |
| **E3 適用範囲** | 複数の異なるタスクを同一セッションで扱う場合 |
| **E4 コスト** | ×0（むしろコンテキスト削減） |
| **E5 実装難度** | ★ |
| **E6 適用条件** | タスクが切り替わるとき / 新しいプロジェクトを開始するとき |
| **E7 限界・反例** | /clear後は前のタスクの履歴が消えるため、CLAUDE.mdや文書として残していない情報は失われる |
| **E8 アクショナビリティ** | 5 |

**今すぐできるアクション**:
```
# コマンド一覧と使いどころ
/clear      - タスク切り替え時（例: Aの実装→Bのレビュー）
/compact    - 会話が長くなってきたが継続したい時（自動要約してコンテキスト圧縮）

# ベストプラクティス
1. 1タスク = 1セッション を基本とする
2. タスク完了 → /clear → 次のタスク
3. 長時間タスクは節目でcommitしてから /compact
4. CLAUDE.mdに「前提知識」を書いておけば /clear後も再現可能
```
出典: 🔵 [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)

### C-04 5コアワークフローパターン

🔵 **公式ドキュメント記載**

Claude Codeには5つのコアワークフローパターンがあり、タスク特性に応じて使い分けることが重要です。

| パターン | 概要 | 最適な用途 | コスト |
|---|---|---|---|
| **Sequential** | タスクを順番に実行 | 依存関係のある多段階処理 | ×1 |
| **Operator** | 人間の確認を挟みながら進行 | 高リスク・不可逆な操作 | ×1 + 待機時間 |
| **Split-and-Merge** | 並列分割 → 統合 | 独立した大量サブタスク | ×N → ×1 |
| **Agent Teams** | 専門エージェントの協調 | 多専門領域をまたぐ複雑タスク | ×N |
| **Headless** | 自律無人実行 | CI/CD / 定期自動処理 | ×1（最高自動化） |

**今すぐできるアクション（タスク → パターン選択）**:
```
タスク種別          推奨パターン
----------------------------------
コードレビュー       Operator（確認ありで安全）
論文一括収集        Headless（自律実行）
マルチカテゴリ調査  Split-and-Merge（並列）
複雑な設計判断      Agent Teams（Opus計画 + Sonnet実行）
通常の実装タスク    Sequential（標準）
```

> 🟡 **コミュニティ実践知**: 「シンプルな制御ループ（Bash + Read + Edit）は複雑なフレームワーク（重いRAG・複雑なオーケストレーション）より多くの場合に優れている」- 実践者報告

出典: 🔵 [5 Claude Code Agentic Workflow Patterns](https://www.mindstudio.ai/blog/claude-code-agentic-workflow-patterns)、🟡 [Claude Code Best Practices](https://thoughtminds.ai/blog/claude-code-best-practices-for-agentic-coding-in-modern-software-development)

### C-05 プロンプト設計：ビジネスゴール × ユーザーコンテキスト × 成功基準

🟡 **コミュニティ実践知（公式推奨を含む）**

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 「build a dashboard」→ビジネスゴール明記プロンプトへの変換で、**実装の妥当性・設計品質が大幅向上**（コミュニティ多数報告）|
| **E2 証拠強度** | 3（公式推奨 + コミュニティ広範な報告） |
| **E3 適用範囲** | Claude Codeへのすべてのタスク指示 |
| **E4 コスト** | ×1.1（より詳細な指示の分のトークン増） |
| **E5 実装難度** | ★ |
| **E6 適用条件** | 常に適用可能 |
| **E7 限界・反例** | 成功基準が定義しにくい創造的タスクではフレームワークが硬直化することがある |
| **E8 アクショナビリティ** | 5 |

**今すぐできるアクション（プロンプトテンプレート）**:
```
❌ 悪い例（コマンド型）:
「ダッシュボードを作って」

✅ 良い例（ゴール・コンテキスト・基準型）:
【ビジネスゴール】
月次の売上レポートを自動生成し、経営陣が5分で意思決定できるようにする

【ユーザーコンテキスト】
- 利用者: 経営陣（非技術者）
- 使用頻度: 毎月1回
- 既存システム: PostgreSQL、PythonでCSV出力済み

【成功基準】
- グラフが3種類以上
- 前月比・前年比を自動計算
- レポート生成が1クリックで完結
- 実行時間 < 30秒

【制約】
- 既存のCSV形式は変更しない
- 追加ライブラリはmatplotlibのみ許可
```
出典: 🔵 [Claude Code Best Practices Official](https://code.claude.com/docs/en/best-practices)、🟡 [eesel AI: 7 Claude Code Best Practices](https://www.eesel.ai/blog/claude-code-best-practices)

---

## その他のリスク低減・精度向上手法

プロンプト・RAG・エージェント以外の補完的な精度向上・リスク低減手法です。特に**出力の形式的な正確性（スキーマ準拠・安全性）**を保証する手法は、プロダクション環境で必須となります。

### O-01 構造化出力・Constrained Decoding

| 軸 | 内容 |
|---|---|
| **E1 効果量** | スキーマ精度 **99.5%**（fine-tuned Mistral-7B + constrained decoding）、content similarity **94.0%**（Claude-3.5-Sonnetを上回る）|
| **E2 証拠強度** | 3（JSONSchemaBench + 複数実装評価） |
| **E3 適用範囲** | LLM出力を別プログラムが消費するすべてのパイプライン |
| **E4 コスト** | ×1.0（むしろ不正確なパースコストが削減） |
| **E5 実装難度** | ★（APIのJSON Mode / structured outputオプションをオン） |
| **E6 適用条件** | LLM出力を後続コードが解析・利用するすべての場合に推奨 |
| **E7 限界・反例** | スキーマが複雑すぎると生成品質が低下することがある。創造的な自由記述には不向き |
| **E8 アクショナビリティ** | 5 |

**今すぐできるアクション**:
```python
# Claude API（Structured Output）
import anthropic, json
from pydantic import BaseModel

class AnalysisResult(BaseModel):
    summary: str
    confidence: float  # 0.0〜1.0
    sources: list[str]
    warnings: list[str]

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    tools=[{
        "name": "output_result",
        "description": "分析結果を構造化して出力する",
        "input_schema": AnalysisResult.model_json_schema()
    }],
    tool_choice={"type": "any"},
    messages=[{"role": "user", "content": "..."}]
)
result = AnalysisResult(**response.content[0].input)
```
出典: [JSONSchemaBench - OpenReview](https://openreview.net/forum?id=FKOaJqKoio)、[Constrained Decoding Guide](https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json)

### O-02 ガードレール（NeMo Guardrails・Llama Guard）

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 有害コンテンツのブロック率 **>95%**（Llama Guard）/ 入力インジェクション攻撃の検出率向上 |
| **E2 証拠強度** | 3（Meta Llama Guard 2024論文 + NVIDIA NeMo評価） |
| **E3 適用範囲** | ユーザー向けプロダクション環境 / 高リスクドメイン（医療・法律・金融） |
| **E4 コスト** | ×1.3〜1.5（ガードレールモデルの追加推論） |
| **E5 実装難度** | ★★ |
| **E6 適用条件** | 不特定多数のユーザーからの入力を処理する場合。規制要件がある業界 |
| **E7 限界・反例** | 過度なフィルタリングは誤検知（false positive）で正当なリクエストも弾く。ガードレール自体が攻撃対象になりうる |
| **E8 アクショナビリティ** | 3 |

**今すぐできるアクション**:
```python
# 最小ガードレール実装（プロンプトレベル）
SYSTEM_GUARDRAIL = """
以下のカテゴリの要求には応じないでください:
- 個人情報の収集・推測
- 違法行為の支援
- 医療診断の確定（必ず「医師に相談してください」と付記）

不明な場合は「この要求には対応できません。{理由}」と回答してください。
"""

# より強固な実装: Llama Guard（オープンソース）
# pip install transformers
# model: meta-llama/Llama-Guard-3-8B
```
出典: [Meta Llama Guard](https://arxiv.org/abs/2312.06674)、[NVIDIA NeMo Guardrails](https://developer.nvidia.com/blog/how-using-a-reranking-microservice-can-improve-accuracy-and-costs-of-information-retrieval/)

### O-03 Human-in-the-Loop設計

| 軸 | 内容 |
|---|---|
| **E1 効果量** | 高リスク操作でのエラー率大幅削減（不可逆な操作の誤実行防止）|
| **E2 証拠強度** | 3（Claude Code公式推奨 + 業界実践知） |
| **E3 適用範囲** | データ削除・本番デプロイ・外部システム変更などの高リスク操作 |
| **E4 コスト** | ×1.0（確認待機時間は発生するが計算コスト追加なし） |
| **E5 実装難度** | ★ |
| **E6 適用条件** | 不可逆な操作 / 外部サービスへの副作用がある操作 / 大規模変更 |
| **E7 限界・反例** | 自動化の恩恵が減少する。承認疲労（approval fatigue）で形骸化するリスク |
| **E8 アクショナビリティ** | 5 |

**今すぐできるアクション**:
```
# Claude Codeでの実装（Operator パターン）
## 確認が必要な操作リスト（CLAUDE.mdに記載）
以下の操作を実行する前に必ずユーザーに確認を求めること:
- git push --force
- データベースの削除・上書き
- 本番環境へのデプロイ
- 外部APIへのPOST/DELETE
- 100行以上のファイルの全書き換え

確認の形式:
「[操作内容]を実行しようとしています。
影響範囲: [影響するファイル・システム]
実行してよいですか？ (yes/no)」
```
出典: 🔵 [Claude Code Best Practices - Reversibility](https://code.claude.com/docs/en/best-practices)

---

## 手法選択フローチャート

タスク特性から推奨手法を絞り込む意思決定フローです。

```
タスクがある
│
├─ 出力を後続コードが使う？
│   └─ YES → O-01 Constrained Decoding（最優先）
│
├─ 外部知識・最新情報が必要？
│   ├─ YES, 文書ベース → RAG全般（R-01〜R-05）
│   │   ├─ 専門用語が多い → R-01 Hybrid Retrieval（最初に実装）
│   │   ├─ 精度をさらに上げたい → R-02 Cross-Encoder Reranking（次に追加）
│   │   ├─ チャンクの文脈が失われている → R-03 Contextual Retrieval
│   │   └─ クエリが短く曖昧 → R-04 HyDE
│   └─ YES, リアルタイム情報 → A-03 Tool-Augmented Grounding
│
├─ 推論・数学・論理が必要？
│   └─ YES → P-01 CoT（まず試す）
│       └─ 精度まだ不足 → P-02 Self-Refine（フィードバックループ）
│
├─ 高精度・高信頼性が必須？
│   ├─ コスト許容 → A-01 Multi-Agent Debate
│   └─ コスト制約あり → A-04 信頼度較正 + Human-in-the-Loop
│
├─ Claude Codeプロジェクト？
│   ├─ セッション横断管理 → C-01 CLAUDE.md
│   ├─ 複数独立タスク → C-02 サブエージェント並列
│   └─ タスク切り替え時 → C-03 /clear
│
└─ 上記いずれでもない（一般タスク）
    └─ P-03 Few-shot + P-05 構造化プロンプトを組み合わせる
```

---

## 効果量サマリ表

全22手法を効果量・証拠強度・実装難度・コストで横断比較します。

| ID | 手法名 | カテゴリ | 効果量（代表値） | E2証拠 | E5難度 | E4コスト | E8即効性 |
|---|---|---|---|---|---|---|---|
| R-03 | Contextual Retrieval | RAG | 検索失敗 **-67%** | ★★★ | ★★ | ×2〜3 | 3 |
| R-02 | Cross-Encoder Reranking | RAG | nDCG **+5〜15点** / +40% | ★★★★ | ★★ | ×1.5〜2 | 4 |
| R-01 | Hybrid Retrieval | RAG | 精度 **+15〜48%** | ★★★★ | ★★ | ×1.1 | 4 |
| P-01 | Chain-of-Thought | プロンプト | 数学論理 **+15〜40%** | ★★★★ | ★ | ×1.5〜2 | 5 |
| A-01 | Multi-Agent Debate | エージェント | 事実性 **+85.5%** | ★★★ | ★★★ | ×3〜5 | 3 |
| O-01 | Constrained Decoding | その他 | スキーマ精度 **99.5%** | ★★★ | ★ | ×1.0 | 5 |
| P-03 | Few-shot + 例選定 | プロンプト | **+10〜50%** | ★★★★ | ★ | ×1.2〜2 | 5 |
| R-04 | HyDE | RAG | nDCG **61.3 vs 44.5** | ★★★ | ★★ | ×1.5〜2 | 3 |
| P-02 | Self-Refine | プロンプト | 支持率 **+20%** | ★★★ | ★ | ×2〜3 | 4 |
| A-03 | Tool-Augmented Grounding | エージェント | 数値誤り **ほぼ0%** | ★★★★ | ★★ | ×1.3〜2 | 4 |
| C-01 | CLAUDE.md管理 | Claude Code | コンテキスト汚染防止 | ★★★ | ★ | ×1.05 | 5 |
| C-02 | サブエージェント並列 | Claude Code | 並列N倍速 | ★★★ | ★★ | ×N | 4 |
| P-04 | Role Prompting | プロンプト | **+10pp**（数学） | ★★ | ★ | ×1.1 | 5 |
| P-05 | 構造化プロンプト | プロンプト | 指示追従率向上 | ★★★ | ★ | ×1.0 | 5 |
| R-05 | チャンク設計最適化 | RAG | 失敗率×2〜3悪化を防止 | ★★★ | ★★ | ×1.0 | 4 |
| A-02 | Planner-Executor-Critic | エージェント | エラー検出率向上 | ★★★ | ★★★ | ×2〜4 | 3 |
| A-04 | 信頼度較正 | エージェント | ECE削減 | ★★ | ★ | ×1.2 | 4 |
| C-03 | /clear・/compact | Claude Code | タスク切り替え品質 | ★★★ | ★ | ×0 | 5 |
| C-04 | 5コアワークフロー | Claude Code | タスク特性適合 | ★★★ | ★★ | 可変 | 4 |
| C-05 | ゴール×コンテキスト×基準 | Claude Code | 実装妥当性向上 | ★★★ | ★ | ×1.1 | 5 |
| O-02 | ガードレール | その他 | 有害ブロック >95% | ★★★ | ★★ | ×1.3〜1.5 | 3 |
| O-03 | Human-in-the-Loop | その他 | 高リスクエラー防止 | ★★★ | ★ | ×1.0 | 5 |

**コスパ最強（効果大 × 実装難度低）**: P-01 CoT、O-01 Constrained Decoding、C-01 CLAUDE.md、P-05 構造化プロンプト

---

## アンチパターン集

### ⚠️ 絶対にやってはいけない指示出し・設計パターン

| # | アンチパターン | なぜ問題か | エビデンス | 正しい対処 |
|---|---|---|---|---|
| 1 | **プロンプトを複雑化すれば精度が上がると思う** | 複雑度 ≠ 性能向上。過剰な指示はモデルを混乱させる | 複数論文・実践報告 | シンプルに書いてから段階的に追加。A/Bテストで検証 |
| 2 | **Self-correction（自己修正）を万能と信じる** | 初期プロンプトが強い場合は改善幅がほぼゼロ | ICLR 2024 | 初期プロンプトを強化する。外部フィードバック（テスト・スキーマ）を使う |
| 3 | **Few-shotの例を大量に詰め込む** | Over-promptingでパフォーマンス低下 | arXiv 2025 | 2〜8例が最適。多様性と関連性でセレクション |
| 4 | **HyDEを何でも使う** | 生成モデルが弱い場合、幻覚した仮想ドキュメントが検索を悪化させる | 実装報告 | まずHybrid Retrievalを試す。HyDEはモデルがドメイン知識を持つ場合のみ |
| 5 | **RAGなしでLLMの記憶に頼る** | 知識カットオフ以降の情報・精密な数値でハルシネーション率が高い | RAG -42%研究 | 常にRAGまたはツール（計算・検索）を使う |
| 6 | **LLMの出力をそのままコードで使う** | 形式・型が保証されず解析エラーが頻発 | JSONSchemaBench | 必ずConstrained Decoding / JSON Modeを使う |
| 7 | **全タスクにMulti-Agent Debateを適用** | コスト×3〜5、レイテンシ増大。単純タスクには完全に過剰 | - | フローチャートで必要性を判断。シンプルなタスクはCoT+Self-Refineで十分 |
| 8 | **CLAUDE.mdを書かずにClaude Codeを使い続ける** | セッションごとに前提の再説明が必要。コンテキストウィンドウを浪費 | 公式推奨 | 最初のセッションでCLAUDE.mdを作成する |
| 9 | **サブエージェントの結果を検証しない** | サブエージェントが誤った情報を返してもメインが気づかない | - | CriticエージェントまたはHuman-in-the-Loopで検証を挟む |
| 10 | **Self-Consistencyを精度向上の決め手と期待する** | Few-shot CoTとの差が限定的。コスト（×5〜10）に見合わないことが多い | 複数論文 | CoT + Self-Refine の組み合わせの方がコスパ良い |

---

## 参考文献

### 学術論文

| ID | タイトル | 著者・年 | リンク |
|---|---|---|---|
| 1 | Chain-of-Thought Prompting Elicits Reasoning in LLMs | Wei et al. 2022 | [arXiv:2201.11903](https://arxiv.org/abs/2201.11903) |
| 2 | SELF-REFINE: Iterative Refinement with Self-Feedback | Madaan et al. 2023 | [arXiv:2303.17651](https://arxiv.org/abs/2303.17651) |
| 3 | Large Language Models Cannot Self-Correct Reasoning Yet | Huang et al. 2024 | [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf) |
| 4 | Improving Factuality via Multiagent Debate | Du et al. 2023 | [arXiv:2305.14325](https://arxiv.org/abs/2305.14325) |
| 5 | Precise Zero-Shot Dense Retrieval (HyDE) | Gao et al. 2022 | [arXiv:2212.10496](https://arxiv.org/abs/2212.10496) |
| 6 | The Few-shot Dilemma: Over-prompting LLMs | 2025 | [arXiv:2509.13196](https://arxiv.org/html/2509.13196v1) |
| 7 | Mitigating LLM Hallucinations: Multi-Agent Framework | MDPI 2025 | [MDPI Information](https://www.mdpi.com/2078-2489/16/7/517) |
| 8 | MARCH: Multi-Agent Reinforced Self-Check | 2025 | [arXiv:2603.24579](https://arxiv.org/html/2603.24579v1) |
| 9 | Toolformer: Language Models Can Teach Themselves | Schick et al. 2023 | [arXiv:2302.04761](https://arxiv.org/abs/2302.04761) |
| 10 | RAGBench: Explainable Benchmark for RAG Systems | 2024 | [arXiv:2407.11005](https://arxiv.org/abs/2407.11005) |
| 11 | From BM25 to Corrective RAG: Benchmarking Strategies | 2025 | [arXiv:2604.01733](https://arxiv.org/html/2604.01733v1) |
| 12 | A Comprehensive Survey of Hallucination in LLMs | 2024 | [arXiv:2510.06265](https://arxiv.org/html/2510.06265v1) |
| 13 | JSONSchemaBench: Evaluating Constrained Decoding | 2024 | [OpenReview](https://openreview.net/forum?id=FKOaJqKoio) |
| 14 | Role-playing Prompt Framework: Generation and Evaluation | 2024 | [arXiv:2406.00627](https://arxiv.org/pdf/2406.00627) |

### 公式ドキュメント・技術ブログ

| タイトル | 発行元 | リンク |
|---|---|---|
| Contextual Retrieval | Anthropic 2024 | [anthropic.com](https://www.anthropic.com/news/contextual-retrieval) |
| Claude Code Best Practices | Anthropic | [code.claude.com](https://code.claude.com/docs/en/best-practices) |
| Claude Code Sub-Agents | Anthropic | [code.claude.com](https://code.claude.com/docs/en/sub-agents) |
| Best Practices for Prompt Engineering | Anthropic | [claude.com](https://claude.com/blog/best-practices-for-prompt-engineering) |
| Cross-Encoder Reranking +40% Accuracy | ailog.fr 2025 | [ailog.fr](https://app.ailog.fr/en/blog/news/reranking-cross-encoders-study) |
| RAG Evaluation Complete Guide 2025 | Maxim AI | [getmaxim.ai](https://www.getmaxim.ai/articles/rag-evaluation-a-complete-guide-for-2025/) |
| Ultimate Guide to Reranking Models 2026 | ZeroEntropy | [zeroentropy.dev](https://zeroentropy.dev/articles/ultimate-guide-to-choosing-the-best-reranking-model-in-2025/) |
