import pygame
import random
import copy
from pygame.sprite import Group

from square import Square
from settings import Settings


class Figure:

    def __init__(self, field):

        self.field = field
        self.template = copy.deepcopy(Settings.figures_storage[Figure.get_random(len(Settings.figures_storage))])
        self.rotate_status = Figure.get_random(len(self.template))
        self.color = Settings.figure_colors[Figure.get_random(len(Settings.figure_colors))]
        self.size = len(self.template[0])
        self.init_stars()

        self.x = self.field.x + Settings.field_width + Settings.field_margin + \
                 (Settings.game_side_width - len(self.template[0]) * Settings.field_cells_size) // 2
        self.y = self.field.y + Settings.field_cells_size

        self.group = Group()
        self.reload_sprites()
        self.move_delay = Settings.game_delay

    @staticmethod
    def get_random(a):

        return int(random.random() * 1000) % a

    def init_stars(self):

        for i in range(self.size):
            for k in range(self.size):
                if self.template[0][i][k] == 0:
                    continue
                if random.random() < Settings.figure_star_probability:
                    self.template[0][i][k] = 2
                    self.template[1][k][self.size - i - 1] = 2
                    self.template[2][self.size - i - 1][self.size - k - 1] = 2
                    self.template[3][self.size - k - 1][i] = 2

    def reload_sprites(self):

        self.group.empty()
        for i in range(self.size):
            for k in range(self.size):
                cell_type = self.template[self.rotate_status][i][k]
                if cell_type:
                    self.group.add(Square(self.x + k * Settings.field_cells_size,
                                          self.y + i * Settings.field_cells_size,
                                          self.color, star=(cell_type == 2)))

    def draw(self):

        self.group.draw(self.field.screen)

    def check_barriers(self):

        for barrier in self.field.barriers:
            if pygame.sprite.groupcollide(self.group, barrier, False, False):
                return True
        return False

    def change_rotate_status(self, shift):

        self.rotate_status += shift + len(self.template)
        self.rotate_status %= len(self.template)

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

    def move_to_field(self):

        self.x = self.field.x + (((Settings.field_cells_x - len(self.template)) // 2) *
                                 Settings.field_cells_size)
        self.y = self.field.y
        self.reload_sprites()
