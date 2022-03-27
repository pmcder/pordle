import pygame as pg
from ui import colors
from ui.colors import Color


class Message:

    def __init__(self, message_service, win):
        self.message_service = message_service
        self.WIN = win
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.Y = 180
        self.X = 180

    def display_message(self):
        message = self.message_service.get_message()
        pg.draw.rect(self.WIN, Color.WHITE.value, pg.Rect(self.X, self.Y, 360, 80))
        img = self.font.render(message, True, Color.BLACK.value)
        self.WIN.blit(img, (self.X, self.Y))












