import pygame
from pygame.sprite import Group

from settings import Settings
from figure import Figure
from fallen import Fallen
from square import Square


class Field:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.score = 0

        # border around the field
        self.border = pygame.rect.Rect(self.x - Settings.field_border_width,
                                       self.y - Settings.field_border_width,
                                       Settings.field_width + 2 * Settings.field_border_width,
                                       Settings.field_height + 2 * Settings.field_border_width)

        self.left_edge = Group()
        self.right_edge = Group()
        for i in range(Settings.field_cells_y):
            self.left_edge.add(Square(x - Settings.field_cells_size,
                                      y + i * Settings.field_cells_size))
            self.right_edge.add(Square(x + Settings.field_cells_x * Settings.field_cells_size,
                                       y + i * Settings.field_cells_size))

        self.falling_figure = Figure(self, self.x, self.y)
        self.fallen = Fallen(self, self.x, self.y)
        self.barriers = [self.left_edge, self.right_edge, self.fallen.group]

    def refresh(self):
        pygame.draw.rect(self.screen, Settings.field_border_color, self.border, Settings.field_border_width)
        self.falling_figure.draw()
        self.fallen.draw()

    def make_step(self):
        self.falling_figure.move_down()
        if pygame.sprite.groupcollide(self.fallen.group, self.falling_figure.group, False, False):
            self.falling_figure.move_up()
            self.score += Settings.game_score_landing
            self.add_figure_to_fallen()
            self.falling_figure = Figure(self, self.x, self.y)

    def add_figure_to_fallen(self):
        for square in self.falling_figure.group.sprites():
            row = (square.rect.y - self.x) // Settings.field_cells_size
            col = (square.rect.x - self.x) // Settings.field_cells_size
            self.fallen.matrix[row][col] = square
