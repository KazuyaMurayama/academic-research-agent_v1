# Academic Research Agent — Claude Code 運用ルール

論文サーチ＆エビデンスベースレポート自動生成システム。

> **本ファイルは VSCode版 / Web版 Claude Code（claude.ai）の両方で本リポジトリの単独完結ガイド**。
> Web版はグローバル `~/.claude/CLAUDE.md` を参照しない前提で、本リポの運用に必要な全ルールをここに集約。

---

## 0. リポジトリ前提
- **デフォルトブランチ: `master`**（他リポジトリは `main` だが本リポは歴史的経緯で `master`）
- 以降、本ファイル内 URL・コマンドは `master` ブランチを基準とする

---

## 🚀 1. セッション開始時の必須手順（毎回）

1. `FILE_INDEX.md` を Read → プロジェクト全体のファイル構造を把握
2. `tasks.md` を Read → 未完了タスク・優先度を確認
3. `reports/INDEX.md` を Read → 既存レポートを確認（重複調査防止）

> 詳細ルールは `.claude/rules/` 配下の各参照先ファイルを読むこと。本ファイルは最小限に保つ。

---

## 2. 関連リポジトリ
| リポ | 役割 |
|---|---|
| [KazuyaMurayama/deep-research](https://github.com/KazuyaMurayama/deep-research) | 汎用ディープリサーチエンジン |
| [KazuyaMurayama/insider-oracle](https://github.com/KazuyaMurayama/insider-oracle) | 専門家視点での知見抽出 |
| [KazuyaMurayama/grid_research_v1](https://github.com/KazuyaMurayama/grid_research_v1) | グリッド型体系リサーチ |

---

## 3. 開発者情報・命名ルール

| 種別 | 表記 | 用途 |
|---|---|---|
| **システム識別子（変更不可）** | `KazuyaMurayama` | GitHub ユーザー名 / URL / `@KazuyaMurayama` |
| **システム識別子（変更不可）** | `kazuya.murayama.21@gmail.com` | git `user.email` / 連絡先 |
| **表記名（人間として記載する場合）** | **男座員也（Kazuya Oza / おざ かずや）** | ドキュメント本文の著者名 / コミット message 中の自己言及 |

- ドキュメント本文等で開発者名を**人間として**記載する際は **男座員也 / Kazuya Oza** を使用
- 「Murayama」「村山」「Otokoza」「おとこざ」を**表記名**として誤用しない（システム識別子としての `KazuyaMurayama` は許容）

---

## 4. ツール実行・Git・ファイル保存
- 確認不要・即実行（事前確認文を出力しない）
- 例外（事前確認必須）: master への `git push --force`、`gh repo delete`
- **ブランチ管理**: デフォルトは master へ直接コミット。ブランチ作成は明示指示時のみ。万一作成した場合は master マージ→削除→push完了で「完了」
- **ファイル保存**: 本リポ内のみ。`C:\Users\user\Desktop` への出力禁止

---

## 5. 成果物報告ルール

| 成果物 | 説明 | リンク |
|---|---|---|
| file.md | 1行説明 | [開く](https://github.com/KazuyaMurayama/academic-research-agent_v1/blob/master/path/to/file.md) |

- Markdownリンク `[表示名](URL)` 形式必須 / `/blob/<実ブランチ>/<実パス>` 形式
- **報告前にURL存在確認**：`Invoke-WebRequest -Uri https://api.github.com/repos/KazuyaMurayama/academic-research-agent_v1/contents/PATH?ref=master -UseBasicParsing` でステータス200確認
- push完了後のみURL生成

---

## ドキュメント命名・日付ルール（v2.0 / 2026-06-03 改訂）

### ファイル名
- `<TOPIC>_YYYYMMDD.md` 形式（**サフィックス・ハイフンなし**）
  - 例: `STRATEGY_REPORT_20260603.md`
- **同日中の追加更新**: `-v2`、`-v3` を追加（例: `STRATEGY_REPORT_20260603-v2.md`）
- **翌日1回目**: v サフィックスをリセット（例: `STRATEGY_REPORT_20260604.md`）

### 表記の区別
- **ファイル名**: ハイフン**なし** `YYYYMMDD`（例: `20260603`）
- **本文中の日付表記**: ハイフン**あり** `YYYY-MM-DD`（例: `2026-06-03`）

### H1直下の日付メタデータ
レポート系 .md 新規作成時は H1直下に必ず記載:
```
作成日: YYYY-MM-DD
最終更新日: YYYY-MM-DD
```
更新時は **最終更新日のみ** 当日付に書き換え（作成日は固定）。

### 対象外（日付サフィックスを入れない）
- README / CLAUDE.md / FILE_INDEX / tasks.md / CHANGELOG / LICENSE / SPEC.md
- `CURRENT_*.md`（常に最新で参照される単一ファイル）
- パイプライン自動生成ファイル（例: `REPORT.md`、`outputs/*.md`）

### 旧形式（廃止・新規禁止）
- ❌ `<TOPIC>_2026-06-03.md`（ハイフン区切り）
- ✅ `<TOPIC>_20260603.md`（**現行ルール**）

---

## 7. Skill 起動ルール

| トリガー | スキル |
|---|---|
| 学術論文・先行研究の調査 | `.claude/skills/research-deep/SKILL.md` |
| 計画立案・実行 | `.claude/skills/sp-writing-plans/SKILL.md` + `sp-executing-plans/SKILL.md` |
| エビデンス品質・引用検証 | `.claude/skills/data-quality-audit/SKILL.md` |
| メタアナリシス・統計検定 | `.claude/skills/ab-test-analysis/SKILL.md` |
| レポート構成・図表 | `.claude/skills/mermaid-agents365/SKILL.md` |
| QC・レビュー・共有前 | `.claude/skills/analysis-qa-checklist/SKILL.md` |
| 成果物の納品・コミット前 | `.claude/skills/sp-verification-before-completion/SKILL.md` |
| インサイト統合 | `.claude/skills/insight-synthesis/SKILL.md` |

---

## モデル使い分け
- メイン: **Claude Fable 5（`claude-fable-5`）** を使用。
  計画・中〜高難易度の実装/分析・全体指揮を担当。
- 実行フェーズ（定型実装・ファイル編集・テスト実行）:
  サブエージェントを `model: "sonnet"` で起動して委譲。
- ※難易度ベースの自動メイン切替は不可。Fable の自動切替は安全性ブロック時の
  Opus 4.8 フォールバックのみ。工程別の使い分けはサブエージェント委譲で行う。
