from messages import messageConstants
from messages.messageConstants import MessageConstants
from rows.row import Row
from words.Word import Words
from messages.message_service import MessageService


class Game:

    def __init__(self):

        self.word = Words.get_word()
        self.rows = []
        self.NUM_ROWS = 6
        self._init_rows()
        self.current_row = 0
        self.message_service = MessageService()

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
        if guess == self.word:
            self.set_win()
        if not Words.is_valid(guess):
            self.message_service.set_message(MessageConstants.INVALID_WORD.value)
        else:
            self.rows[self.current_row].complete_row(guess, self.word)
            self.current_row = self.current_row + 1

    def is_last_row(self):
        if self.current_row == 5:
            return True
        return False

    def get_message_service(self):
        return self.message_service

    def set_win(self):
        self.message_service.set_message(MessageConstants.FANTASTIC.value)























