import pygame
import sys

from settings import Settings
from button import Button


class Menu:

    def __init__(self):

        self.screen = pygame.display.set_mode((Settings.single_screen_width, Settings.single_screen_height))

        self.screen.blit(Settings.bg_image, (0, 0))

        header = Settings.header_font.render('TETRIS', 1, Settings.header_color)
        self.screen.blit(header, ((Settings.single_screen_width - header.get_width()) / 2,
                                  Settings.single_screen_height * 0.1))

        self.single_play_button = Button(self.screen,
                                         (Settings.single_screen_width - Settings.button_width) // 2,
                                         Settings.single_screen_height * 0.4,
                                         'SINGLE PLAY')
        self.multi_play_button = Button(self.screen,
                                        (Settings.single_screen_width - Settings.button_width) // 2,
                                        Settings.single_screen_height * 0.6,
                                        'MULTI PLAY')
        self.exit_button = Button(self.screen,
                                  (Settings.single_screen_width - Settings.button_width) // 2,
                                  Settings.single_screen_height * 0.8,
                                  'EXIT')

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if self.single_play_button.rect.collidepoint(mouse):
                        return 'single play'
                    elif self.multi_play_button.rect.collidepoint(mouse):
                        return 'multi play'
                    elif self.exit_button.rect.collidepoint(mouse):
                        sys.exit()
            pygame.display.flip()
            # pygame.time.delay(20)
