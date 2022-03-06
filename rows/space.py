from game.gameConstants import GameConstants


class Space:
    def __init__(self):
        self.user_letter = ""
        self.state = GameConstants.NO_LETTER

    def get_user_letter(self):
        return self.user_letter

    def set_user_letter(self, letter):
        self.user_letter = letter

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state






