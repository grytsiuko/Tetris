import pygame


class Settings:
    bg_image = pygame.image.load('bg.jpg')

    single_screen_width = 800
    single_screen_height = 700
    multi_screen_width = 1500
    multi_screen_height = 700

    button_width = 230
    button_height = 50
    button_text_color = (255, 255, 255)
    button_bg_color = (30, 30, 30)
    button_border_color = (255, 255, 255)

    pygame.font.init()
    font = pygame.font.SysFont("Helvetica", 27)
    header_font = pygame.font.SysFont("Helvetica", 140, bold=True)
    header_color = (255, 255, 255)
