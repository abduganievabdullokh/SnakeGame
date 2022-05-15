import pygame as p
import time
from pygame.locals import *
import random
from tkinter import *

SIZE = 40
#BACKGROUND_COLOR = (200, 200, 200)


class Apple:
    def __init__(self, parent_screen):
        self.image = p.image.load("Properties/mushroom_mario.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 4
        self.y = SIZE * 5

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        p.display.flip()

    def move(self):
        self.x = random.randint(0, 29) * SIZE
        self.y = random.randint(0, 15) * SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = p.image.load("Properties/mario_block.jpg").convert()  # uploading image
        self.x = [SIZE] * length  # place in x line
        self.y = [SIZE] * length  # place in y line
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
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE
        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE
        self.draw()


class Game:
    def __init__(self):
        p.init()
        # p.display.set_caption("Snake Game")
        #p.mixer.init()
        self.play_backgroun_music()
        self.surface = p.display.set_mode((SIZE * 30, SIZE * 16))  # width and height size
        #self.surface.fill(BACKGROUND_COLOR)  # color of background
        self.snake = Snake(self.surface, 3)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    def play_backgroun_music(self):
        p.mixer.music.load("Properties/super_mario_10_minutes.mp3")
        p.mixer.music.play()

    def play_sound(self, sound):
        sound = p.mixer.Sound(f"Properties/{sound}.mp3")
        p.mixer.Sound.play(sound)

    def back_image(self):
        back = p.image.load("Properties/img_mario_bg.jpg")
        self.surface.blit(back, (0, 0))

    def stop_back_image(self):
        stop_bg = p.image.load("Properties/intro_backg.jpg")
        self.surface.blit(stop_bg, (0, 0))

    def play(self):
        self.back_image()
        self.snake.walk()
        self.display_score()
        self.apple.draw()

        p.display.flip()

        # colliding with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("mario_money_sound")
            self.snake.increase_length()
            self.apple.move()

        # colliding with itself
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("dead_mario")
                raise "Game over"

    def display_score(self):
        font = p.font.SysFont("cambria", 45)
        score = font.render(f"Score: {self.snake.length - 1}", True, (0, 0, 1))
        self.surface.blit(score, (1010, 25))

    def show_game_over(self):
        self.stop_back_image()
        font = p.font.SysFont("Segoe UI", 46)
        line1 = font.render(f"  Game over! Score {self.snake.length - 1}", True, (0, 125, 0))
        self.surface.blit(line1, (330, 220))
        line2 = font.render(f"Press Enter to play again!", True, (0, 125, 0))
        self.surface.blit(line2, (330, 250))
        p.display.flip()
        p.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause = False
        while running:
            for event in p.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        p.mixer.music.play()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()

            except Exception:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(.248)



if __name__ == "__main__":
    game = Game()
    game.run()
