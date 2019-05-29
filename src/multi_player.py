import pygame
import sys

from src.alert import Alert
from src.settings import Settings
from src.button import Button
from src.game import Game


class MultiPlayer:

    def __init__(self):

        self.screen = pygame.display.set_mode((Settings.multi_screen_width,
                                               Settings.screen_height))

        self.menu_button = Button(self.screen,
                                  (Settings.multi_screen_width - Settings.button_width) // 2,
                                  Settings.screen_height * 0.9,
                                  'BACK TO MENU')

        self.game1 = Game(self.screen, 0,
                          pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_ESCAPE)
        self.game2 = Game(self.screen, Settings.single_screen_width,
                          pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE)

        self.winner_alert = None

    def run(self):

        while True:
            for event in pygame.event.get():
                self.game1.check_event(event)
                self.game2.check_event(event)
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if self.menu_button.rect.collidepoint(mouse):
                        return 'menu'
            self.screen.blit(Settings.bg_image, (0, 0))
            self.menu_button.show()
            self.game1.refresh()
            self.game2.refresh()

            if self.game1.over and self.game2.over:
                if self.winner_alert is None:
                    self.init_winner_label()
                self.winner_alert.draw()

            pygame.display.flip()

    def init_winner_label(self):

        score_difference = self.game2.score - self.game1.score
        if score_difference < 0:
            self.winner_alert = Alert(self.screen, 'PLAYER 1 WON!', Settings.font_result,
                                      Settings.multi_screen_width // 2, Settings.screen_height * 0.5)
        elif score_difference > 0:
            self.winner_alert = Alert(self.screen, 'PLAYER 2 WON!', Settings.font_result,
                                      Settings.multi_screen_width // 2, Settings.screen_height * 0.5)
        else:
            self.winner_alert = Alert(self.screen, 'IT\'S A TIE!', Settings.font_result,
                                      Settings.multi_screen_width // 2, Settings.screen_height * 0.5)
