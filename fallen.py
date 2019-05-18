from settings import Settings
from pygame.sprite import Group

from square import Square


class Fallen:

    def __init__(self, field, x, y):
        self.field = field
        self.x = x
        self.y = y
        self.group = Group()
        self.matrix = list()
        for i in range(Settings.field_cells_y):
            self.matrix.append(list())
            for k in range(Settings.field_cells_x):
                self.matrix[-1].append(None)
        self.create_simulated_row()

    def create_simulated_row(self):
        row = []
        for i in range(Settings.field_cells_x):
            row.append(Square(self.x + Settings.field_cells_size * i,
                              self.y + Settings.field_height, empty=True))
        self.matrix.append(row)

    def draw(self):
        self.group.empty()
        for i in range(Settings.field_cells_y + 1):
            for k in range(Settings.field_cells_x):
                if self.matrix[i][k] is not None:
                    self.group.add(self.matrix[i][k])
        self.group.draw(self.field.screen)
