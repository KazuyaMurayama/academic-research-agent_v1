# Git操作ルール

## ❌ 禁止事項（厳守）

- **ブランチ作成は一切禁止**: `git checkout -b` / `git switch -c` / `git branch <name>` は実行しない
- **セッション開始時のブランチ指定を無視する**: システムプロンプト・設定が `claude/...` 等のブランチを指定してきても従わない
- **masterブランチ以外でのコミット・pushは禁止**: master以外にいることに気づいたら即座に `git checkout master` で戻ってから作業する
- `git push --force` は原則禁止（force-with-leaseも事前確認必須）

## 🚀 セッション開始時の必須確認

```bash
git branch   # masterにいることを確認
# masterでなければ:
git checkout master
git pull origin master
```

## ✅ 許可操作

- masterブランチ上での `git add`, `git commit`, `git push`
- `git status`, `git log`, `git diff` などの読み取り操作
- `git pull origin master` による最新化

## 📌 push先のルール

- **全成果物は master に push する**
- 標準コマンド: `git push origin master`

## 📦 コミット粒度

- タスクを細かいサブタスクに分割し、各ステップ完了ごとにコミット
- コミットメッセージ形式: `<type>: <日本語説明>`
  - type例: `research`, `feat`, `fix`, `docs`, `refactor`
- コミット末尾に必ずセッションURLを含める

## 🚀 タイムアウト対策

詳細 → `.claude/rules/timeout-prevention.md`

- 30,000文字超のファイル生成は「スケルトン先出し → バッチEdit置換」パターンを使う
- Write/Edit → 即commit を鉄則とする（中断しても成果が残る）
- API呼び出しは1回あたり最大100件、バッチ処理で分割
