---
name: research
description: >
  ユーザーの研究テーマに対して体系的な論文サーチを実行し、
  エビデンスベースの構造化レポートを自動生成する。
  「論文を調べて」「〜について研究して」等のリクエストで自動起動。
---

# /research スキル: フル論文サーチ＆レポート生成

ユーザーが研究テーマを指定したら、以下の5フェーズを順次実行する。
各フェーズ完了時に短い進捗サマリーをユーザーに表示すること。

## 【必須】実行前チェック: 過去レポートの確認

**Phase 1 の前に必ず `reports/INDEX.md` を Read して**、類似テーマのレポートが存在しないか確認すること。
- 既存レポートで対応できる場合: そのレポートをユーザーに提示し、追加調査の要否を確認する
- 類似テーマがある場合: そのレポートを出発点として差分調査のみ行う
- 完全に新規テーマの場合: 通常通り5フェーズを実行する

## 実行手順

### Phase 1: 検索戦略立案（Query Planning）
1. ユーザーのテーマを分析し、以下を生成する:
   - メイン検索クエリ（英語、3〜5個、同義語・関連概念を網羅）
   - 除外キーワード（ノイズ回避用）
   - 推奨年範囲（デフォルト: 過去5年）
   - 分野判定（CS/Medical/Business等 → 使用APIの決定）
2. outputs/{session_id}/01_search_plan.md に保存
3. ユーザーに表示: 検索戦略のサマリー（クエリ一覧と予想論文数）

### Phase 2: 論文収集（Paper Collection）
1. 以下を実行:
   ```
   python src/collectors/paper_collector.py \
     --queries "query1" "query2" "query3" \
     --years 2020-2025 \
     --max-results 100 \
     --output outputs/{session_id}/02_raw_papers.json
   ```
2. 収集完了後、重複排除済みの論文数をユーザーに報告
3. ユーザーに表示: 「{N}件の論文を{M}つのAPIから収集しました（重複排除後: {K}件）」

### Phase 3: スクリーニング＆品質評価（Screening）
1. 02_raw_papers.json を10本ずつバッチで読み込む（コンテキスト窓対策）
2. 各論文を以下の基準で評価:
   - 関連性: テーマとの関連度（High/Medium/Low）
   - 影響度: 被引用数 × 出版年の新しさ
   - エビデンスレベル: Oxford CEBM基準（メタ分析 > RCT > コホート > ...）
   - 研究デザイン: 自動識別
3. 分類結果:
   - Tier 1（コア論文）: 5〜10本（詳細分析対象）
   - Tier 2（補助論文）: 10〜20本（参照用）
4. outputs/{session_id}/03_screening.md に保存
5. ユーザーに表示: Tier 1論文リスト（著者・年・タイトル・選定理由）

### Phase 4: エビデンス統合（Evidence Synthesis）
1. Tier 1論文について以下を実行:
   - 個別要約: 目的・方法・主要結果・限界の4要素
   - クロス分析: 論文間の一致点と矛盾点を特定
   - 比較テーブル生成: | 著者(年) | 研究デザイン | 対象(N) | 主要結果 | エビデンスレベル |
   - 実行性評価: 各施策の所要時間・難易度・専門家要否・続けやすさを整理（実行性スコア用）
   - 具体的なやり方の抽出: 各施策の手順・ステップ・初心者向けの実行例を収集（★レポートで最重要）
   - テーマ別マッピング: 知見をサブテーマごとに整理
2. outputs/{session_id}/04_synthesis.md に保存
3. ユーザーに表示: 主要発見トップ3のサマリー

### Phase 5: レポート生成（Report Generation）
1. `templates/report_template.md` と **`.claude/rules/output-rules.md`「🎯 レポート構成テンプレート（実践重視）」に必ず従う**。レポートは研究用でなく「ユーザーが実践して成果を出すため」。品質＝①早く読める ②早く効果的なものを選べる ③簡単に実行できる。
2. レポート構成（**実践重視・この順序を厳守**）:
   1. **エグゼクティブサマリー**（結論先出し：目的別の推奨＋反直感的な警告）
   2. **目的・スコープ・読み方**（短く。評価軸の定義のみ）
   3. **スコアリング比較テーブル**（必ず序盤・「2」の直後。列名は **「効果量／エビデンス強度／実行性」**）
   4. **目的別クイック選択／推奨プロトコル**（読者の状況別にどれを選ぶか）
   5. **施策別 実践ガイド**（**A・Bランクまたはトップ5〜7のみ**）。各施策＝機序1〜2文／効果量2〜3個／エビデンス強度1行／**★具体的なやり方（ステップ・所要時間・例。初心者が迷わず実行できるレベル）**／注意点
   6. （背景理論・科学的基盤があれば **後方**に。読みたい人だけ）
   7. **注意点・安全性・免責**
   8. **参考文献**（APA・URL付き）
   - ❌ **「エビデンスギャップ／今後の研究課題」セクションは作らない（常に不要）**
   - C・D／非推奨・研究段階の施策は詳細を書かず **1行サマリー表に集約**（重要な警告のみ残す）

2.5. **【完成前チェックリスト・毎回必須】** 以下を全て満たすまでレポートを完成としない:
   - [ ] スコア比較表が序盤（目的説明の直後）にある
   - [ ] スコア表の列名が「効果量／エビデンス強度／**実行性**」になっている（「実行」は不可）
   - [ ] 「エビデンスギャップ／今後の研究課題」セクションが**存在しない**
   - [ ] 詳細ガイドはA・Bランク（またはトップ5〜7）に限定。C/Dは1行表に集約
   - [ ] 各施策に**★具体的なやり方（ステップ・所要時間・例）**があり、初心者が迷わず実行できる
   - [ ] 機序は1〜2文／効果量は2〜3個／エビデンス強度は1行に収まっている
   - [ ] 冒頭に目次と「お急ぎの方へ」の読む順ガイドがある
   - 検証コマンド例: `grep -c "エビデンスギャップ\|今後の研究課題" reports/対象.md`（0であるべき）／`grep -c "実行性" reports/対象.md`（1以上）
3. outputs/{session_id}/05_report.md に保存
4. **【毎回必須】reports/ へコピーして git push する**:
   - ファイル名: `reports/YYYY-MM-DD_{テーマの短い英語スラグ}.md`（例: `reports/2026-04-06_four-hour-workday.md`）
   - `git add reports/{filename}` → `git commit -m "research: {テーマ} レポート"` → `git push origin master`（403時はCLAUDE.mdの自動フローに従う）
   - GitHub URL を生成: `https://github.com/KazuyaMurayama/academic-research-agent_v1/blob/master/reports/{filename}`
   - **⚠️ 推定30,000文字超の場合は1回のWriteで生成せず、`.claude/rules/timeout-prevention.md` の Option C（スケルトン先出し → バッチEdit置換）に従うこと**
   - この手順を省略してはならない。レポートはGitHubからワンクリックで開けることが必須条件。
5. **【毎回必須】`reports/INDEX.md` を更新する**:
   - 次のIDを確認（既存の最大ID + 1）
   - 一覧テーブルに1行追加
   - 詳細セクションに1ブロック追加（タイトル・ファイル名・テーマ・一言サマリー・主要発見・タグ・エビデンスレベル）
   - タグ索引を更新
   - `git add reports/INDEX.md` → 前のコミットにまとめるか個別コミット
6. ユーザーへの最終提示:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 論文サーチレポート完成
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
テーマ: {ユーザーのテーマ}
分析論文数: Tier1 {X}本 / Tier2 {Y}本（総検索: {Z}件）
エビデンスレベル: {最も高いレベル}

📋 Executive Summary:
{300字サマリー}

📊 主要発見:
1. {発見1}
2. {発見2}
3. {発見3}

⚠️ 反直感的な警告:
- {読者が誤解しがちな点・やってはいけないこと}

🔗 [📄 レポートを開く（GitHub）]({GitHub URL})

📁 ローカル成果物:
- レポート全文: outputs/{session_id}/05_report.md
- 検索戦略: outputs/{session_id}/01_search_plan.md
- エビデンス統合: outputs/{session_id}/04_synthesis.md
- Notion: {Notion_page_URL}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Phase 6: Notion保存（自動実行）
※ ユーザーが「Notionに保存しない」「skip Notion」等と指示した場合はスキップ

1. 05_report.md からExecutive Summaryを抽出（300字以内）→ Summaryプロパティ
2. 研究テーマに基づいてTagsを自動選択（タグマスターリストから2-5個）:
   - **ビジネス・コンサル系**: ai-strategy, ai-implementation, dx-transformation, consulting-methodology, client-communication, pricing-strategy, freelance-ops, market-analysis, sales-strategy, project-management
   - **テクニカル系**: python, claude-api, prompt-engineering, mcp, automation, data-analysis, backtesting, web-scraping, github-actions, react-firebase
   - **ドメイン知識**: finance-investment, real-estate, tax-japan, health-optimization, skincare-dermatology, childcare-japan, marathon-fitness
   - **メタ・ナレッジ管理**: knowledge-base, research-summary, case-study, how-to, decision-log, lesson-learned
   - 必ず `research-summary` を含め、テーマに該当するドメイン系タグを1つ以上選ぶ
3. Notion MCPツール（notionApi の API-post-page）を使用してデータベースにページを作成:
   - 名前: 「{YYYY/MM/DD} {研究テーマ} - 論文サーチレポート」
   - Tags: 自動選択したタグ
   - Source: `claude-code`
   - Date: 実行日（ISO 8601形式）
   - Status: `draft`
   - Summary: Executive Summary テキスト
   - ページ本文: レポートのMarkdownをNotionブロック（heading_2, heading_3, paragraph, bulleted_list_item, numbered_list_item, code）に変換して挿入
4. Notion MCP が利用不可の場合:
   - `python src/notion_client.py --session-id {session_id}` でフォールバック投稿を試行
   - それも失敗した場合: ローカル保存のみで完了とし、エラーを報告
5. outputs/{session_id}/06_notion_url.txt にNotion URLを保存
6. ユーザーに表示: 「📝 Notionに保存しました: {Notion_page_URL}」
