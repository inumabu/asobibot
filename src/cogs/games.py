"""Discord slash commands for the games."""

import logging
import random

import discord
from discord import app_commands
from discord.ext import commands

from src import games

logger = logging.getLogger(__name__)


class GamesCog(commands.Cog):
    """遊び系スラッシュコマンドの集合。"""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="omikuji", description="今日の運勢を占います")
    async def omikuji(self, interaction: discord.Interaction) -> None:
        result, message = games.draw_omikuji()
        logger.info("おみくじ: user=%s result=%s", interaction.user, result)
        await interaction.response.send_message(
            f"{interaction.user.mention} の運勢は **{result}**！\n{message}"
        )

    @app_commands.command(name="dice", description="サイコロを振ります")
    @app_commands.describe(sides="サイコロの面数（2〜1000）", count="振る個数（1〜20）")
    async def dice(self, interaction: discord.Interaction, sides: int = 6, count: int = 1) -> None:
        try:
            rolls = games.roll_dice(sides, count)
        except ValueError as error:
            await interaction.response.send_message(str(error), ephemeral=True)
            return
        logger.info("ダイス: user=%s sides=%d count=%d", interaction.user, sides, count)
        formatted = ", ".join(map(str, rolls))
        await interaction.response.send_message(
            f"🎲 {sides}面ダイスを{count}個振りました！\n"
            f"出目: **{formatted}**（合計: **{sum(rolls)}**）"
        )

    @app_commands.command(name="janken", description="BOTとじゃんけんします")
    @app_commands.describe(hand="出す手を選択")
    @app_commands.choices(hand=[
        app_commands.Choice(name=hand, value=hand) for hand in games.JANKEN_HANDS
    ])
    async def janken(self, interaction: discord.Interaction, hand: app_commands.Choice[str]) -> None:
        bot_hand = games.JANKEN_HANDS[random.randrange(len(games.JANKEN_HANDS))]
        result = games.janken_result(hand.value, bot_hand)
        logger.info(
            "じゃんけん: user=%s player=%s bot=%s result=%s",
            interaction.user,
            hand.value,
            bot_hand,
            result,
        )
        await interaction.response.send_message(
            f"✊ あなた: **{hand.value}** / BOT: **{bot_hand}**\n結果: **{result}**！"
        )

    @app_commands.command(name="quiz", description="4択クイズを出題します")
    async def quiz(self, interaction: discord.Interaction) -> None:
        item = games.draw_quiz()
        choices = "\n".join(f"{index + 1}. {choice}" for index, choice in enumerate(item.choices))
        embed = discord.Embed(
            title="🧠 4択クイズ",
            description=f"**{item.question}**\n\n{choices}",
            color=discord.Color.blurple(),
        )
        embed.set_footer(text=f"正解は {item.answer + 1}番：{item.explanation}")
        logger.info("クイズ: user=%s question=%s", interaction.user, item.question)
        await interaction.response.send_message(embed=embed)
