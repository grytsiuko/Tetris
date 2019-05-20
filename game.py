import pygame

from field import Field
from settings import Settings


class Game:

    def __init__(self, screen, x_shift, key_left, key_right, key_rotate, key_faster):
        self.screen = screen
        self.x_shift = x_shift
        self.field = Field(self.screen, self.x_shift + Settings.field_margin, Settings.field_margin)

        self.high_score = Game.get_high_score()

        self.score_label = Settings.font.render('SCORE', 1, Settings.game_text_color)
        self.high_score_label = Settings.font.render('HIGHSCORE', 1, Settings.game_text_color)
        self.high_score_num = Settings.score_font.render(str(self.high_score), 1, Settings.game_text_color)
        self.score_num = Settings.score_font.render(str(self.field.score), 1, Settings.game_text_color)

        self.key_left = key_left
        self.key_right = key_right
        self.key_rotate = key_rotate
        self.key_faster = key_faster

    @staticmethod
    def get_high_score():
        return 9718

    def refresh(self):
        self.refresh_labels()
        self.field.refresh()

    def refresh_labels(self):

        self.score_num = Settings.score_font.render(str(self.field.score), 1, Settings.game_text_color)

        # show score and highscore labels
        self.screen.blit(self.score_label, (self.x_shift + Settings.field_width_with_margin +
                                            (Settings.game_text_width - self.score_label.get_width()) / 2,
                                            Settings.single_screen_height * 0.3))
        self.screen.blit(self.high_score_label, (self.x_shift + Settings.field_width_with_margin +
                                                 (Settings.game_text_width - self.high_score_label.get_width()) / 2,
                                                 Settings.single_screen_height * 0.5))

        # show score and highscore numbers
        self.screen.blit(self.score_num, (self.x_shift + Settings.field_width_with_margin +
                                          (Settings.game_text_width - self.score_num.get_width()) / 2,
                                          Settings.single_screen_height * 0.35))
        self.screen.blit(self.high_score_num, (self.x_shift + Settings.field_width_with_margin +
                                               (Settings.game_text_width - self.high_score_num.get_width()) / 2,
                                               Settings.single_screen_height * 0.55))

    def check_event(self, event):
        if self.field.falling_figure is None:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_rotate:
                self.field.falling_figure.rotate_clock_wise()
            elif event.key == self.key_left:
                self.field.falling_figure.move_left()
            elif event.key == self.key_right:
                self.field.falling_figure.move_right()
            elif event.key == self.key_faster:
                self.field.falling_figure.move_delay = Settings.game_short_delay
        if event.type == pygame.KEYUP:
            if event.key == self.key_faster:
                self.field.falling_figure.move_delay = Settings.game_delay
