import pygame
from pygame.sprite import Sprite

from src.settings import Settings


class Square(Sprite):

    def __init__(self, x, y, color=(0, 0, 0), empty=False,
                 size=Settings.field_cells_size, star=False):

        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = pygame.rect.Rect(x, y, size, size)
        self.star = star

        if not empty:
            pygame.draw.rect(self.image, color, self.image.get_rect())
            pygame.draw.rect(self.image, Settings.field_cells_border_color,
                             self.image.get_rect(), 1)
            if self.star:
                self.image.blit(Settings.figure_star_img, Settings.figure_star_img.get_rect())
        else:
            self.image.set_alpha(0)

    def update(self, *args):

        x = args[0]
        y = args[1]
        self.rect.move_ip(x, y)
