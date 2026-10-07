"""Game rules and randomization independent from Discord."""

import random
from dataclasses import dataclass

OMIKUJI_RESULTS = ("大吉", "中吉", "小吉", "吉", "末吉", "凶")
OMIKUJI_MESSAGES = {
    "大吉": "最高の一日！思い切って行動してみよう。",
    "中吉": "いい流れです。小さな一歩を大切に。",
    "小吉": "焦らずいけば、きっと良いことがあります。",
    "吉": "平和で安定した一日になりそう。",
    "末吉": "これから運気上昇。準備をして待とう。",
    "凶": "今日は無理をせず、慎重に過ごそう。",
}
JANKEN_HANDS = ("グー", "チョキ", "パー")
JANKEN_BEATS = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}


@dataclass(frozen=True)
class Quiz:
    question: str
    choices: tuple[str, ...]
    answer: int
    explanation: str


QUIZZES = (
    Quiz("日本でいちばん高い山は？", ("富士山", "北岳", "奥穂高岳", "間ノ岳"), 0, "富士山は標高3,776mです。"),
    Quiz("太陽系で最も大きい惑星は？", ("地球", "木星", "土星", "海王星"), 1, "木星は太陽系最大の惑星です。"),
    Quiz("水の化学式は？", ("CO2", "O2", "H2O", "NaCl"), 2, "水は水素2つと酸素1つからなるH2Oです。"),
)


def draw_omikuji() -> tuple[str, str]:
    result = random.choice(OMIKUJI_RESULTS)
    return result, OMIKUJI_MESSAGES[result]


def roll_dice(sides: int, count: int = 1) -> list[int]:
    if not 2 <= sides <= 1000:
        raise ValueError("面数は2〜1000で指定してください。")
    if not 1 <= count <= 20:
        raise ValueError("個数は1〜20で指定してください。")
    return [random.randint(1, sides) for _ in range(count)]


def janken_result(player: str, bot: str) -> str:
    if player not in JANKEN_HANDS or bot not in JANKEN_HANDS:
        raise ValueError("グー・チョキ・パーのいずれかを指定してください。")
    if player == bot:
        return "あいこ"
    return "あなたの勝ち" if JANKEN_BEATS[player] == bot else "BOTの勝ち"


def draw_quiz() -> Quiz:
    return random.choice(QUIZZES)
