import pygame

pygame.init()

font = pygame.font.Font(None, 30)
yellow = (247, 215, 22)
blue = (41, 52, 98)

def debug(info, y=10, x=10):
    display_surface = pygame.display.get_surface()
    debug_text = font.render(str(info), True, yellow)
    debug_rect = debug_text.get_rect(
        topleft=(x, y),
        width=debug_text.get_size()[0] + 10,
        height=debug_text.get_size()[1] + 10
        )
    pygame.draw.rect(display_surface, blue, debug_rect, border_radius=3)
    display_surface.blit(debug_text, (debug_rect.left + 5, debug_rect.top + 5))