import math
import pygame
import sys
from pygame.sprite import Sprite

pygame.init()

FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
GRAY = (100, 100, 100)
GRAVITY = (0, 10)
FPS_CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Ball(Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = (0, 0)
        self.radius = 5
        self.color = (200, 200, 200)
        # self.x_increment = self.velocity[0] + GRAVITY[0]
        # self.y_increment = self.velocity[1] + GRAVITY[1]
        self.x_increment = 0
        self.y_increment = 0
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT - self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius - 2)

    def update(self):
        if self.x >= screen.get_size()[0] - self.radius:
            self.x_increment *= -1
        elif self.x <= 0:
            self.x_increment *= -1
        elif self.y >= screen.get_size()[1] - self.radius:
            self.y_increment *= -1
        elif self.y <= self.radius:
            self.y_increment *= -1
        self.x += self.x_increment
        self.y += self.y_increment
        self.x_increment *= 0.95
        self.y_increment *= 0.95
        # pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def findangle(self, pos):
        delta_x = (self.x - pos[0])
        delta_y = (self.y - pos[1])

        if delta_x == 0:
            angle = math.pi / 2
        else:
            angle = math.atan(delta_y / delta_x)

        # haut droite
        if pos[1] < self.y and pos[0] > self.x:
            angle = - angle
        # haut gauche
        if pos[1] < self.y and pos[0] < self.x:
            angle = math.pi - angle
        # # bas gauche
        # if pos[1] > self.y and pos[0] < self.x:
        #     angle = math.pi + abs(angle)
        # # bas droite
        # if pos[1] > self.y and pos[0] > self.x:
        #     angle = (math.pi * 2) - angle

        return angle

    def ball_path(self, x, y, power, angle, time):
        vel_x = math.cos(angle) * power
        vel_y = math.sin(angle) * power

        dist_x = vel_x * time
        dist_y = vel_y * time + - 8 * time ** 2 / 2

        new_x = round(dist_x + x)
        new_y = round(y - dist_y)

        return [new_x, new_y]


font = pygame.font.SysFont('Arial', 15)


def update_text(content):
    text = font.render(content, True, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - text.get_size()[0] - 10, 10))


ball = Ball()

time = 0
power = 0
angle = 0
shoot = False
text = 'default'

while True:

    pos = pygame.mouse.get_pos()
    line = [(ball.x, ball.y), pos]

    # redraw screen --------------
    screen.fill((100, 100, 100))
    ball.draw(screen)
    pygame.draw.line(screen, (0, 0, 0), line[0], line[1])
    # ball.update()
    update_text(text)
    pygame.display.update()
    # ----------------------------

    if shoot:
        if ball.y <= SCREEN_HEIGHT - ball.radius:
            time += 0.1
            new_pos = ball.ball_path(x, y, power, angle, time)

            if new_pos[0] <= 0:
                new_pos[0] = abs(new_pos[0])
                if new_pos[0] >= (SCREEN_WIDTH - ball.radius):
                    new_pos[0] = SCREEN_WIDTH - abs(new_pos[0] - SCREEN_WIDTH)
            elif new_pos[0] >= (SCREEN_WIDTH - ball.radius):
                new_pos[0] = SCREEN_WIDTH - abs(new_pos[0] - SCREEN_WIDTH)
            else:
                ball.x = new_pos[0]

            ball.x = new_pos[0]
            ball.y = new_pos[1]
        else:
            shoot = False
            ball.y = SCREEN_HEIGHT - ball.radius

    power_d = round(
        math.sqrt((line[0][1] - line[1][1]) ** 2 + (line[0][0] - line[1][0]) ** 2), 2)
    angle_d = round(ball.findangle(pos), 2)
    text = f'Power : {power_d} Angle : {angle_d} shoot : {shoot} '\
           f'Ball : {ball.x, ball.y} Mouse {pos} time : {round(time, 0)}'

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not shoot:
                shoot = True
                x = ball.x
                y = ball.y
                time = 0
                power = round(
                    math.sqrt((line[0][1] - line[1][1]) ** 2 + (line[0][0] - line[1][0]) ** 2), 2) / 6
                angle = round(ball.findangle(pos), 2)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    FPS_CLOCK.tick(FPS)
