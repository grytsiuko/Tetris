import pygame
from pygame.sprite import Sprite

from settings import Settings


class Square(Sprite):
    def __init__(self, x, y, color=(0, 0, 0), empty=False):
        super().__init__()
        self.image = pygame.Surface((Settings.field_cells_size, Settings.field_cells_size))
        if not empty:
            pygame.draw.rect(self.image, color, self.image.get_rect())
            pygame.draw.rect(self.image, Settings.field_cells_border_color, self.image.get_rect(), 1)
        else:
            self.image.set_alpha(0)
        self.rect = pygame.rect.Rect(x, y, Settings.field_cells_size, Settings.field_cells_size)
