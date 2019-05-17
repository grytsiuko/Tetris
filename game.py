import pygame

from field import Field
from settings import Settings


class Game:

    def __init__(self, screen, shift):
        self.screen = screen
        self.shift = shift
        self.field = Field(self.screen, self.shift + Settings.field_margin, Settings.field_margin)

        self.score = 0
        self.high_score = 9718

        self.score_label = Settings.font.render('SCORE', 1, Settings.game_text_color)
        self.high_score_label = Settings.font.render('HIGHSCORE', 1, Settings.game_text_color)
        self.high_score_num = Settings.score_font.render(str(self.high_score), 1, Settings.game_text_color)
        self.score_num = Settings.score_font.render(str(self.score), 1, Settings.game_text_color)

        self.timer = pygame.time.Clock()
        self.passed_time = 0

    def refresh(self):
        self.passed_time += self.timer.tick()
        delay = Settings.game_delay
        if self.field.falling_figure.moving_fast:
            delay = Settings.game_short_delay
        if self.passed_time > delay:
            self.score += 1
            self.field.make_step()
            self.passed_time = 0

        self.score_num = Settings.score_font.render(str(self.score), 1, Settings.game_text_color)

        # show score and highscore labels
        self.screen.blit(self.score_label, (self.shift + Settings.field_width_with_margin +
                                            (Settings.game_text_width - self.score_label.get_width()) / 2,
                                            Settings.single_screen_height * 0.3))
        self.screen.blit(self.high_score_label, (self.shift + Settings.field_width_with_margin +
                                                 (Settings.game_text_width - self.high_score_label.get_width()) / 2,
                                                 Settings.single_screen_height * 0.5))

        # show score and highscore numbers
        self.screen.blit(self.score_num, (self.shift + Settings.field_width_with_margin +
                                          (Settings.game_text_width - self.score_num.get_width()) / 2,
                                          Settings.single_screen_height * 0.35))
        self.screen.blit(self.high_score_num, (self.shift + Settings.field_width_with_margin +
                                               (Settings.game_text_width - self.high_score_num.get_width()) / 2,
                                               Settings.single_screen_height * 0.55))

        self.field.refresh()

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.field.falling_figure.rotate_clock_wise()
            elif event.key == pygame.K_LEFT:
                self.field.falling_figure.move_left()
            elif event.key == pygame.K_RIGHT:
                self.field.falling_figure.move_right()
            elif event.key == pygame.K_DOWN:
                self.field.falling_figure.moving_fast = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.field.falling_figure.moving_fast = False
