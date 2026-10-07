import pytest

from src.games import draw_omikuji, janken_result, roll_dice


def test_roll_dice_returns_requested_count_and_range():
    result = roll_dice(6, 10)
    assert len(result) == 10
    assert all(1 <= value <= 6 for value in result)


@pytest.mark.parametrize("sides,count", [(1, 1), (6, 0), (1001, 1), (6, 21)])
def test_roll_dice_rejects_invalid_values(sides, count):
    with pytest.raises(ValueError):
        roll_dice(sides, count)


def test_janken_result():
    assert janken_result("グー", "チョキ") == "あなたの勝ち"
    assert janken_result("グー", "グー") == "あいこ"
    assert janken_result("グー", "パー") == "BOTの勝ち"


def test_omikuji_has_known_result_and_message():
    result, message = draw_omikuji()
    assert result in {"大吉", "中吉", "小吉", "吉", "末吉", "凶"}
    assert message
