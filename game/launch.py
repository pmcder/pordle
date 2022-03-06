import pygame as pg

from game.controller import Game
from ui.board import Board
from ui.colors import Color

pg.init()


WIDTH = 600
HEIGHT = 600

"""create X and Y to position squares"""
X = 400
Y = 400

FPS = 60
pg.display.set_caption("Pordle")
WIN = pg.display.set_mode((WIDTH, HEIGHT))

ENTER_KEY = 13
BACKSPACE = 8 # os specific ?

clock = pg.time.Clock()

game = Game()
board = Board(WIN, game.get_rows())
board.draw_board()
run = False

user_input = ""
FONT_OFFSET = 40
current_letter = -1
FONT_OFFSET_ROW = 120
new_row_flag = False


def tick():
    global user_input
    global FONT_OFFSET
    global FONT_OFFSET_ROW
    global current_letter
    global run
    global new_row_flag


    for event in pg.event.get():
        if event.type == pg.KEYDOWN and len(user_input) <= 4:
            if event.unicode.isalpha():
                user_input += event.unicode
                FONT_OFFSET = FONT_OFFSET + 75
                current_letter = current_letter + 1

            # elif event.key == BACKSPACE:
            #     user_input = user_input.rstrip(user_input[-1])
            #     current_letter = current_letter - 1

        elif event.type == pg.KEYDOWN and len(user_input) >= 4:
            if event.key == ENTER_KEY:
                game.complete_current_row(user_input)
                board.update_rows(game.get_rows())
                board.reset_board()
                FONT_OFFSET_ROW = FONT_OFFSET_ROW + 75
                FONT_OFFSET = 40
                board.draw_board()
                pg.display.update()
                new_row_flag = True



        elif event.type == pg.QUIT:
            run = False


def render():
    global FONT_OFFSET
    global FONT_OFFSET_ROW
    global new_row_flag
    global user_input
    global current_letter
    pg.display.update()

    # UI letters only
    font = pg.font.Font('freesansbold.ttf', 32)
    if current_letter > -1:
        img = font.render(user_input[current_letter], True, Color.BLACK.value)
        WIN.blit(img, (FONT_OFFSET, FONT_OFFSET_ROW))
    if new_row_flag:
        user_input = ""
        current_letter = -1
        new_row_flag = False


def launch():
    global run
    run = True

    while run:
        clock.tick(FPS)
        tick()
        render()

    pg.quit()


if __name__ == "__main__" :

    launch()



