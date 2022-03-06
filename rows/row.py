from game.gameConstants import GameConstants
from rows.space import Space
from words import invalidWord
from words.Word import Words


class Row:
    def __init__(self):
        self.complete = False
        self.spaces = []
        for letter in range(5):
            space = Space()
            self.spaces.append(space)
        self.is_complete = False
        self.is_current = False
        self.partial_guess = ""
        self.final_guess = ""

    def get_spaces(self):
        return self.spaces

    def set_spaces(self, spaces):
        self.spaces = spaces

    def set_partial_guess(self, word):
        idx = len(word)
        self.partial_guess = word
        if idx > 0:
            for num in range(idx):
                self.spaces[num].set_user_letter(self.partial_guess[num])

    def find_space(self, letter):
        pass

    def complete_row(self, guess, word):
        self._set_user_letter(guess)
        self.final_guess = guess
        self.is_complete = True
        self.is_current = False
        for idx in range(5):
            if word[idx] == guess[idx]:
                self.spaces[idx].set_state(GameConstants.CORRECT_SQUARE)
                # TODO additional testing this line
                #  passed test but doesn't look correct
                # TODO implement search algorithm for letter space with letter
            elif guess[idx] in word:
                self.spaces[idx].set_state(GameConstants.CORRECT_LETTER)

    def _set_user_letter(self, guess):
        for idx in range(5):
            self.spaces[idx].set_user_letter(guess[idx])





































