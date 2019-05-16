import pygame

from settings import Settings


class Field:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        # border around the field
        self.border = pygame.rect.Rect(self.x - Settings.field_border_width,
                                       self.y - Settings.field_border_width,
                                       Settings.field_width + 2 * Settings.field_border_width,
                                       Settings.field_height + 2 * Settings.field_border_width)
        pygame.draw.rect(self.screen, Settings.field_border_color, self.border, Settings.field_border_width)
