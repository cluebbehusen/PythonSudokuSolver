class Cell:

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        if x in range(0,2):
            if y in range(0,2):
                self.region = 0
            elif y in range(3,5):
                self.region = 1
            elif y in range(6,8):
                self.region = 2
        elif x in range(3,5):
            if y in range(0,2):
                self.region = 3
            elif y in range(3,5):
                self.region = 4
            elif y in range(6,8):
                self.region = 5
        elif x in range(6,8):
            if y in range(0,2):
                self.region = 6
            elif y in range(3,5):
                self.region = 7
            elif y in range(6,8):
                self.region = 8

    def __str__(self):
        return str(self.value)


class Grid:

    def __init__(self):
        self.grid = [[Cell(x, y, 0) for x in range(9)] for y in range(9)]

    def __str__(self):
        return_string = ''
        for row in self.grid:
            return_string += '['
            for cell in row:
                return_string += str(cell) + ' '
            return_string = return_string[0:-1]
            return_string += ']\n'
        return_string = return_string[0:-1]
        return return_string

    def change_cell(self, x, y, new_value):
        try:
            self.grid[x][y].value = new_value
        except Exception as e:
            print(e)
            print('Attempted to access invalid index.')

    def get_empty_cell(self):
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    return (cell.x, cell.y)
        return False

    def check_row_validity(self, target_cell):
        for cell in self.grid[x]:
            if cell == target_cell.value:
                return False
        return True

    def check_col_validity(self, target_cell):
        for row in self.grid:
            if row[y] == target_cell.value:
                return False
        return True

    def check_region_validity(self, target_cell):
        for row in self.grid:
            for cell in row:
                if cell.x == target_cell.x and cell.y == target_cell.y:
                    pass
                elif (cell.region == target_cell.region) and
                   (cell.value == target_cell.value):
                   return False
        return True

    def check_validity(self, target_cell):
        return (check_row_validity(target_cell) and
                check_col_validity(target_cell) and
                check_region_validity(target_cell))
