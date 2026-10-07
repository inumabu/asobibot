"""Environment-based application configuration."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    discord_token: str
    log_level: str = "INFO"


def load_settings() -> Settings:
    """Load and validate settings needed to start the bot."""
    token = os.getenv("DISCORD_TOKEN", "").strip()
    if not token:
        raise RuntimeError("DISCORD_TOKEN 環境変数を設定してください。")
    return Settings(
        discord_token=token,
        log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
    )
