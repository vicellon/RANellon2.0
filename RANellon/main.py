#stealing this from table too lol
__author__      = "Vicellon"
__credits__     = ["Vicellon"], ["T4Bl3rUs"]
__version__     = 0.1

import pygame
import random
import string
import sys

from text import renderText
from colormap import colors

class Game:
    SMALL_X = 400
    SMALL_Y = 400
    BIG_X = 800
    BIG_Y = 800
    FPS = 60  # frames per second setting

    def __init__(self):
        self.sequence_length = self.get_delay()
        self.clock = pygame.time.Clock()
        self.display = pygame.Surface((self.SMALL_X, self.SMALL_Y), pygame.SRCALPHA)
        self.background = pygame.Surface((self.SMALL_X, self.SMALL_Y))
        self.screen = pygame.display.set_mode((self.BIG_X, self.BIG_Y))
        pygame.display.set_caption('RANellon')
        pygame.mouse.set_visible(True)
        self.font = pygame.font.SysFont(None, 200, bold=False)
        self.delay_counter = self.sequence_length
        self.last_color = None

    def get_delay(self):
        while True:
            try:
                delay_deciseconds = int(input("Deciseconds of delay: "))
                if delay_deciseconds >= 0:
                    return delay_deciseconds * self.FPS // 10  # convert deciseconds to equivalent frame count
                else:
                    print("Please input a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    @staticmethod
    def random_char_num():
        chars_and_nums = string.ascii_letters + string.digits
        return random.choice(chars_and_nums)

    def random_color(self):
        color = random.choice(list(colors.values()))
        while color == self.last_color: # Ensures the new color is not the same as the last one.
            color = random.choice(list(colors.values()))
        self.last_color = color
        return color

    def populate(self):
        self.background.fill(self.random_color())
        renderText(self.random_char_num(), self.font, (255, 255, 255), self.SMALL_X/2, (self.SMALL_Y/2)-60, self.display, -1, "center")

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def run(self):
        while True:
            try:
                self.handle_input()

                if self.delay_counter >= self.sequence_length:
                    self.display.fill((0,0,0,0))  # clear the foreground surface
                    self.populate()
                    self.delay_counter = 0
                else:
                    self.delay_counter += 1

                self.screen.blit(pygame.transform.scale(self.background, self.screen.get_size()), (0, 0))
                self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
                pygame.display.flip()
                self.clock.tick(self.FPS)

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()