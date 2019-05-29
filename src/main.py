import pygame

from src.menu import Menu
from src.single_player import SinglePlayer
from src.multi_player import MultiPlayer


class Main:

    @staticmethod
    def run():

        pygame.init()
        pygame.display.set_caption('Tetris')
        switch_status = 'menu'

        while True:
            if switch_status == 'menu':
                menu = Menu()
                switch_status = menu.run()
            elif switch_status == 'single player':
                single_player = SinglePlayer()
                switch_status = single_player.run()
            elif switch_status == 'multi player':
                multi_player = MultiPlayer()
                switch_status = multi_player.run()
