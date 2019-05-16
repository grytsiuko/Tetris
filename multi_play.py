import pygame
import sys

from settings import Settings
from button import Button


class MultiPlay:

    def __init__(self):

        self.screen = pygame.display.set_mode((Settings.multi_screen_width, Settings.multi_screen_height))

        self.screen.blit(Settings.bg_image, (0, 0))

        self.menu_button = Button(self.screen,
                                  (Settings.multi_screen_width - Settings.button_width) // 2,
                                  Settings.multi_screen_height * 0.9,
                                  'BACK TO MENU')

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if self.menu_button.rect.collidepoint(mouse):
                        return 'menu'
            pygame.display.flip()
            # pygame.time.delay(20)
