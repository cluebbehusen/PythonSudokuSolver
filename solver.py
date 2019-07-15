import os

def backtracking_solve(grid):
    # Find the next empty cell
    cell = grid.get_empty_cell()
    if not cell:
        print('== Puzzle Solved ==')
        print(grid)
        return True
    for value in range(1, 10):
        if grid.check_validity(cell, value):
            cell.value = value
            if backtracking_solve(grid):
                return True
            cell.value = 0
    return False
