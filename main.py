import pygame

from menu import Menu
from single_play import SinglePlay
from multi_play import MultiPlay


class Main:

    @staticmethod
    def run():
        pygame.init()
        switch_status = 'menu'

        while True:
            if switch_status == 'menu':
                menu = Menu()
                switch_status = menu.run()
            elif switch_status == 'single play':
                single_play = SinglePlay()
                switch_status = single_play.run()
            elif switch_status == 'multi play':
                multi_play = MultiPlay()
                switch_status = multi_play.run()


Main.run()
