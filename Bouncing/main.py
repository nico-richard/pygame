import string
from random import randint, random, randrange, choice
import pygame, sys

INITIAL_SQUARE_COLOR = (255, 100, 100)

class Game:

    def __init__(self):
        pygame.init()
        self.fps_clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 500))

class Square(pygame.sprite.Sprite):
    
    def __init__(self):
        self.width = randint(5, 10)
        self.height = randint(5, 10)
        self.x = randint(1, game.screen.get_width() - self.width - 1)
        self.y = randint(1, game.screen.get_height() - self.height - 1)
        self.x_increment = randint(2, 10) * randrange(-1, 2, 2)
        self.y_increment = randint(2, 10) * randrange(-1, 2, 2)
        self.color = INITIAL_SQUARE_COLOR
        self.name = ''.join([choice(string.ascii_lowercase) for _ in range(8)])
        self.draw_rect()
        super().__init__()

    def draw_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(game.screen, self.color, self.rect)

    def update_rect(self):
        if self.x >= game.screen.get_size()[0] - self.width:
            self.x_increment *= -1
            self.set_random_color()

        elif self.x <= 0:
            self.x_increment *= -1
            self.set_random_color()

        if self.y >= game.screen.get_size()[1] - self.height:
            self.y_increment *= -1
            self.set_random_color()

        if self.y <= 0:
            self.y_increment *= -1
            self.set_random_color()

        self.x += self.x_increment
        self.y += self.y_increment

        # self.x_increment *= 1.001
        # self.y_increment *= 1.001

        self.draw_rect()

    def set_random_color(self):
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))


class KillSquare(Square):
    
    def __init__(self):
        super().__init__()
        self.width = 200
        self.height = 20
        self.x = game.screen.get_width() / 2 - self.width / 2 - 100
        self.y = game.screen.get_height() / 2 - self.height / 2
        self.color = (255, 0, 0)
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def draw_rect(self):
        super().draw_rect()
        self.loading_bar = pygame.Rect(self.x, self.y, (nb_square - len(squares)) * 200 / nb_square, self.height)
        pygame.draw.rect(game.screen, (0, 255, 0), self.loading_bar)

    def move(self):
        if self.move_right:
            kill_square.x += 5
        if self.move_left:
            kill_square.x -= 5
        if self.move_up:
            kill_square.y -= 5
        if self.move_down:
            kill_square.y += 5

game = Game()
squares = pygame.sprite.Group()

nb_square = 10000

for _ in range(nb_square):
    squares.add(Square())

kill_square = KillSquare()

while len(squares) > 1:
    game.screen.fill((0, 0, 0))
    for square in squares:
        square.update_rect()
    
    kill_square.draw_rect()
    kill_square.move()

    pygame.sprite.spritecollide(kill_square, squares, True)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                kill_square.move_left = True
            if event.key == pygame.K_RIGHT:
                kill_square.move_right = True
            if event.key == pygame.K_UP:
                kill_square.move_up = True
            if event.key == pygame.K_DOWN:
                kill_square.move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                kill_square.move_left = False
            if event.key == pygame.K_RIGHT:
                kill_square.move_right = False
            if event.key == pygame.K_UP:
                kill_square.move_up = False
            if event.key == pygame.K_DOWN:
                kill_square.move_down = False
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    game.fps_clock.tick(60)

for square in squares:
    print(square.name)