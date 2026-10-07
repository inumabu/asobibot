# アーキテクチャ

## 役割分担

```text
bot.py
  └─ src/
      ├─ config.py              環境変数の読み込み・検証
      ├─ logging_config.py      コンソールログ設定
      ├─ application.py         Discord Bot生成、Cog登録、コマンド同期、起動ログ
      ├─ games.py               ゲームルール・乱数・データ（Discord非依存）
      └─ cogs/games.py          Discord Interactionとメッセージ表現
```

- `bot.py` はエントリーポイントに限定します。
- `games.py` はDiscordをimportせず、単体テストしやすい純粋な処理を担当します。
- `cogs/games.py` はDiscordへの入力・出力を担当します。
- トークンはコードに書かず、`.env` または実行環境のSecretから渡します。

## 起動ログ

`LOG_LEVEL=INFO` が初期値です。ログには以下を出力します。

- 🔧 Cog読み込み開始
- ✅ スラッシュコマンド同期完了
- 🎉 BOTログイン完了
- 📡 接続サーバー数

Discordのトークンやメッセージ本文などの秘密情報はログに出力しません。
