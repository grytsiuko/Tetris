import pygame


class Settings:
    bg_image = pygame.image.load('img/bg.jpg')
    high_score_file_name = 'data/high_score.dat'

    single_screen_width = 600
    multi_screen_width = single_screen_width * 2
    screen_height = 750

    field_width = 300
    field_height = 600
    field_border_color = (255, 255, 255)
    field_border_width = 2
    field_margin = 20
    field_width_with_margin = field_width + 2 * field_margin
    field_cells_size = 30
    field_cells_x = field_width // field_cells_size
    field_cells_y = field_height // field_cells_size
    field_cells_border_color = (255, 255, 255)
    field_cells_falling_shift = 1
    field_cells_falling_frames = field_cells_size // field_cells_falling_shift

    game_side_width = single_screen_width - field_width_with_margin
    game_delay = 400
    game_delay_short = 50
    game_delay_reduction = 0.95
    game_delay_steps = 10
    game_score_landing = 10
    game_score_row = [0, 300, 1000, 2000, 4000]
    game_score_star = 100

    button_width = 230
    button_height = 50
    button_text_color = (255, 255, 255)
    button_bg_color = (30, 30, 30)
    button_border_color = (255, 255, 255)

    alert_bg_color = (0, 0, 0)
    alert_bg_alpha = 200
    alert_label_margin = 0.05

    pygame.font.init()
    font = pygame.font.SysFont("Helvetica", 25)
    font_header = pygame.font.SysFont("Helvetica", 140, bold=True)
    font_medium = pygame.font.SysFont("Helvetica", 70, bold=True)
    font_result = pygame.font.SysFont("Helvetica", 120, bold=True)
    font_color = (255, 255, 255)

    figure_star_probability = 0.2
    figure_star_img = pygame.image.load('img/star.png')
    figure_star_img = pygame.transform.scale(figure_star_img, (field_cells_size, field_cells_size))
    figure_colors = [
        (150, 0, 0),
        (0, 150, 0),
        (0, 0, 150),
        (0, 150, 150),
        (150, 0, 150),
        (150, 150, 0),
    ]

    figures_storage = [

        [
            [
                [0, 1, 1],
                [0, 1, 0],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 1]
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 0]
            ],
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ],
        ],

        [
            [
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 0],
            ],
            [
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 1]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [1, 0, 0]
            ],
        ],

        [
            [
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0],
            ],
            [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 0, 1]
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [1, 1, 0],
            ],
        ],

        [
            [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1],
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [1, 0, 0]
            ],
            [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0]
            ],
        ],

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
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [0, 1, 0],
            ],
        ],

        [
            [
                [1, 1],
                [1, 1],
            ],
            [
                [1, 1],
                [1, 1],
            ],
            [
                [1, 1],
                [1, 1],
            ],
            [
                [1, 1],
                [1, 1],
            ],
        ]

    ]
