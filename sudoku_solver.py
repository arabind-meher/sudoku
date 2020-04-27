# SUDOKU SOLVER
class SolveSudoku:
    # Get the board from user
    @staticmethod
    def get_board(board):
        SolveSudoku.solve_sudoku(board)
        if 0 in board:
            return -1
        else:
            return board

    # Function to solve the sudoku board
    @staticmethod
    def solve_sudoku(board):
        # Finds the first blank grid of sudoku board
        find = SolveSudoku.find_blank(board)

        # If there is no blank grid left then the board is solved
        if not find:
            return True
        else:
            row, col = find

        # Indexing from 1 to 9 to check the valid number for the grid
        for num in range(1, 10):
            if SolveSudoku.is_valid(board, num, (row, col)):
                board[row][col] = num

                # Recursive function call and backtrack the function
                if SolveSudoku.solve_sudoku(board):
                    return True

                # If 'num' is not valid in future steps
                board[row][col] = 0

        # If there is no valid result for 'index' in board for tis step
        return False

    # Check for valid number in the given index
    @staticmethod
    def is_valid(board, num, index):
        # Check row for validation
        for i in range(9):
            if board[index[0]][i] == num and index[1] != i:
                return False

        # Check column for validation
        for i in range(9):
            if board[i][index[1]] == num and index[0] != i:
                return False

        # Check inner squares for validation
        x = index[0] // 3
        y = index[1] // 3

        for i in range(x * 3, x * 3 + 3):
            for j in range(y * 3, y * 3 + 3):
                if board[i][j] == num and (i, j) != index:
                    return False

        # If the number is valid
        return True

    # Find the first blank grid in the board
    @staticmethod
    def find_blank(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j

        # If there is no blank grid left in the board
        return None
