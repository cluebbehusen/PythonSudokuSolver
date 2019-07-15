class Cell:
    """Cell object to hold information about each cell in grid."""

    def __init__(self, x, y, value):
        # It is useful for the cell to contain information about its location.
        self.x = int(x)
        self.y = int(y)
        self.value = int(value)
        # Check if the cell is given or not.
        if self.value == 0:
            self.given = False
        else:
            self.given = True
        # Find region for the cell.
        if x in range(0,3):
            if y in range(0,3):
                self.region = 0
            elif y in range(3,6):
                self.region = 1
            elif y in range(6,9):
                self.region = 2
        elif x in range(3,6):
            if y in range(0,3):
                self.region = 3
            elif y in range(3,6):
                self.region = 4
            elif y in range(6,9):
                self.region = 5
        elif x in range(6,9):
            if y in range(0,3):
                self.region = 6
            elif y in range(3,6):
                self.region = 7
            elif y in range(6,9):
                self.region = 8

    def __str__(self):
        # Visualization of the grid is easier if empty cells do not hold zero
        if self.value == 0:
            return '-'
        return str(self.value)


class Grid:

    def __init__(self, file):
        self.grid = []
        x = 0
        # Gather and create cells from given file.
        with open (file, 'r') as grid_file:
            for line in grid_file:
                y = 0
                cell_list = []
                line = line.strip()
                value_list = list(line.split(' '))
                for value in value_list:
                    cell_list.append(Cell(x, y, value))
                    y += 1
                self.grid.append(cell_list)
                x += 1

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

    def get_empty_cell(self):
        """Finds the next empty cell in the grid."""
        x = 0
        y = 0
        for row in self.grid:
            for cell in row:
                # Rather than going row by row, work down in a square shape to increase speed.
                if y > x and self.grid[x][y].value == 0:
                    return self.grid[x][y]
                if cell.value == 0:
                    return cell
                y += 1
            y = 0
            x += 1
        return False

    def check_row_validity(self, target_cell, test_value):
        """Checks if a test value is valid in the current row."""
        for cell in self.grid[target_cell.x]:
            if cell.x == target_cell.x and cell.y == target_cell.y:
                pass
            elif cell.value == test_value:
                return False
        return True

    def check_col_validity(self, target_cell, test_value):
        """Checks if a test value is valid in the current column."""
        for row in self.grid:
            cell = row[target_cell.y]
            if cell.x == target_cell.x and cell.y == target_cell.y:
                pass
            elif row[target_cell.y].value == test_value:
                return False
        return True

    def check_region_validity(self, target_cell, test_value):
        """Checks if a test value is valid in the current region."""
        for row in self.grid:
            for cell in row:
                if cell.x == target_cell.x and cell.y == target_cell.y:
                    pass
                elif ((cell.region == target_cell.region) and
                     (cell.value == test_value)):
                   return False
        return True

    def check_validity(self, target_cell, test_value):
        """Checks and returns result of all validity checks"""
        return (self.check_row_validity(target_cell, test_value) and
                self.check_col_validity(target_cell, test_value) and
                self.check_region_validity(target_cell, test_value))
