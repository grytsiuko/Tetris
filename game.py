from field import Field
from settings import Settings


class Game:

    def __init__(self, screen, shift):
        self.screen = screen
        self.shift = shift
        self.field = Field(self.screen, self.shift + Settings.field_margin, Settings.field_margin)

        # show score and highscore labels
        self.score_label = Settings.font.render('SCORE', 1, Settings.game_text_color)
        self.screen.blit(self.score_label, (self.shift + Settings.field_width_with_margin +
                                            (Settings.game_text_width - self.score_label.get_width()) / 2,
                                            Settings.single_screen_height * 0.3))
        self.high_score_label = Settings.font.render('HIGHSCORE', 1, Settings.game_text_color)
        self.screen.blit(self.high_score_label, (self.shift + Settings.field_width_with_margin +
                                                 (Settings.game_text_width - self.high_score_label.get_width()) / 2,
                                                 Settings.single_screen_height * 0.5))

        self.score = 0
        self.high_score = 9718

        # show score and highscore numbers
        self.score_num = Settings.score_font.render(str(self.score), 1, Settings.game_text_color)
        self.screen.blit(self.score_num, (self.shift + Settings.field_width_with_margin +
                                          (Settings.game_text_width - self.score_num.get_width()) / 2,
                                          Settings.single_screen_height * 0.35))
        self.high_score_num = Settings.score_font.render(str(self.high_score), 1, Settings.game_text_color)
        self.screen.blit(self.high_score_num, (self.shift + Settings.field_width_with_margin +
                                               (Settings.game_text_width - self.high_score_num.get_width()) / 2,
                                               Settings.single_screen_height * 0.55))
