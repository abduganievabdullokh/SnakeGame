# class Apple file
import pygame as p
import random
import main


class Apple:
    def __init__(self, parent_screen):
        self.image = p.image.load("Properties/mushroom_mario.jpg").convert()
        self.parent_screen = parent_screen
        self.x = random.randint(0, (main.SCREEN_WIDTH/main.SIZE)-1) * main.SIZE
        self.y = random.randint(0, (main.SCREEN_HEIGHT/main.SIZE)-1) * main.SIZE

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        p.display.flip()

    def move(self):
        self.x = random.randint(0, 29) * main.SIZE
        self.y = random.randint(0, 15) * main.SIZE


