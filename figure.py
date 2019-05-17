import pygame
import random
from pygame.sprite import Group

from square import Square
from settings import Settings


class Figure:

    def __init__(self, field, x, y):
        self.field = field
        self.x = x + (Settings.field_cells_x // 2 - 2) * Settings.field_cells_size
        self.y = y
        self.group = Group()
        self.template = Settings.figures_storage[1]
        self.rotate_status = 0
        self.color = Settings.figures_colors[Figure.get_random(len(Settings.figures_colors))]
        self.moving_fast = False

    @staticmethod
    def get_random(a):
        return int(random.random() * 1000) % a

    def draw(self, screen):
        self.group.empty()
        for i in range(Settings.figures_size):
            for k in range(Settings.figures_size):
                if self.template[self.rotate_status][i][k]:
                    self.group.add(Square(self.x + k * Settings.field_cells_size,
                                          self.y + i * Settings.field_cells_size,
                                          self.color))
        self.group.draw(screen)

    def rotate_clock_wise(self):
        self.rotate_status = (self.rotate_status + 1) % len(self.template)

    def rotate_anti_clock_wise(self):
        self.rotate_status = (self.rotate_status - 1 + len(self.template)) % len(self.template)

    def move_left(self):
        self.x -= Settings.field_cells_size
        for square in self.group.sprites():
            if square.rect.colliderect(self.field.left_edge):
                self.x += Settings.field_cells_size
                return

    def move_right(self):
        self.x += Settings.field_cells_size
        for square in self.group.sprites():
            if square.rect.colliderect(self.field.right_edge):
                self.x -= Settings.field_cells_size
                return

    def move_down(self):
        self.y += Settings.field_cells_size
