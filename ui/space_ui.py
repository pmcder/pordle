import pygame as pg

from game.gameConstants import GameConstants
from ui.colors import Color


class SpaceUi:
    def __init__(self, win, letter):

        self.WIN = win

        self.color = Color.BLACK

        self.state = GameConstants.NO_LETTER

        self.letter = letter

        self.font = pg.font.Font('freesansbold.ttf', 32)

        self.X = 100

        self.Y = 100

        self.X_LETTER_OFFSET = 20

        self.Y_LETTER_OFFSET = 10

    def set_state(self, state):
        self.state = state

    def set_coords(self, x, y):
        self.X = x
        self.Y = y

    def draw_space(self):
        this_color = self._get_color(self.state)
        pg.draw.rect(self.WIN, this_color, pg.Rect(self.X, self.Y, 60, 60))
        img = self.font.render(self.letter, True, Color.BLACK.value)
        self.WIN.blit(img, (self.X+self.X_LETTER_OFFSET, self.Y + self.Y_LETTER_OFFSET))


    def _get_color(self, state ):
        """consider eliminating color and using value on game constants"""
        colors = {
            GameConstants.NO_LETTER: Color.WHITE.value,
            GameConstants.CORRECT_LETTER: Color.CORRECT_LETTER.value,
            GameConstants.CORRECT_SQUARE: Color.CORRECT_SQUARE.value,
            GameConstants.INCORRECT_LETTER: Color.INCORRECT_LETTER.value
        }
        return colors.get(state)


