import pygame
from pygame.sprite import Group
from tile import Tile
from player import Player
from settings import *
from debug import debug


class Level:
    def __init__(self):
        # Get display surface
        self.display_surface = pygame.display.get_surface()
        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = Group()

        self.create_map()

    def create_map(self):

        for y_index, row in enumerate(GAME_MAP):
            for x_index, tile in enumerate(row):
                x = TILESIZE * x_index
                y = TILESIZE * y_index
                if tile == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif tile == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
                else:
                    pass

    def run(self):
        # Update and draw the game
        # for sprite in self.visible_sprites:
        #     self.display_surface.blit(sprite.image, sprite.rect)
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)


class YSortCameraGroup(Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = self.half_width - player.rect.centerx
        self.offset.y = self.half_height - player.rect.centery

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image, offset_position)