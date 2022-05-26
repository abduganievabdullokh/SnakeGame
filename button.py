# class Button file
import pygame as p


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = p.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # making mouse
        position = p.mouse.get_pos()

        # get the collision and click
        if self.rect.collidepoint(position):
            if p.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if p.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # displaying buttons on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


# start_img = p.image.load('Properties/apple.jpg').convert_alpha()
# exit_img = p.image.load('Properties/apple.jpg').convert_alpha()

