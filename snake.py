# class Snake file

import pygame as p
import main


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = p.image.load("Properties/akfalogo.jpg").convert()  # uploading image
        self.x = [main.SIZE] * length  # place in x line
        self.y = [main.SIZE] * length  # place in y line
        self.direction = "up"
        self.direction = "down"
        self.direction = "left"
        self.direction = "right"

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        # self.parent_screen.fill(BACKGROUND_COLOR)

        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        p.display.flip()

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= main.SIZE
        if self.direction == "down":
            self.y[0] += main.SIZE
        if self.direction == "left":
            self.x[0] -= main.SIZE
        if self.direction == "right":
            self.x[0] += main.SIZE
        self.draw()
