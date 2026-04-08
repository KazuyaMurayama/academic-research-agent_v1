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
   - エビデンスギャップ: 未解明の問題を特定
   - テーマ別マッピング: 知見をサブテーマごとに整理
2. outputs/{session_id}/04_synthesis.md に保存
3. ユーザーに表示: 主要発見トップ3のサマリー

### Phase 5: レポート生成（Report Generation）
1. templates/report_template.md に従い、最終レポートを生成
2. レポート構成:
   1. Executive Summary（300字以内の研究全体の結論）
   2. 研究背景と目的
   3. 検索方法論（PRISMA準拠: 検索式・対象DB・フロー図テキスト版）
   4. エビデンス概要（テーマ別整理）
   5. 比較テーブル（Phase 4で生成したもの）
   6. 詳細分析（Tier 1論文の個別分析）
   7. エビデンスギャップと今後の研究課題
   8. 実務への示唆（Practical Implications）— ビジネスパーソン向け
   9. 参考文献（APA 7th形式、URLリンク付き）
   10. 付録: PRISMAフローダイアグラム、全スクリーニング結果
3. outputs/{session_id}/05_report.md に保存
4. **【毎回必須】reports/ へコピーして git push する**:
   - ファイル名: `reports/YYYY-MM-DD_{テーマの短い英語スラグ}.md`（例: `reports/2026-04-06_four-hour-workday.md`）
   - `git add reports/{filename}` → `git commit -m "research: {テーマ} レポート"` → `git push -u origin {current-branch}`
   - GitHub URL を生成: `https://github.com/KazuyaMurayama/academic-research-agent_v1/blob/{branch}/reports/{filename}`
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

⚠️ エビデンスギャップ:
- {ギャップ1}

🔗 [📄 レポートを開く（GitHub）]({GitHub URL})

📁 ローカル成果物:
- レポート全文: outputs/{session_id}/05_report.md
- 検索戦略: outputs/{session_id}/01_search_plan.md
- エビデンス統合: outputs/{session_id}/04_synthesis.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
