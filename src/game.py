import pygame

from alert import Alert
from field import Field
from settings import Settings


class Game:

    def __init__(self, screen, x_shift, key_left, key_right, key_rotate, key_faster, key_pause):

        self.screen = screen
        self.x_shift = x_shift
        self.field = Field(self, self.screen,
                           self.x_shift + Settings.field_margin, Settings.field_margin)

        self.score = 0
        self.high_score = Game.get_high_score()

        self.pause_label = Settings.font_header.render('PAUSE', 1, Settings.font_color)
        self.score_label = Settings.font.render('SCORE', 1, Settings.font_color)
        self.high_score_label = Settings.font.render('HIGHSCORE', 1, Settings.font_color)
        self.new_high_score_label = Settings.font.render('NEW HIGHSCORE!', 1, Settings.font_color)
        self.high_score_num = Settings.font_medium.render(str(self.high_score), 1, Settings.font_color)
        self.score_num = Settings.font_medium.render(str(self.score), 1, Settings.font_color)

        self.game_over_alert = Alert(self.screen, 'GAME OVER!', Settings.font_medium,
                                     self.x_shift + Settings.single_screen_width // 2,
                                     Settings.screen_height * 0.2)

        self.key_left = key_left
        self.key_right = key_right
        self.key_rotate = key_rotate
        self.key_faster = key_faster
        self.key_pause = key_pause

        self.over = False
        self.pause = False

    def update_high_score(self):

        if self.score < self.high_score:
            return
        file = open(Settings.high_score_file_name, 'w')
        file.write(str(self.score) + '\n')
        file.close()

    @staticmethod
    def get_high_score():

        file = open(Settings.high_score_file_name)
        score_str = file.read()
        file.close()
        try:
            return int(score_str)
        except ValueError:
            return 0

    def refresh(self):

        if self.pause:
            self.screen.blit(self.pause_label,
                             (self.x_shift +
                              (Settings.single_screen_width - self.pause_label.get_width()) / 2,
                              Settings.screen_height * 0.3))
        else:
            self.field.refresh()
            self.refresh_labels()

    def refresh_labels(self):

        self.score_num = Settings.font_medium.render(str(self.score), 1, Settings.font_color)

        self.screen.blit(self.score_label,
                         (self.x_shift + Settings.field_width_with_margin +
                          (Settings.game_side_width - self.score_label.get_width()) / 2,
                          Settings.screen_height * 0.3))
        self.screen.blit(self.high_score_label,
                         (self.x_shift + Settings.field_width_with_margin +
                          (Settings.game_side_width - self.high_score_label.get_width()) / 2,
                          Settings.screen_height * 0.5))
        self.screen.blit(self.score_num,
                         (self.x_shift + Settings.field_width_with_margin +
                          (Settings.game_side_width - self.score_num.get_width()) / 2,
                          Settings.screen_height * 0.35))
        self.screen.blit(self.high_score_num,
                         (self.x_shift + Settings.field_width_with_margin +
                          (Settings.game_side_width - self.high_score_num.get_width()) / 2,
                          Settings.screen_height * 0.55))

        if self.high_score < self.score:
            self.screen.blit(self.new_high_score_label,
                             (self.x_shift + Settings.field_width_with_margin +
                              (Settings.game_side_width - self.new_high_score_label.get_width()) / 2,
                              Settings.screen_height * 0.25))

        if self.over:
            self.game_over_alert.draw()

    def check_event(self, event):

        if self.over:
            return

        if event.type == pygame.KEYDOWN:
            if event.key == self.key_pause:
                self.pause = not self.pause
            elif self.field.falling_figure is None or self.pause:
                return
            elif event.key == self.key_rotate:
                self.field.falling_figure.rotate_clock_wise()
            elif event.key == self.key_left:
                self.field.falling_figure.move_left()
            elif event.key == self.key_right:
                self.field.falling_figure.move_right()
            elif event.key == self.key_faster:
                self.field.falling_figure.move_delay = Settings.game_delay_short

        if event.type == pygame.KEYUP:
            if self.field.falling_figure is None:
                return
            if event.key == self.key_faster:
                self.field.falling_figure.move_delay = Settings.game_delay
