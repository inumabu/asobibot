# 🎲 AsobiBot

Python と discord.py で作る日本語の遊び系 Discord Bot。

## 🎮 コマンド

- `/omikuji` — 今日の運勢
- `/dice` — 2〜1000面、1〜20個のサイコロ
- `/janken` — BOTとじゃんけん
- `/quiz` — 4択クイズ

## 🚀 セットアップ

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -e .
cp .env.example .env
# PowerShell: Copy-Item .env.example .env
python bot.py
```

`.env` の `DISCORD_TOKEN` は実際のトークンへ置き換え、GitHub へ公開しないでください。Bot には必要最小限の権限だけを付与します。

## 🧩 実装方針

Discord 依存のコマンド層と、テストしやすいゲームロジック層を分離します。トークンは `.env` からのみ読み込み、ログや例外に出力しません。

## 🧪 検証

一括検証（テスト・Lint・Build）:

```sh
python scripts/verify.py
```

```bash
python -m pip install -r requirements-dev.txt
python -m pip install -e .
ruff check .
pytest -q
python -m compileall -q bot.py src test_bot.py
```

## 📚 文書

- [アーキテクチャ](docs/architecture.md)
- [コマンド仕様](docs/commands.md)
- [開発ガイド](DEVELOPMENT.md)
- [貢献ガイド](CONTRIBUTING.md)
- [テスト方針](TESTING.md)
- [セキュリティ](SECURITY.md)

## 📄 ライセンス

AsobiBot は [MIT License](LICENSE) のもとでライセンスされています。

### 📦 第三者ライブラリ

AsobiBot は第三者ライブラリを利用しています。各ライブラリには、それぞれのライセンス条件が適用されます。

- [discord.py](https://github.com/Rapptz/discord.py) — MIT License
- [python-dotenv](https://github.com/theskumar/python-dotenv) — BSD-3-Clause

開発・テスト用途では、以下のライブラリも利用しています。

- [pytest](https://github.com/pytest-dev/pytest) — MIT License
- [Ruff](https://github.com/astral-sh/ruff) — MIT License
- [build](https://github.com/pypa/build) — MIT License

詳細は [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) を参照してください。
