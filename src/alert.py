import pygame

from src.settings import Settings


class Alert:

    def __init__(self, screen, text, font, centerx, top):

        super().__init__()
        self.screen = screen

        self.label = font.render(text, 1, Settings.font_color)
        self.label_margin = Settings.alert_label_margin * self.label.get_width()

        image_width = self.label.get_width() + 2 * self.label_margin
        image_height = self.label.get_height() + 2 * self.label_margin
        self.image = pygame.Surface((image_width, image_height))

        pygame.draw.rect(self.image, Settings.alert_bg_color, self.image.get_rect())
        self.image.set_alpha(Settings.alert_bg_alpha)

        self.rect = pygame.rect.Rect(0, top, image_width, image_height)
        self.rect.centerx = centerx

    def draw(self):

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.label, self.rect.move(self.label_margin, self.label_margin))
