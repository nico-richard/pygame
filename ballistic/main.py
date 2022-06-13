from math import gamma
import pygame, sys

class Game:

    def __init__(self):
        pygame.init()
        self.FPS = 30
        self.fps_clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 500))
        self.screen.fill((100, 100, 100))
        self.gravity = (0, 10)
        

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 50
        self.velocity = (1, 0)
        self.diameter = 20
        self.color = (200, 200, 200)
        self.x_increment = self.velocity[0] + game.gravity[0]
        self.y_increment = self.velocity[1] + game.gravity[1]
        pygame.draw.circle(game.screen, self.color, (self.x, self.y), self.diameter)

    def update(self):
        if self.x >= game.screen.get_size()[0] - self.diameter:
            self.x_increment *= -1
        elif self.x <= 0:
            self.x_increment *= -1
        elif self.y >= game.screen.get_size()[1] - self.diameter:
            self.y_increment *= -1
        elif self.y <= self.diameter:
            self.y_increment *= -1
        self.x += self.x_increment
        self.y += self.y_increment
        pygame.draw.circle(game.screen, self.color, (self.x, self.y), self.diameter)

        pygame.draw.line(game.screen, (255,0,0), (0,0), (game.screen.get_size()[0],0))

game = Game()
ball = Ball()

while True:
    game.screen.fill((100, 100, 100))
    ball.update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.fps_clock.tick(game.FPS)