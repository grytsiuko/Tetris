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
        self.score = 0

        # border around the field
        self.border = pygame.rect.Rect(self.x - Settings.field_border_width,
                                       self.y - Settings.field_border_width,
                                       Settings.field_width + 2 * Settings.field_border_width,
                                       Settings.field_height + 2 * Settings.field_border_width)

        self.left_edge = Square(self.x - Settings.field_height,
                                self.y,
                                size=Settings.field_height)
        self.right_edge = Square(self.x + Settings.field_cells_x * Settings.field_cells_size,
                                 self.y,
                                 size=Settings.field_height)
        self.edges = Group()
        self.edges.add(self.left_edge, self.right_edge)

        self.falling_figure = None
        self.fallen = Fallen(self.screen, self.x, self.y)

        self.barriers = [self.edges, self.fallen.group]

        self.timer = pygame.time.Clock()
        self.passed_time = 0

        self.pause = False

    def refresh(self):
        self.fallen.draw()
        pygame.draw.rect(self.screen, Settings.field_border_color,
                         self.border, Settings.field_border_width)
        if not self.game.over:
            self.update()
        if self.falling_figure is not None:
            self.falling_figure.draw()

    def update(self):
        if self.falling_figure is not None:
            self.passed_time += self.timer.tick()
            if self.passed_time > self.falling_figure.move_delay:
                self.passed_time = 0
                self.falling_figure.move_down()
                self.check_landing()
        elif self.fallen.moving_frames_left:
            self.fallen.shift_down()
        elif not self.fallen.available_to_move():
            self.falling_figure = Figure(self, self.x, self.y)
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
            self.score += Settings.game_score_landing
            self.fallen.check_rows()
            rows_filled = len(self.fallen.removed_rows)
            self.score += Settings.game_score_row[rows_filled]
            self.game.update_high_score()

    def add_figure_to_fallen(self):
        for square in self.falling_figure.group.sprites():
            row = (square.rect.y - self.x) // Settings.field_cells_size
            col = (square.rect.x - self.x) // Settings.field_cells_size
            self.fallen.matrix[row][col] = square
            self.fallen.group.add(square)
