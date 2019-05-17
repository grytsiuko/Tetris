import pygame
from pygame.sprite import Sprite

from settings import Settings


class Square(Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((Settings.field_cells_size, Settings.field_cells_size))
        self.rect = pygame.rect.Rect(x, y, Settings.field_cells_size, Settings.field_cells_size)
        pygame.draw.rect(self.image, self.color, self.image.get_rect())
        pygame.draw.rect(self.image, Settings.field_cells_border_color, self.image.get_rect(), 1)
