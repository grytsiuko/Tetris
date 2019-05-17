import pygame


class Settings:
    bg_image = pygame.image.load('bg.jpg')

    single_screen_width = 600
    single_screen_height = 750
    multi_screen_width = single_screen_width * 2
    multi_screen_height = single_screen_height

    field_width = 200
    field_height = 600
    field_border_color = (255, 255, 255)
    field_border_width = 2
    field_margin = 10
    field_width_with_margin = field_width + 2 * field_margin
    field_cells_size = 20
    field_cells_x = field_width // field_cells_size
    field_cells_y = field_height // field_cells_size
    field_cells_border_color = (255, 255, 255)

    game_text_color = (255, 255, 255)
    game_text_width = single_screen_width - field_width_with_margin
    game_delay = 400
    game_short_delay = 100

    button_width = 230
    button_height = 50
    button_text_color = (255, 255, 255)
    button_bg_color = (30, 30, 30)
    button_border_color = (255, 255, 255)

    pygame.font.init()
    font = pygame.font.SysFont("Helvetica", 25)
    header_font = pygame.font.SysFont("Helvetica", 140, bold=True)
    score_font = pygame.font.SysFont("Helvetica", 70, bold=True)
    header_color = (255, 255, 255)

    figures_size = 4
    figures_colors = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255)
    ]
    figures_storage = [

        [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0]
            ],
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0]
            ],
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]
            ],
        ],

        [
            [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]
            ],
        ]

    ]
