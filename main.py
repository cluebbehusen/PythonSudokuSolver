import solver
from grid import Grid

if __name__ == '__main__':
    file = input('Enter name of Sudoku file: ')
    grid = Grid(file)
    print(grid)
    if not solver.backtracking_solve(grid):
        print('Failed to solve puzzle.')
