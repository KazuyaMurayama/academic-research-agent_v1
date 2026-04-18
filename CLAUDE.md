# Academic Research Agent — CLAUDE.md

論文サーチ＆エビデンスベースレポート自動生成システム。

> **詳細ルールは各参照先ファイルを読むこと。このファイルは最小限に保つ。**

---

## 🚀 セッション開始時の必須手順（毎回）

1. `FILE_INDEX.md` を Read → プロジェクト全体のファイル構造を把握
2. `tasks.md` を Read → 未完了タスク・優先度を確認
3. `reports/INDEX.md` を Read → 既存レポートを確認（重複調査防止）

---

## 📋 回答の基本ルール

1. **回答冒頭にプロンプト要約を必ず明記**してから本題に入る
2. 論理的・客観的・事実ベース（おべっか・楽観コメント禁止）
3. 意外な点・反直感的な情報は強調（太字・⚠️等）
4. ユーザーに判断を求めるときは選択肢＋推奨案を提示
5. Claude Code側でタスク実行し、ユーザー側タスクを最小化
6. セッション継続困難になったら、その旨＋新セッション用引き継ぎプロンプトを提示

---

## 📌 最重要ルール（省略禁止）

### Git
- **ブランチ作成禁止**: `git checkout -b` / `git branch <name>` は実行しない
- **全成果物は master に push**: `git push origin HEAD:master`
- 詳細 → `.claude/rules/git-rules.md`

### レポート
- 保存先: `reports/YYYY-MM-DD_{英語スラグ}.md`（gitignore対象外）
- push後: **Markdownハイパーリンク形式**でユーザーに提示（URL直貼り禁止）
  - 形式: `[📄 レポートを開く（GitHub）](https://github.com/KazuyaMurayama/academic-research-agent_v1/blob/master/reports/{ファイル名})`
  - **ブランチ名は常に `master`**（セッション跨ぎで確実にアクセス可能）
- `reports/INDEX.md` を毎回更新（IDは R001〜連番、次は `R025`）
- 詳細 → `.claude/rules/output-rules.md`

### タスク管理
- `tasks.md` を常に最新状態に保つ（完了時に即更新・コミット）

### モデル使い分け
- 計画・高度な論理推論 → **Opus**
- 実行・大部分のステップ → **Sonnet**
- 詳細 → `.claude/rules/model-selection.md`

---

## 🛠️ スキル（スラッシュコマンド）

| コマンド | 用途 | 参照先 |
|---|---|---|
| `/research テーマ` | フル論文サーチ＆レポート生成（5フェーズ） | `.claude/skills/research/SKILL.md` |
| `/research-quick テーマ` | 簡易版（検索→即レポート） | `.claude/skills/research-quick/SKILL.md` |
| `/search-only テーマ` | 論文リスト取得のみ | `.claude/skills/search-only/SKILL.md` |

---

## ⚙️ 技術制約（最小限）

- Semantic Scholar API: タイムアウト頻発 → フォールバック: `collect_no_ss.py`
- arXiv API: リクエスト間隔3秒以上
- 論文は10本ずつバッチ処理（コンテキスト窓対策）
- `outputs/` はgitignore済み → `reports/` への保存が必須
- Notion連携: レポート生成後に自動保存可（`src/notion_client.py` / MCP: notionApi）
