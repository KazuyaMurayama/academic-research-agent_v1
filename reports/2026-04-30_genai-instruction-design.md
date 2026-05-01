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

> 「まず考えて」と一言加えるだけで推論精度が大幅向上する手法。
> **効果**: 数学・論理タスクで +15〜40% | **証拠** ★★★★ | **コスト** ×1.5〜2 | **実装** ★

#### いつ使うか

**使うべき場面**:
- 数学・論理・コード生成・因果推論など、ステップを踏む必要があるタスク
- 「なぜそう判断したか」の根拠が必要な場面（監査・説明責任）
- モデルが答えを間違えているが、手順は分かっていそうな場合

**効果が薄い場面**:
- 単純な事実検索・翻訳・分類（追加コストのみかかる）
- **7B以下の小モデル**（推論ステップが誤りを増幅するリスクあり）

#### 実装（コピペ即使用）

```python
# ── Zero-shot CoT（最も簡単。1行追加するだけ）──
system = "あなたは優秀なアシスタントです。"
user = f"""
{ユーザーの質問}

ステップごとに考えてから回答してください。
"""

# ── Few-shot CoT（精度重視。例を2〜3件添付）──
few_shot_examples = """
例1:
Q: 花子は15個のリンゴを持っています。3人に均等に配ると1人あたり何個?
A: まず15 ÷ 3 = 5を計算します。よって1人あたり5個です。

例2:
Q: 時速60kmで2時間走ると何km?
A: 距離 = 速度 × 時間 = 60 × 2 = 120kmです。
"""

prompt = f"""
{few_shot_examples}

Q: {ユーザーの質問}
A: """
```

#### 改善のコツ

- **「ステップごとに」より「まず問題を分解して」の方が複雑なタスクに効く**
- Few-shot例は答えより**推論過程**を充実させる（答えだけ書いた例はCoTの意味なし）
- XML形式で思考と回答を分離すると後処理が楽: `<thinking>…</thinking><answer>…</answer>`

#### 落とし穴

- ⚠️ **過剰なステップ指示はかえって冗長になる**。「10ステップで考えて」などの数値指定は逆効果
- ⚠️ **Self-Consistency（多数決型）はコスト×5〜10の割に追加効果が限定的**。通常のFew-shot CoTで十分

#### 出典

[Wei et al. 2022, NeurIPS — Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)

---

### M-02 Few-shot + 例選定最適化

> 「こういう例でやって」と具体例を数件見せることで、モデルがタスクパターンを即座に理解する手法。
> **効果**: タスク精度 +10〜50%（例の質次第） | **証拠** ★★★★ | **コスト** ×1〜1.5 | **実装** ★

#### いつ使うか

**使うべき場面**:
- 出力フォーマットを固定したい（JSONキー名・表形式・特定の言い回し）
- ドメイン固有の判断基準があり、言葉で説明しにくい
- Zero-shotで精度が不安定な分類・変換・抽出タスク

**効果が薄い場面**:
- 例が多すぎる（over-prompting）とトークン消費の割に精度が下がる。**3〜5件が最適**
- 例の質が低い場合（間違った例を入れると間違ったパターンを学習する）

#### 実装（コピペ即使用）

```python
# ── 基本形：感情分類の例 ──
examples = [
    {"input": "最高の映画だった。また見たい！", "output": "ポジティブ"},
    {"input": "全然おもしろくなかった。時間の無駄。", "output": "ネガティブ"},
    {"input": "普通だった。特に印象なし。", "output": "ニュートラル"},
]

def build_few_shot_prompt(examples, new_input):
    shots = "\n\n".join(
        f"入力: {ex['input']}\n出力: {ex['output']}"
        for ex in examples
    )
    return f"{shots}\n\n入力: {new_input}\n出力:"

# ── 出力形式固定の例（JSON構造化抽出）──
format_examples = """
入力: 「田中太郎さん（35歳）が2024年3月に入社しました。」
出力: {"name": "田中太郎", "age": 35, "join_date": "2024-03"}

入力: 「山田花子、42歳、2025年1月から勤務開始。」
出力: {"name": "山田花子", "age": 42, "join_date": "2025-01"}
"""
```

#### 改善のコツ

- **例の順番が重要**。最後の例がモデルに最も影響する → 最も典型的な例を最後に置く
- **難しい例（境界ケース）を1件含める**と精度が安定する
- 例が3件以下でも十分な場合が多い。まず3件試してから増減する

#### 落とし穴

- ⚠️ **例の選び方がランダムだと効果がバラつく**。タスクを代表する例を意図的に選ぶ
- ⚠️ **例に誤りが混ざると大幅に精度低下**。Few-shotを追加しても改善しない場合は例を疑う

#### 出典

[Brown et al. 2020 — Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165)、
[The Few-shot Dilemma: Over-prompting LLMs (arXiv:2509.13196)](https://arxiv.org/html/2509.13196v1)

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

> 出力をJSONスキーマに強制的に縛ることで、パース失敗・フォーマット崩れをほぼゼロにする手法。
> **効果**: スキーマ適合率 99.5% | **証拠** ★★★★ | **コスト** ×1（追加コストなし） | **実装** ★

#### いつ使うか

**使うべき場面**:
- アプリケーションコードでLLM出力をパースする全ケース（APIレスポンス・DB保存・後続処理）
- 必須フィールドの有無が重要な業務フロー
- ストリーミング出力で部分的なJSONを扱う場合

**効果が薄い場面**:
- 自由記述（エッセイ・説明文）には不要。制約が冗長になるだけ

#### 実装（コピペ即使用）

```python
import anthropic
import json
from pydantic import BaseModel

client = anthropic.Anthropic()

# ── 方法1: tool useでスキーマ強制（最確実）──
tools = [{
    "name": "extract_person",
    "description": "テキストから人物情報を抽出する",
    "input_schema": {
        "type": "object",
        "properties": {
            "name":     {"type": "string", "description": "氏名"},
            "age":      {"type": "integer", "description": "年齢"},
            "role":     {"type": "string", "enum": ["管理職", "一般職", "役員"]},
        },
        "required": ["name", "age"]
    }
}]

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "tool", "name": "extract_person"},
    messages=[{"role": "user", "content": "田中部長（45歳）が退職します。"}]
)
result = response.content[0].input  # 確実にスキーマ準拠

# ── 方法2: プロンプト + JSONパース（シンプルな場合）──
prompt = """以下のテキストから情報を抽出し、必ずJSON形式で返してください。
余計な説明や```json```記法は不要。JSONのみ返すこと。

スキーマ:
{"name": "string", "age": int, "department": "string"}

テキスト: {text}"""
```

#### 改善のコツ

- **tool useのほうがプロンプト指示よりも確実**。`tool_choice`で特定ツールを強制指定
- Pydanticモデルを定義しておくと `model_validate(result)` で型安全に使える
- `required`フィールドを最小限にする（不要なフィールドの強制はエラーの元）

#### 落とし穴

- ⚠️ **JSONモードでも`null`や空文字が入ることがある**。バリデーションは別途実施
- ⚠️ **enumの選択肢が多すぎるとモデルが迷う**。5個以下を目安にする

#### 出典

[JSONSchemaBench: Evaluating Constrained Decoding (OpenReview 2024)](https://openreview.net/forum?id=FKOaJqKoio)、
[Anthropic Tool Use Documentation](https://docs.anthropic.com/en/docs/tool-use)

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
