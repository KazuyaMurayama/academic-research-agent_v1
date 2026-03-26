---
name: research-quick
description: >
  簡易版の論文サーチ。検索→上位10本で即座にレポート生成。
  「ざっくり調べて」「概要だけ教えて」等のリクエストで自動起動。
---

# /research-quick スキル: 簡易論文サーチ

Phase 1（検索戦略）→ Phase 2（論文収集、上位10本のみ）→ Phase 5（レポート生成）
の3ステップで簡易レポートを生成する。Phase 3-4のスクリーニング・統合分析は省略。
被引用数上位10本をそのままTier 1として扱う。
他の手順は /research スキルに準拠する。

レポート生成後、/research スキルの Phase 6（Notion保存）と同じ手順でNotionに自動保存する。
「skip Notion」等の指示があればスキップ。
