import pygame

from settings import Settings
from figure import Figure


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

        self.left_edge = pygame.rect.Rect(x - Settings.field_cells_size + 1, y,
                                          Settings.field_cells_size, Settings.field_height)
        self.right_edge = pygame.rect.Rect(x + Settings.field_cells_x * Settings.field_cells_size - 1, y,
                                          Settings.field_cells_size, Settings.field_height)

        self.falling_figure = Figure(self, self.x, self.y)

    def refresh(self):
        pygame.draw.rect(self.screen, Settings.field_border_color, self.border, Settings.field_border_width)
        self.falling_figure.draw(self.screen)

    def make_step(self):
        self.falling_figure.move_down()
