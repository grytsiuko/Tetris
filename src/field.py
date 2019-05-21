import pygame
from pygame.sprite import Group

from settings import Settings
from figure import Figure
from fallen import Fallen
from square import Square


class Field:

    def __init__(self, game, screen, x, y):

        self.game = game
        self.screen = screen
        self.x = x
        self.y = y

        self.border_rect = pygame.rect.Rect(self.x - Settings.field_border_width,
                                            self.y - Settings.field_border_width,
                                            Settings.field_width + 2 * Settings.field_border_width,
                                            Settings.field_height + 2 * Settings.field_border_width)

        left_edge = Square(self.x - Settings.field_height,
                           self.y,
                           size=Settings.field_height)
        right_edge = Square(self.x + Settings.field_cells_x * Settings.field_cells_size,
                            self.y,
                            size=Settings.field_height)
        self.edges = Group(left_edge, right_edge)

        self.falling_figure = None
        self.next_figure = Figure(self)
        self.fallen = Fallen(self.screen, self.x, self.y)
        self.landed = 0

        self.barriers = [self.edges, self.fallen.group]

        self.timer = pygame.time.Clock()
        self.passed_time = 0

        self.pause = False

    def refresh(self):

        self.fallen.draw()
        pygame.draw.rect(self.screen, Settings.field_border_color,
                         self.border_rect, Settings.field_border_width)
        self.next_figure.draw()

        if not self.game.over:
            self.update()
        if self.falling_figure is not None:
            self.falling_figure.draw()

    def update(self):

        if self.falling_figure is not None:
            self.passed_time += self.timer.tick()
            delay_needed = self.falling_figure.move_delay * \
                           (Settings.game_delay_reduction ** (self.landed // Settings.game_delay_steps))
            if self.passed_time > delay_needed:
                self.passed_time = 0
                self.falling_figure.move_down()
                self.check_landing()

        elif self.fallen.moving_frames_left:
            self.fallen.shift_down()

        elif not self.fallen.available_to_move():
            self.falling_figure = self.next_figure
            self.falling_figure.move_to_field()
            self.next_figure = Figure(self)
            self.check_game_over()
            self.passed_time = 0

    def check_game_over(self):

        if pygame.sprite.groupcollide(self.fallen.group, self.falling_figure.group, False, False):
            self.game.over = True

    def check_landing(self):

        if pygame.sprite.groupcollide(self.fallen.group, self.falling_figure.group, False, False):
            self.falling_figure.move_up()
            self.add_figure_to_fallen()
            self.falling_figure = None
            self.game.score += Settings.game_score_landing
            self.fallen.check_rows()
            removed = len(self.fallen.removed_rows)
            self.game.score += Settings.game_score_row[removed]
            self.game.update_high_score()

    def add_figure_to_fallen(self):

        for square in self.falling_figure.group.sprites():
            row = (square.rect.y - self.x) // Settings.field_cells_size
            col = (square.rect.x - self.x) // Settings.field_cells_size
            self.fallen.matrix[row][col] = square
            self.fallen.group.add(square)
            self.landed += 1
