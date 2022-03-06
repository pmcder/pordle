from rows.row import Row
from words import invalidWord

from words.Word import Words


class Game:

    def __init__(self):

        self.word = Words.get_word()
        self.rows = []
        self.NUM_ROWS = 6
        self._init_rows()
        self.current_row = 0

    def get_rows(self):
        return self.rows

    def get_current_row(self):
        return self.rows[self.current_row]

    def _init_rows(self):
        for num in range(self.NUM_ROWS):
            row = Row()
            self.rows.append(row)

    def update_incomplete_row(self, user_input):
        self.rows[self.current_row].set_partial_guess(user_input)

    def complete_current_row(self, guess):
        self.rows[self.current_row].complete_row(guess, self.word)
        self.current_row = self.current_row + 1























