# 熊野市花火大会コンプリートガイド (Webアプリ)

## 概要
熊野市の花火大会に特化した観光客向けWebアプリ。インタラクティブマップ、店舗詳細、リアルタイム情報を提供。

## 機能
- インタラクティブマップ（Google Maps API）
- 店舗詳細システム
- リアルタイム情報（花火プログラム、交通規制、駐車場満空）
- モバイルファーストUI/UX
- カテゴリ別フィルターと検索機能

## 技術スタック
- Python + Flask
- Google Maps API
- HTML/CSS/JavaScript (Bootstrap)
- SQLiteデータベース

## インストール
1. Python 3.8+ をインストール
2. `pip install -r requirements.txt`
3. Google Maps APIキーを `config.py` に設定
4. `python init_db.py` でサンプルデータを投入
5. `python run.py` で起動

## デプロイ
### Herokuへのデプロイ
1. Herokuアカウントを作成
2. Heroku CLIをインストール
3. `heroku create your-app-name`
4. `git push heroku main`
5. 環境変数で `GOOGLE_MAPS_API_KEY` を設定

### Vercelへのデプロイ
1. Vercelアカウントを作成
2. `vercel --prod`
3. 環境変数を設定

## 開発ロードマップ
1. ✅ プロジェクト計画と設計
2. ✅ 環境設定（Python, Flask）
3. ✅ 基本Flaskアプリセットアップ
4. ✅ Google Maps API統合
5. ✅ データベース設計
6. ✅ フロントエンド開発
7. ✅ 機能実装
8. ✅ テスト
9. 🔄 デプロイ