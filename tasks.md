# Tasks — Academic Research Agent

> **新セッション開始時は必ずこのファイルを読んで未完了タスクを確認すること。**
> 完了したタスクは即座にステータス更新 → コミット。

---

## 🔄 進行中

| ID | タスク | ステータス | 開始日 | 担当モデル | 成果物 |
|---|---|---|---|---|---|
| T009 | R027: 風邪介入エビデンス評価レポート作成 | 進行中 | 2026-04-30 | Opus+Sonnet | `reports/2026-04-30_common-cold-interventions-evidence.md` |

---

## ⏳ 未着手

なし

---

## ✅ 完了済み（直近）

| ID | タスク | 完了日 | 担当モデル | 成果物 |
|---|---|---|---|---|
| T001 | 全ブランチからreports/へレポート統合（R001〜R023） | 2026-04 | Sonnet | `reports/` 23本 |
| T002 | 内臓脂肪レポートに期間正規化分析（Section 14）追加 | 2026-04 | Sonnet | `reports/2026-03-28_visceral-fat-reduction.md` |
| T003 | GitHubハイパーリンクルールをCLAUDE.md・スキルに追記 | 2026-04 | Sonnet | `CLAUDE.md`, `SKILL.md` |
| T004 | 花粉症・黄砂×サプリvs薬 レポート作成（R024） | 2026-04-13 | Sonnet | `reports/2026-04-13_hayfever-supplements-vs-drugs.md` |
| T005 | 小児便秘レポートにマンナンごはんvsさつまいも追記（Section 11） | 2026-04-13 | Sonnet | `reports/2026-03-30_pediatric-constipation-fiber.md` |
| T006 | masterへの全ファイル統合・リポジトリ整備 | 2026-04-13 | Sonnet | `master` ブランチ |
| T007 | 胃がん予防介入の包括的スコアリングレポート作成（R025） | 2026-04-21 | Opus+Sonnet | `reports/2026-04-21_gastric-cancer-prevention-scoring.md` |
| T008 | 40代男性サプリ＆処方薬全レジメンのリスク分析レポート（R026） | 2026-04-28 | Sonnet | `reports/2026-04-28_supplement-drug-risk-analysis.md` |
| T009 | 免疫力強化v2レポート作成（R027）: 16介入定量スコアリング、Opus計画+Sonnet実行 | 2026-04-28 | Opus+Sonnet | `reports/2026-04-28_immunity-boost-v2.md` |

---

## 📋 タスク管理ルール

### 新セッション開始時
1. このファイル（`tasks.md`）を Read
2. 「進行中」「未着手」を確認し、前セッションの継続作業を把握
3. `FILE_INDEX.md` を Read → ファイル構造を把握
4. `reports/INDEX.md` を Read → 既存レポートを確認

### タスク追加時
- 「未着手」セクションに追加（ID: T001〜連番、次は `T010`）
- 担当モデル（Opus/Sonnet）を明記
- 期待成果物を具体的に記述

### タスク実行時
- 「進行中」に移動
- サブタスクに分割してチェックポイントを設定

### タスク完了時
- 「完了済み」に移動（完了日・成果物リンクを記入）
- 即座にコミット: `git add tasks.md && git commit -m "docs: tasks.md更新 T00X完了"`
- masterへ push: `git push origin HEAD:master`

---

## 📌 常時維持タスク（定常業務）

| 業務 | タイミング | 方法 |
|---|---|---|
| `reports/INDEX.md` 更新 | 新レポート作成時 | 次のIDは `R026` |
| `FILE_INDEX.md` 更新 | 新ファイル追加時 | ファイル種別・説明を追記 |
| masterへのpush | 全コミット後 | `git push origin HEAD:master` |
