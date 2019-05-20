import pygame
import sys

from settings import Settings
from button import Button
from game import Game


class MultiPlayer:

    def __init__(self):

        self.screen = pygame.display.set_mode((Settings.multi_screen_width, Settings.multi_screen_height))

        self.menu_button = Button(self.screen,
                                  (Settings.multi_screen_width - Settings.button_width) // 2,
                                  Settings.multi_screen_height * 0.9,
                                  'BACK TO MENU')

        self.game1 = Game(self.screen, 0, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        self.game2 = Game(self.screen, Settings.single_screen_width, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)

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
            pygame.display.flip()
