import pygame as pg

from game.gameConstants import GameConstants
from ui.space_ui import SpaceUi


class RowUi:
    def __init__(self, win, row):

        self.WIN = win
        self.row = row
        self.x = 100
        self.y = 100
        self.spaces = self.row.get_spaces()
        self.SPACING = 75

    def draw_row(self):
        for s in self.spaces:
            space = SpaceUi(self.WIN, s.get_user_letter())
            space.set_state(s.get_state())
            space.set_coords(self.x, self.y)
            space.draw_space()
            self.x = self.x + self.SPACING

    def set_y(self, y):
        self.y = y

    def update(self, row):
        self.row = row

    def reset_row(self):
        self.x = 100











