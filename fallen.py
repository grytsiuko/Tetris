from settings import Settings
from pygame.sprite import Group

from square import Square


class Fallen:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.matrix = list()
        self.init_matrix()
        self.group = Group()
        for square in self.matrix[-1]:
            self.group.add(square)
        self.to_move = list()
        self.removed_rows = list()
        self.moving_frames_left = 0

    def init_matrix(self):
        for i in range(Settings.field_cells_y):
            self.matrix.append(list())
            for k in range(Settings.field_cells_x):
                self.matrix[-1].append(None)

        # simulated row
        row = []
        for i in range(Settings.field_cells_x):
            row.append(Square(self.x + Settings.field_cells_size * i,
                              self.y + Settings.field_height, empty=True))
        self.matrix.append(row)

    def check_rows(self):
        for i in range(Settings.field_cells_y):
            filled = 0
            for k in range(Settings.field_cells_x):
                if self.matrix[i][k] is None:
                    break
                else:
                    filled += 1
            if filled == Settings.field_cells_x:
                self.removed_rows.append(i)
                for k in range(Settings.field_cells_x):
                    self.matrix[i][k].kill()
                    self.matrix[i][k] = None

    def shift_down(self):
        for square in self.to_move:
            square.rect.y += Settings.field_cells_falling_shift
        self.moving_frames_left -= 1

    def available_to_move(self):
        if len(self.removed_rows) == 0:
            return False
        self.moving_frames_left = Settings.field_cells_size // Settings.field_cells_falling_shift
        self.to_move = list()
        i = self.removed_rows.pop(-1)
        for row in range(i - 1, -1, -1):
            for col in range(Settings.field_cells_x):
                if self.matrix[row][col] is not None:
                    self.to_move.append(self.matrix[row][col])
                    self.matrix[row + 1][col] = self.matrix[row][col]
                    self.matrix[row][col] = None
        for i in range(len(self.removed_rows)):
            self.removed_rows[i] += 1
        return True

    def draw(self):
        self.group.draw(self.screen)
