"""AsobiBot entry point. Keep startup concerns here only."""

from src.application import create_bot
from src.config import load_settings
from src.logging_config import configure_logging


def main() -> None:
    settings = load_settings()
    configure_logging(settings.log_level)
    bot = create_bot()
    bot.run(settings.discord_token, log_handler=None)


if __name__ == "__main__":
    main()
