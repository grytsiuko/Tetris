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
        self.template = Settings.figures_storage[Figure.get_random(len(Settings.figures_storage))]
        self.rotate_status = 0
        # self.rotate_status = Figure.get_random(len(self.template))
        self.color = Settings.figures_colors[Figure.get_random(len(Settings.figures_colors))]
        self.size = len(self.template[0])
        self.group = Group()
        self.reload_sprites()
        self.move_delay = Settings.game_delay

    @staticmethod
    def get_random(a):
        return int(random.random() * 1000) % a

    def reload_sprites(self):
        self.group.empty()
        for i in range(self.size):
            for k in range(self.size):
                if self.template[self.rotate_status][i][k]:
                    self.group.add(Square(self.x + k * Settings.field_cells_size,
                                          self.y + i * Settings.field_cells_size,
                                          self.color))

    def draw(self):
        self.group.draw(self.field.screen)

    def check_barriers(self):
        for barrier in self.field.barriers:
            if pygame.sprite.groupcollide(self.group, barrier, False, False):
                return True
        return False

    def change_rotate_status(self, shift):
        self.rotate_status = (self.rotate_status + shift + len(self.template)) % len(self.template)

    def rotate_clock_wise(self):
        self.change_rotate_status(1)
        self.reload_sprites()
        if self.check_barriers():
            self.change_rotate_status(-1)
            self.reload_sprites()

    def rotate_anti_clock_wise(self):
        self.change_rotate_status(-1)
        self.reload_sprites()
        if self.check_barriers():
            self.change_rotate_status(1)
            self.reload_sprites()

    def move_left(self):
        self.x -= Settings.field_cells_size
        self.group.update(-Settings.field_cells_size, 0)
        if self.check_barriers():
            self.x += Settings.field_cells_size
            self.group.update(Settings.field_cells_size, 0)

    def move_right(self):
        self.x += Settings.field_cells_size
        self.group.update(Settings.field_cells_size, 0)
        if self.check_barriers():
            self.x -= Settings.field_cells_size
            self.group.update(-Settings.field_cells_size, 0)

    def move_down(self):
        self.y += Settings.field_cells_size
        self.group.update(0, Settings.field_cells_size)

    def move_up(self):
        self.y -= Settings.field_cells_size
        self.group.update(0, -Settings.field_cells_size)
