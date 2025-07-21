# Bill Auto Download

## プロジェクト概要
個人経営者・中小企業向けの請求書自動ダウンロードシステム

## 主な機能
- ユーザー認証
- 請求書サイト管理
- スクレイピング基盤

## 開発方針
- モジュラーデザイン
- セキュリティ重視
- robots.txt準拠

## 今後の開発予定
- 多様なECサイト対応
- AI支援スクレイピング
- 電子帳簿保存法対応

## セットアップ手順
1. リポジトリをクローン
```bash
git clone https://github.com/ユーザー名/BillAutoDownload.git
```

2. 仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

4. データベースの移行
```bash
python manage.py migrate
```

5. 開発サーバーの起動
```bash
python manage.py runserver
2f40a86 (初回プッシュ)
