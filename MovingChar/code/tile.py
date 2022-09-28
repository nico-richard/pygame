import pygame
from settings import *
from pygame.sprite import Sprite


class Tile(Sprite):
    def __init__(self, pos, groups, sprite_type=None, area=pygame.Rect(0, 0, 32, 32), surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.area = area
        # if sprite_type == 'details':
        #     self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
        # else:
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)