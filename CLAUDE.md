# Academic Research Agent

論文サーチ＆エビデンスベースレポート自動生成システム。

## プロジェクト概要
- ユーザーの研究テーマに対して、複数の学術APIから論文を自動収集
- Claude自身が論文のスクリーニング・分析・統合を実行
- PRISMA準拠の構造化レポートを自動生成

## アーキテクチャ原則
1. **Pythonの役割はデータ収集のみ**: API呼び出し、JSON保存、重複排除
2. **分析・統合・レポート生成はClaude自身が実行**: LLMの推論力を直接活用
3. **中間ファイルによるフェーズ間連携**: outputs/{session_id}/ に各フェーズの成果物を保存

## 利用可能なスキル（スラッシュコマンド）
- `/research テーマ` : フル論文サーチ＆レポート生成（5フェーズ）
- `/research-quick テーマ` : 簡易版（検索→即レポート）
- `/search-only テーマ` : 論文リスト取得のみ

## 技術スタック
- Python 3.10+
- httpx（非同期HTTP）, xmltodict（arXiv XML解析）
- python-dotenv（環境変数）

## コードスタイル
- type hints必須
- docstring必須（Google style）
- エラーハンドリング: API障害時は他APIで継続（フォールバック）

## 重要な制約
- Semantic Scholar API: 100 requests/5min（APIキーなし）
- arXiv API: リクエスト間隔3秒以上
- コンテキスト窓対策: 論文は必ず10本ずつバッチ処理する

## Notion連携
- レポート生成後、自動的にNotionデータベースに保存（毎回自動。「skip Notion」で個別スキップ可能）
- MCP Server: notionApi（user scope で登録済み）
- Database ID: .env の NOTION_DATABASE_ID を参照
- フォールバック: `python src/notion_client.py`（MCP利用不可時のみ）
- 詳細ルール: ~/.claude/CLAUDE.md の「Notion Report Output Rules」を参照

## 進捗報告ルール

長時間タスク（/research等）の実行中、以下のタイミングで進捗を報告する:

1. **フェーズ完了時**: 各フェーズ（Phase 1-5）完了時に短いサマリーを表示
2. **10分経過時**: 10分以上経過したら中間進捗を表示（処理中の論文数、完了率等）
3. **エラー発生時**: 即座にエラー内容と回復策を報告

進捗報告フォーマット:

```
⏳ 進捗報告 [{現在のPhase}/{全Phase数}]
━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 完了: {完了したフェーズ一覧}
🔄 実行中: {現在のフェーズと詳細}
⏳ 待機中: {未実行のフェーズ}
📊 統計: 論文{N}件処理済み / 推定残り時間{M}分
━━━━━━━━━━━━━━━━━━━━━━━━━━
```
