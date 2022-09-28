import pygame
import sys
from settings import *
from debug import debug
from level import Level


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.icon = pygame.image.load('zelda like/graphics/swords.png').convert_alpha()
        pygame.display.set_caption('Zlada')
        pygame.display.set_icon(self.icon)

        self.clock = pygame.time.Clock()
        self.level = Level()
        self.GREEN_BACKGROUND = (50, 90, 50)
        self.BLACK= (0, 0, 0)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.BLACK)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
