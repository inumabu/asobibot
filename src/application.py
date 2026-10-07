"""Discord client construction and lifecycle hooks."""

import logging

import discord
from discord.ext import commands

from src.cogs.games import GamesCog

logger = logging.getLogger(__name__)


class AsobiBot(commands.Bot):
    """Application-specific Discord bot."""

    async def setup_hook(self) -> None:
        logger.info("🔧 コマンドCogを読み込んでいます...")
        await self.add_cog(GamesCog(self))
        synced = await self.tree.sync()
        logger.info("✅ スラッシュコマンドを%d件同期しました", len(synced))

    async def on_ready(self) -> None:
        if self.user is None:
            return
        logger.info("🎉 BOTが起動しました: %s (ID: %s)", self.user, self.user.id)
        logger.info("📡 接続サーバー数: %d", len(self.guilds))


def create_bot() -> AsobiBot:
    intents = discord.Intents.default()
    return AsobiBot(command_prefix="!", intents=intents)
