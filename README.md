# Python Sudoku Solver

This project uses Python to solve Sudoku puzzles. Currently, the algorithm implemented utilizes backtracking recursion.

## Usage

Run the program with the following command
```bash
python3 main.py
```
The program will ask for a file containing the unsolved puzzle. It should be formatted in nine rows with spaces between each of the nine columns. Empty cells should be filled with zero. An example follows
```
0 0 0 2 6 0 7 0 1
6 8 0 0 7 0 0 9 0
1 9 0 0 0 4 5 0 0
8 2 0 1 0 0 0 4 0
0 0 4 6 0 2 9 0 0
0 5 0 0 0 3 0 2 8
0 0 9 3 0 0 0 7 4
0 4 0 0 5 0 0 3 6
7 0 3 0 1 8 0 0 0
```
Note that recursion is not as optimized in Python as it is in some functional languages. Python has no tail call optimization and a fairly low maximum recursion depth (1000), although this number can be adjusted.
