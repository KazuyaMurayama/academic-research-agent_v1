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

## 6. ドキュメント日付ルール
レポート系 .md 新規作成時は H1直下に `作成日: YYYY-MM-DD` / `最終更新日: YYYY-MM-DD` 必須。更新時は最終更新日のみ書き換え。除外: README / CLAUDE.md / FILE_INDEX / tasks.md / CHANGELOG / LICENSE / reports/INDEX.md。

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
