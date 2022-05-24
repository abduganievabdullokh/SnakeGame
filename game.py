# class game file
import pygame as p
import main
import snake
import apple
import time
from pygame.locals import *


class Game:
    def __init__(self):
        p.init()
        p.display.set_caption("Snake Game")
        self.play_background_music()
        self.surface = p.display.set_mode((main.SCREEN_WIDTH, main.SCREEN_HEIGHT))  # width and height size
        # self.surface.fill(BACKGROUND_COLOR)  # color of background
        self.snake = snake.Snake(self.surface, 3)
        self.snake.draw()
        self.apple = apple.Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + main.SIZE:
            if y2 <= y1 < y2 + main.SIZE:
                return True
        return False

    def play_background_music(self):
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
            pass
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
            self.play_sound("dead_mario")
            raise "Game over"

    def display_score(self):
        font = p.font.SysFont("cambria", 45)
        score = font.render(f"Score: {self.snake.length - 1}", True, (0, 0, 1))
        self.surface.blit(score, (1010, 25))

    def show_game_over(self):
        self.stop_back_image()
        font = p.font.SysFont("", 80)
        line1 = font.render(f"  Game over! Score {self.snake.length - 1}", True, (0, 0, 0))
        self.surface.blit(line1, (290, 260))
        # line2 = font.render(f"Press Enter to play again!", True, (0, 1, 0))
        # self.surface.blit(line2, (222, 343))
        p.display.flip()
        main.exit_button.draw(main.screen)
        p.mixer.music.pause()

    def reset(self):
        self.snake = snake.Snake(self.surface, 1)
        self.apple = apple.Apple(self.surface)

    def run(self):
        running = True
        pause = False
        while running:
            main.screen.fill((111, 111, 111))
            if main.start_button.draw(main.screen):
                print('Start')
            if main.exit_button.draw(main.screen):
                running = False
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
            time.sleep(.1)
