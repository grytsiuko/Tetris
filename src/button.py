import pygame

from settings import Settings


class Button:
    def __init__(self, screen, x, y, text, width=Settings.button_width, height=Settings.button_height):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.show()

    def show(self):
        self.draw_button()
        self.write_text()

    def write_text(self):
        my_text = Settings.font.render(self.text, 1, Settings.button_text_color)
        self.screen.blit(my_text, ((self.x + self.width / 2) - my_text.get_width() / 2,
                                   (self.y + self.height / 2) - my_text.get_height() / 2))

    def draw_button(self):
        pygame.draw.rect(self.screen, Settings.button_bg_color, self.rect, 0)
        pygame.draw.rect(self.screen, Settings.button_border_color, self.rect, 1)
