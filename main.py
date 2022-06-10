import pygame, sys

pygame.init()
fps_clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
x = y = 20
x_increment = 5
y_increment = 2

while True:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 100, 100), pygame.Rect(x, y, 30, 30))
    pygame.draw.rect(screen, (25, 120, 200), pygame.Rect(x, y, 10, 10))
    pygame.display.update()

    if x >= screen.get_size()[0] - 30:
        x_increment *= -1

    elif x <= 0:
        x_increment *= -1

    if y >= screen.get_size()[1] - 30:
        y_increment *= -1

    if y <= 0:
        y_increment *= -1

    x += x_increment
    y += y_increment

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    fps_clock.tick(120)