import pygame
from pygame.sprite import Group
from tile import Tile
from player import Player
from settings import *
from debug import debug
from support import *


class Level:
    def __init__(self):
        # Get display surface
        self.display_surface = pygame.display.get_surface()
        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = Group()

        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('zelda like/levels/0/level_0_Borders.csv'),
            'details': import_csv_layout('zelda like/levels/0/level_0_Details.csv'),
            'player': import_csv_layout('zelda like/levels/0/level_0_Player.csv'),
        }

        graphics = {
            'details': pygame.image.load('zelda like/graphics/tileset.png')
        }
        
        for style, layout in layouts.items():
            for y_index, row in enumerate(layout):
                for x_index, tile in enumerate(row):
                    if tile != '-1':
                        x = TILESIZE * x_index
                        y = TILESIZE * y_index
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites])
                        if style == 'details':
                            y_area = int(tile) // 16 * TILESIZE
                            x_area = (int(tile) - y_area * 16 / TILESIZE) * TILESIZE

                            Tile((x, y), [self.visible_sprites], 'details', area=pygame.Rect(x_area, y_area, TILESIZE, TILESIZE), surface=graphics['details'])
                        if style == 'player':
                            self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
        

    def run(self):
        # Update and draw the game
        # for sprite in self.visible_sprites:
        #     self.display_surface.blit(sprite.image, sprite.rect)
        self.visible_sprites.custom_draw_with_offset(self.player)
        self.visible_sprites.update()
        # debug(self.player.direction)


class YSortCameraGroup(Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # Creating floor
        self.floor_surface = pygame.image.load('zelda like/graphics/terrain.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0, 0))

    def custom_draw_with_offset(self, player):
        self.offset.x = self.half_width - player.rect.centerx
        self.offset.y = self.half_height - player.rect.centery

        # Drawing the floor
        floor_offset_position = self.floor_rect.topleft + self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_position)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft + self.offset

            if sprite.sprite_type != 'details':
                self.display_surface.blit(sprite.image, offset_position)
            else:
                self.display_surface.blit(sprite.image, offset_position, sprite.area)