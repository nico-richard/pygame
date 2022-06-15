import pygame
from tile import Tile
from player import Player
from settings import *
from debug import debug


class Level:
    def __init__(self):
        # Get display surface
        self.display_surface = pygame.display.get_surface()
        # Sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):

        for y_index, row in enumerate(GAME_MAP):
            for x_index, tile in enumerate(row):
                x = TILESIZE * x_index
                y = TILESIZE * y_index
                if tile == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif tile == 'p':
                    self.player = Player((x, y), [self.visible_sprites])
                else:
                    pass

    def run(self):
        # Update and draw the game
        for sprite in self.visible_sprites:
            self.display_surface.blit(sprite.image, sprite.rect)
        self.visible_sprites.update()
        debug(self.player.direction)
