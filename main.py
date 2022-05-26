# import pygame as p  # typedef pygame p;
# import button as but
import game
# from tkinter import *

SIZE = 40
SCREEN_HEIGHT = SIZE * 16
SCREEN_WIDTH = SIZE * 30
#
# screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# p.display.set_caption("Button screen")
#
# start_img = p.image.load('Properties/apple.jpg').convert_alpha()
# exit_img = p.image.load('Properties/apple.jpg').convert_alpha()
#
# start_button = but.Button(140, 210, start_img, 0.6)
# exit_button = but.Button(450, 210, exit_img, 0.6)


if __name__ == "__main__":
    game_run = game.Game()
    game_run.run()
