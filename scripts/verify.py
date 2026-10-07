#!/usr/bin/env python3
"""AsobiBot のローカル検証を一括実行するクロスプラットフォーム runner。"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> None:
    print(f"\n>>> {' '.join(args)}", flush=True)
    executable = sys.executable if args[0] == "python" else args[0]
    subprocess.run([executable, *args[1:]], cwd=ROOT, check=True)


def main() -> int:
    run("python", "-m", "pytest", "-q")
    run("ruff", "check", ".")
    run("python", "-m", "compileall", "-q", "bot.py", "src", "test_bot.py")
    run("python", "-m", "build")
    artifacts = sorted((ROOT / "dist").glob("*"))
    if not artifacts:
        raise SystemExit("dist/ に Build 成果物がありません")
    print("\n✅ AsobiBot のテスト・Lint・Build が完了しました")
    for artifact in artifacts:
        print(f"  - {artifact.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
