from game.gameConstants import GameConstants
from rows.row import Row


def test_set_partial_guess():
    row = Row()
    row.set_partial_guess("wor")
    assert row.get_spaces()[0].get_user_letter() == "w"


def test_complete_row_correct_square():
    word = "table"
    guess = "tzzza"

    row = Row()
    row.complete_row(guess, word)
    assert row.get_spaces()[0].get_state() == GameConstants.CORRECT_SQUARE


def test_complete_row_correct_letter():
    word = "table"
    guess = "tzzza"

    row = Row()
    row.complete_row(guess, word)
    assert row.get_spaces()[4].get_state() == GameConstants.CORRECT_LETTER
















