import pygame
import sys

from src.settings import Settings
from src.button import Button


class Menu:

    def __init__(self):

        self.screen = pygame.display.set_mode((Settings.single_screen_width,
                                               Settings.screen_height))

        self.screen.blit(Settings.bg_image, (0, 0))

        header = Settings.font_header.render('TETRIS', 1, Settings.font_color)
        self.screen.blit(header, ((Settings.single_screen_width - header.get_width()) / 2,
                                  Settings.screen_height * 0.1))

        self.single_play_button = Button(self.screen,
                                         (Settings.single_screen_width - Settings.button_width) // 2,
                                         Settings.screen_height * 0.4,
                                         'SINGLE PLAYER')
        self.multi_play_button = Button(self.screen,
                                        (Settings.single_screen_width - Settings.button_width) // 2,
                                        Settings.screen_height * 0.6,
                                        'MULTI PLAYER')
        self.exit_button = Button(self.screen,
                                  (Settings.single_screen_width - Settings.button_width) // 2,
                                  Settings.screen_height * 0.8,
                                  'EXIT')

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if self.single_play_button.rect.collidepoint(mouse):
                        return 'single player'
                    elif self.multi_play_button.rect.collidepoint(mouse):
                        return 'multi player'
                    elif self.exit_button.rect.collidepoint(mouse):
                        sys.exit()
            pygame.display.flip()
