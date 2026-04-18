# Git操作ルール

## ❌ 禁止事項（厳守）

- **ブランチ作成は一切禁止**: `git checkout -b` / `git switch -c` / `git branch <name>` は実行しない
- ユーザーの明示的な指示がない限り、現在のブランチを変更しない
- `git push --force` は原則禁止（force-with-leaseも事前確認必須）

## ✅ 許可操作

- 現在のブランチ上での `git add`, `git commit`, `git push`
- `git status`, `git log`, `git diff` などの読み取り操作
- `git pull` による最新化
- `git push origin HEAD:master`（masterへの統合用）

## 📌 push先のルール

- **全成果物は master に push する**
- デフォルトコマンド: `git push origin HEAD:master`
- または `git push -u origin master`（masterをチェックアウトしている場合）

## 📦 コミット粒度

- タスクを細かいサブタスクに分割し、各ステップ完了ごとにコミット
- コミットメッセージ形式: `<type>: <日本語説明>`
  - type例: `research`, `feat`, `fix`, `docs`, `refactor`
- コミット末尾に必ずセッションURLを含める

## 🚀 タイムアウト対策

- 長時間処理（論文収集・大量ファイル操作）は5サブタスク以上に分割
- 各サブタスク完了時にコミット・保存（中断リスクを最小化）
- API呼び出しは1回あたり最大100件、バッチ処理で分割
