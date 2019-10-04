# SUDOKU SOLVER

import tkinter as tk
import sudoku_board


# Function to solve the sudoku board
def solve_sudoku(b):
    # Finds the first blank grid of sudoku board
    find = find_blank(b)

    # If there is no blank grid left then the board is solved
    if not find:
        return True
    else:
        row, col = find

    # Indexing from 1 to 9 to check the valid number for the grid
    for num in range(1, 10):
        if is_valid(b, num, (row, col)):
            b[row][col] = num

            # Recursive function call and backtrack the function
            if solve_sudoku(b):
                return True

            # If 'num' is not valid in future steps
            b[row][col] = 0

    # If there is no valid result for 'index' in board for tis step
    return False


# Check for valid number in the given index
def is_valid(b, num, index):
    # Check row for validation
    for i in range(9):
        if b[index[0]][i] == num and index[1] != i:
            return False

    # Check column for validation
    for i in range(9):
        if b[i][index[1]] == num and index[0] != i:
            return False

    # Check inner squares for validation
    x = index[0] // 3
    y = index[1] // 3

    for i in range(x * 3, x * 3 + 3):
        for j in range(y * 3, y * 3 + 3):
            if b[i][j] == num and (i, j) != index:
                return False

    # If the number is valid
    return True


# Find the first blank grid in the board
def find_blank(b):
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                return i, j

    # If there is no blank grid left in the board
    return None


# To enter the board
root1 = tk.Tk()
sudoku_board.EntryBoard(root1)
root1.mainloop()

board = sudoku_board.board
solve_sudoku(board)
sudoku_board.board = board

# To display the board
root2 = tk.Tk()
sudoku_board.DisplayBoard(root2)
root2.mainloop()
