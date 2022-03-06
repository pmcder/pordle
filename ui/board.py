import pygame as pg

from ui.row_ui import RowUi


class Board:

    def __init__(self, win, rows):
        self.SPACING = 75
        self.WIN = win
        self.row_num = 0
        self.rows_ui = []
        self.y = 100
        self.rows = rows
        self.init_rows(self.rows)

    def draw_board(self):
        for row in self.rows_ui:
            row.draw_row()

    def init_rows(self, rows):
        for row in self.rows:
            row_ui = RowUi(self.WIN, row)
            row_ui.set_y(self.y)
            self.rows_ui.append(row_ui)
            self.y = self.y + self.SPACING

    def update_rows(self, rows):
        idx = 0
        self.rows = rows
        for row in self.rows:
            self.rows_ui[idx].update(row)
            idx = idx+1

    def draw_completed_row(self):
        pass

    def reset_board(self):
        for row_ui in self.rows_ui:
            row_ui.reset_row()







