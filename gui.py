from tkinter import *
from tkinter import ttk, messagebox

from sudoku_solver import SolveSudoku


class SudokuBoard:
    """Sudoku Board"""

    def __init__(self):
        """Enter the Unsolved Sudoku Board"""
        master = Tk()

        master.title('Sudoku Board')
        master.geometry('327x475')
        master.resizable(0, 0)

        Label(
            master,
            text='ENTER THE NUMBERS',
            font=('hack', 20, 'bold'),
            pady=10,
        ).grid(row=0, column=0, columnspan=9)

        Label(
            master,
            text="**USE '0' FOR BLANK**",
            padx=10
        ).grid(row=1, column=0, columnspan=9)

        style = ttk.Style()
        style.configure('TEntry', bg='black', foreground='green')

        entry00 = IntVar()
        ttk.Entry(master, textvariable=entry00, justify='center', font=('hack', 20), width=2).grid(row=2, column=0)
        entry01 = IntVar()
        ttk.Entry(master, textvariable=entry01, justify='center', font=('hack', 20), width=2).grid(row=2, column=1)
        entry02 = IntVar()
        ttk.Entry(master, textvariable=entry02, justify='center', font=('hack', 20), width=2).grid(row=2, column=2)
        entry03 = IntVar()
        ttk.Entry(master, textvariable=entry03, justify='center', font=('hack', 20), width=2).grid(row=2, column=3)
        entry04 = IntVar()
        ttk.Entry(master, textvariable=entry04, justify='center', font=('hack', 20), width=2).grid(row=2, column=4)
        entry05 = IntVar()
        ttk.Entry(master, textvariable=entry05, justify='center', font=('hack', 20), width=2).grid(row=2, column=5)
        entry06 = IntVar()
        ttk.Entry(master, textvariable=entry06, justify='center', font=('hack', 20), width=2).grid(row=2, column=6)
        entry07 = IntVar()
        ttk.Entry(master, textvariable=entry07, justify='center', font=('hack', 20), width=2).grid(row=2, column=7)
        entry08 = IntVar()
        ttk.Entry(master, textvariable=entry08, justify='center', font=('hack', 20), width=2).grid(row=2, column=8)

        entry10 = IntVar()
        ttk.Entry(master, textvariable=entry10, justify='center', font=('hack', 20), width=2).grid(row=3, column=0)
        entry11 = IntVar()
        ttk.Entry(master, textvariable=entry11, justify='center', font=('hack', 20), width=2).grid(row=3, column=1)
        entry12 = IntVar()
        ttk.Entry(master, textvariable=entry12, justify='center', font=('hack', 20), width=2).grid(row=3, column=2)
        entry13 = IntVar()
        ttk.Entry(master, textvariable=entry13, justify='center', font=('hack', 20), width=2).grid(row=3, column=3)
        entry14 = IntVar()
        ttk.Entry(master, textvariable=entry14, justify='center', font=('hack', 20), width=2).grid(row=3, column=4)
        entry15 = IntVar()
        ttk.Entry(master, textvariable=entry15, justify='center', font=('hack', 20), width=2).grid(row=3, column=5)
        entry16 = IntVar()
        ttk.Entry(master, textvariable=entry16, justify='center', font=('hack', 20), width=2).grid(row=3, column=6)
        entry17 = IntVar()
        ttk.Entry(master, textvariable=entry17, justify='center', font=('hack', 20), width=2).grid(row=3, column=7)
        entry18 = IntVar()
        ttk.Entry(master, textvariable=entry18, justify='center', font=('hack', 20), width=2).grid(row=3, column=8)

        entry20 = IntVar()
        ttk.Entry(master, textvariable=entry20, justify='center', font=('hack', 20), width=2).grid(row=4, column=0)
        entry21 = IntVar()
        ttk.Entry(master, textvariable=entry21, justify='center', font=('hack', 20), width=2).grid(row=4, column=1)
        entry22 = IntVar()
        ttk.Entry(master, textvariable=entry22, justify='center', font=('hack', 20), width=2).grid(row=4, column=2)
        entry23 = IntVar()
        ttk.Entry(master, textvariable=entry23, justify='center', font=('hack', 20), width=2).grid(row=4, column=3)
        entry24 = IntVar()
        ttk.Entry(master, textvariable=entry24, justify='center', font=('hack', 20), width=2).grid(row=4, column=4)
        entry25 = IntVar()
        ttk.Entry(master, textvariable=entry25, justify='center', font=('hack', 20), width=2).grid(row=4, column=5)
        entry26 = IntVar()
        ttk.Entry(master, textvariable=entry26, justify='center', font=('hack', 20), width=2).grid(row=4, column=6)
        entry27 = IntVar()
        ttk.Entry(master, textvariable=entry27, justify='center', font=('hack', 20), width=2).grid(row=4, column=7)
        entry28 = IntVar()
        ttk.Entry(master, textvariable=entry28, justify='center', font=('hack', 20), width=2).grid(row=4, column=8)

        entry30 = IntVar()
        ttk.Entry(master, textvariable=entry30, justify='center', font=('hack', 20), width=2).grid(row=5, column=0)
        entry31 = IntVar()
        ttk.Entry(master, textvariable=entry31, justify='center', font=('hack', 20), width=2).grid(row=5, column=1)
        entry32 = IntVar()
        ttk.Entry(master, textvariable=entry32, justify='center', font=('hack', 20), width=2).grid(row=5, column=2)
        entry33 = IntVar()
        ttk.Entry(master, textvariable=entry33, justify='center', font=('hack', 20), width=2).grid(row=5, column=3)
        entry34 = IntVar()
        ttk.Entry(master, textvariable=entry34, justify='center', font=('hack', 20), width=2).grid(row=5, column=4)
        entry35 = IntVar()
        ttk.Entry(master, textvariable=entry35, justify='center', font=('hack', 20), width=2).grid(row=5, column=5)
        entry36 = IntVar()
        ttk.Entry(master, textvariable=entry36, justify='center', font=('hack', 20), width=2).grid(row=5, column=6)
        entry37 = IntVar()
        ttk.Entry(master, textvariable=entry37, justify='center', font=('hack', 20), width=2).grid(row=5, column=7)
        entry38 = IntVar()
        ttk.Entry(master, textvariable=entry38, justify='center', font=('hack', 20), width=2).grid(row=5, column=8)

        entry40 = IntVar()
        ttk.Entry(master, textvariable=entry40, justify='center', font=('hack', 20), width=2).grid(row=6, column=0)
        entry41 = IntVar()
        ttk.Entry(master, textvariable=entry41, justify='center', font=('hack', 20), width=2).grid(row=6, column=1)
        entry42 = IntVar()
        ttk.Entry(master, textvariable=entry42, justify='center', font=('hack', 20), width=2).grid(row=6, column=2)
        entry43 = IntVar()
        ttk.Entry(master, textvariable=entry43, justify='center', font=('hack', 20), width=2).grid(row=6, column=3)
        entry44 = IntVar()
        ttk.Entry(master, textvariable=entry44, justify='center', font=('hack', 20), width=2).grid(row=6, column=4)
        entry45 = IntVar()
        ttk.Entry(master, textvariable=entry45, justify='center', font=('hack', 20), width=2).grid(row=6, column=5)
        entry46 = IntVar()
        ttk.Entry(master, textvariable=entry46, justify='center', font=('hack', 20), width=2).grid(row=6, column=6)
        entry47 = IntVar()
        ttk.Entry(master, textvariable=entry47, justify='center', font=('hack', 20), width=2).grid(row=6, column=7)
        entry48 = IntVar()
        ttk.Entry(master, textvariable=entry48, justify='center', font=('hack', 20), width=2).grid(row=6, column=8)

        entry50 = IntVar()
        ttk.Entry(master, textvariable=entry50, justify='center', font=('hack', 20), width=2).grid(row=7, column=0)
        entry51 = IntVar()
        ttk.Entry(master, textvariable=entry51, justify='center', font=('hack', 20), width=2).grid(row=7, column=1)
        entry52 = IntVar()
        ttk.Entry(master, textvariable=entry52, justify='center', font=('hack', 20), width=2).grid(row=7, column=2)
        entry53 = IntVar()
        ttk.Entry(master, textvariable=entry53, justify='center', font=('hack', 20), width=2).grid(row=7, column=3)
        entry54 = IntVar()
        ttk.Entry(master, textvariable=entry54, justify='center', font=('hack', 20), width=2).grid(row=7, column=4)
        entry55 = IntVar()
        ttk.Entry(master, textvariable=entry55, justify='center', font=('hack', 20), width=2).grid(row=7, column=5)
        entry56 = IntVar()
        ttk.Entry(master, textvariable=entry56, justify='center', font=('hack', 20), width=2).grid(row=7, column=6)
        entry57 = IntVar()
        ttk.Entry(master, textvariable=entry57, justify='center', font=('hack', 20), width=2).grid(row=7, column=7)
        entry58 = IntVar()
        ttk.Entry(master, textvariable=entry58, justify='center', font=('hack', 20), width=2).grid(row=7, column=8)

        entry60 = IntVar()
        ttk.Entry(master, textvariable=entry60, justify='center', font=('hack', 20), width=2).grid(row=8, column=0)
        entry61 = IntVar()
        ttk.Entry(master, textvariable=entry61, justify='center', font=('hack', 20), width=2).grid(row=8, column=1)
        entry62 = IntVar()
        ttk.Entry(master, textvariable=entry62, justify='center', font=('hack', 20), width=2).grid(row=8, column=2)
        entry63 = IntVar()
        ttk.Entry(master, textvariable=entry63, justify='center', font=('hack', 20), width=2).grid(row=8, column=3)
        entry64 = IntVar()
        ttk.Entry(master, textvariable=entry64, justify='center', font=('hack', 20), width=2).grid(row=8, column=4)
        entry65 = IntVar()
        ttk.Entry(master, textvariable=entry65, justify='center', font=('hack', 20), width=2).grid(row=8, column=5)
        entry66 = IntVar()
        ttk.Entry(master, textvariable=entry66, justify='center', font=('hack', 20), width=2).grid(row=8, column=6)
        entry67 = IntVar()
        ttk.Entry(master, textvariable=entry67, justify='center', font=('hack', 20), width=2).grid(row=8, column=7)
        entry68 = IntVar()
        ttk.Entry(master, textvariable=entry68, justify='center', font=('hack', 20), width=2).grid(row=8, column=8)

        entry70 = IntVar()
        ttk.Entry(master, textvariable=entry70, justify='center', font=('hack', 20), width=2).grid(row=9, column=0)
        entry71 = IntVar()
        ttk.Entry(master, textvariable=entry71, justify='center', font=('hack', 20), width=2).grid(row=9, column=1)
        entry72 = IntVar()
        ttk.Entry(master, textvariable=entry72, justify='center', font=('hack', 20), width=2).grid(row=9, column=2)
        entry73 = IntVar()
        ttk.Entry(master, textvariable=entry73, justify='center', font=('hack', 20), width=2).grid(row=9, column=3)
        entry74 = IntVar()
        ttk.Entry(master, textvariable=entry74, justify='center', font=('hack', 20), width=2).grid(row=9, column=4)
        entry75 = IntVar()
        ttk.Entry(master, textvariable=entry75, justify='center', font=('hack', 20), width=2).grid(row=9, column=5)
        entry76 = IntVar()
        ttk.Entry(master, textvariable=entry76, justify='center', font=('hack', 20), width=2).grid(row=9, column=6)
        entry77 = IntVar()
        ttk.Entry(master, textvariable=entry77, justify='center', font=('hack', 20), width=2).grid(row=9, column=7)
        entry78 = IntVar()
        ttk.Entry(master, textvariable=entry78, justify='center', font=('hack', 20), width=2).grid(row=9, column=8)

        entry80 = IntVar()
        ttk.Entry(master, textvariable=entry80, justify='center', font=('hack', 20), width=2).grid(row=10, column=0)
        entry81 = IntVar()
        ttk.Entry(master, textvariable=entry81, justify='center', font=('hack', 20), width=2).grid(row=10, column=1)
        entry82 = IntVar()
        ttk.Entry(master, textvariable=entry82, justify='center', font=('hack', 20), width=2).grid(row=10, column=2)
        entry83 = IntVar()
        ttk.Entry(master, textvariable=entry83, justify='center', font=('hack', 20), width=2).grid(row=10, column=3)
        entry84 = IntVar()
        ttk.Entry(master, textvariable=entry84, justify='center', font=('hack', 20), width=2).grid(row=10, column=4)
        entry85 = IntVar()
        ttk.Entry(master, textvariable=entry85, justify='center', font=('hack', 20), width=2).grid(row=10, column=5)
        entry86 = IntVar()
        ttk.Entry(master, textvariable=entry86, justify='center', font=('hack', 20), width=2).grid(row=10, column=6)
        entry87 = IntVar()
        ttk.Entry(master, textvariable=entry87, justify='center', font=('hack', 20), width=2).grid(row=10, column=7)
        entry88 = IntVar()
        ttk.Entry(master, textvariable=entry88, justify='center', font=('hack', 20), width=2).grid(row=10, column=8)

        Label(
            master,
            text='PRESS START TO CONTINUE',
            padx=10,
            pady=10
        ).grid(row=11, column=0, columnspan=9)

        def button_clicked():
            board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

            board[0][0] = entry00.get()
            board[0][1] = entry01.get()
            board[0][2] = entry02.get()
            board[0][3] = entry03.get()
            board[0][4] = entry04.get()
            board[0][5] = entry05.get()
            board[0][6] = entry06.get()
            board[0][7] = entry07.get()
            board[0][8] = entry08.get()

            board[1][0] = entry10.get()
            board[1][1] = entry11.get()
            board[1][2] = entry12.get()
            board[1][3] = entry13.get()
            board[1][4] = entry14.get()
            board[1][5] = entry15.get()
            board[1][6] = entry16.get()
            board[1][7] = entry17.get()
            board[1][8] = entry18.get()

            board[2][0] = entry20.get()
            board[2][1] = entry21.get()
            board[2][2] = entry22.get()
            board[2][3] = entry23.get()
            board[2][4] = entry24.get()
            board[2][5] = entry25.get()
            board[2][6] = entry26.get()
            board[2][7] = entry27.get()
            board[2][8] = entry28.get()

            board[3][0] = entry30.get()
            board[3][1] = entry31.get()
            board[3][2] = entry32.get()
            board[3][3] = entry33.get()
            board[3][4] = entry34.get()
            board[3][5] = entry35.get()
            board[3][6] = entry36.get()
            board[3][7] = entry37.get()
            board[3][8] = entry38.get()

            board[4][0] = entry40.get()
            board[4][1] = entry41.get()
            board[4][2] = entry42.get()
            board[4][3] = entry43.get()
            board[4][4] = entry44.get()
            board[4][5] = entry45.get()
            board[4][6] = entry46.get()
            board[4][7] = entry47.get()
            board[4][8] = entry48.get()

            board[5][0] = entry50.get()
            board[5][1] = entry51.get()
            board[5][2] = entry52.get()
            board[5][3] = entry53.get()
            board[5][4] = entry54.get()
            board[5][5] = entry55.get()
            board[5][6] = entry56.get()
            board[5][7] = entry57.get()
            board[5][8] = entry58.get()

            board[6][0] = entry60.get()
            board[6][1] = entry61.get()
            board[6][2] = entry62.get()
            board[6][3] = entry63.get()
            board[6][4] = entry64.get()
            board[6][5] = entry65.get()
            board[6][6] = entry66.get()
            board[6][7] = entry67.get()
            board[6][8] = entry68.get()

            board[7][0] = entry70.get()
            board[7][1] = entry71.get()
            board[7][2] = entry72.get()
            board[7][3] = entry73.get()
            board[7][4] = entry74.get()
            board[7][5] = entry75.get()
            board[7][6] = entry76.get()
            board[7][7] = entry77.get()
            board[7][8] = entry78.get()

            board[8][0] = entry80.get()
            board[8][0] = entry80.get()
            board[8][0] = entry80.get()
            board[8][0] = entry80.get()
            board[8][0] = entry80.get()
            board[8][0] = entry80.get()
            board[8][0] = entry80.get()
            board[8][0] = entry80.get()
            board[8][0] = entry80.get()

            # master.destroy()
            print(board)
            board = SolveSudoku.get_board(board)

            if board == -1:
                messagebox.showwarning('Warning', 'This board contain ERROR')
            else:
                self.display_board(board)

        Button(master, text='START', command=button_clicked, padx=10, pady=10).grid(row=12, column=3, columnspan=3)

        master.mainloop()

    @staticmethod
    def display_board(board):
        master = Tk()

        master.title('Sudoku Board')
        master.geometry('327x400')
        master.resizable(0, 0)

        Button(master, text=board[0][0], bg='gray75', padx=12, pady=10).grid(row=0, column=0)
        Button(master, text=board[0][1], bg='gray75', padx=12, pady=10).grid(row=0, column=1)
        Button(master, text=board[0][2], bg='gray75', padx=12, pady=10).grid(row=0, column=2)
        Button(master, text=board[0][3], bg='gray95', padx=12, pady=10).grid(row=0, column=3)
        Button(master, text=board[0][4], bg='gray95', padx=12, pady=10).grid(row=0, column=4)
        Button(master, text=board[0][5], bg='gray95', padx=12, pady=10).grid(row=0, column=5)
        Button(master, text=board[0][6], bg='gray75', padx=12, pady=10).grid(row=0, column=6)
        Button(master, text=board[0][7], bg='gray75', padx=12, pady=10).grid(row=0, column=7)
        Button(master, text=board[0][8], bg='gray75', padx=12, pady=10).grid(row=0, column=8)

        Button(master, text=board[1][0], bg='gray75', padx=12, pady=10).grid(row=1, column=0)
        Button(master, text=board[1][1], bg='gray75', padx=12, pady=10).grid(row=1, column=1)
        Button(master, text=board[1][2], bg='gray75', padx=12, pady=10).grid(row=1, column=2)
        Button(master, text=board[1][3], bg='gray95', padx=12, pady=10).grid(row=1, column=3)
        Button(master, text=board[1][4], bg='gray95', padx=12, pady=10).grid(row=1, column=4)
        Button(master, text=board[1][5], bg='gray95', padx=12, pady=10).grid(row=1, column=5)
        Button(master, text=board[1][6], bg='gray75', padx=12, pady=10).grid(row=1, column=6)
        Button(master, text=board[1][7], bg='gray75', padx=12, pady=10).grid(row=1, column=7)
        Button(master, text=board[1][8], bg='gray75', padx=12, pady=10).grid(row=1, column=8)

        Button(master, text=board[2][0], bg='gray75', padx=12, pady=10).grid(row=2, column=0)
        Button(master, text=board[2][1], bg='gray75', padx=12, pady=10).grid(row=2, column=1)
        Button(master, text=board[2][2], bg='gray75', padx=12, pady=10).grid(row=2, column=2)
        Button(master, text=board[2][3], bg='gray95', padx=12, pady=10).grid(row=2, column=3)
        Button(master, text=board[2][4], bg='gray95', padx=12, pady=10).grid(row=2, column=4)
        Button(master, text=board[2][5], bg='gray95', padx=12, pady=10).grid(row=2, column=5)
        Button(master, text=board[2][6], bg='gray75', padx=12, pady=10).grid(row=2, column=6)
        Button(master, text=board[2][7], bg='gray75', padx=12, pady=10).grid(row=2, column=7)
        Button(master, text=board[2][8], bg='gray75', padx=12, pady=10).grid(row=2, column=8)

        Button(master, text=board[3][0], bg='gray95', padx=12, pady=10).grid(row=3, column=0)
        Button(master, text=board[3][1], bg='gray95', padx=12, pady=10).grid(row=3, column=1)
        Button(master, text=board[3][2], bg='gray95', padx=12, pady=10).grid(row=3, column=2)
        Button(master, text=board[3][3], bg='gray75', padx=12, pady=10).grid(row=3, column=3)
        Button(master, text=board[3][4], bg='gray75', padx=12, pady=10).grid(row=3, column=4)
        Button(master, text=board[3][5], bg='gray75', padx=12, pady=10).grid(row=3, column=5)
        Button(master, text=board[3][6], bg='gray95', padx=12, pady=10).grid(row=3, column=6)
        Button(master, text=board[3][7], bg='gray95', padx=12, pady=10).grid(row=3, column=7)
        Button(master, text=board[3][8], bg='gray95', padx=12, pady=10).grid(row=3, column=8)

        Button(master, text=board[4][0], bg='gray95', padx=12, pady=10).grid(row=4, column=0)
        Button(master, text=board[4][1], bg='gray95', padx=12, pady=10).grid(row=4, column=1)
        Button(master, text=board[4][2], bg='gray95', padx=12, pady=10).grid(row=4, column=2)
        Button(master, text=board[4][3], bg='gray75', padx=12, pady=10).grid(row=4, column=3)
        Button(master, text=board[4][4], bg='gray75', padx=12, pady=10).grid(row=4, column=4)
        Button(master, text=board[4][5], bg='gray75', padx=12, pady=10).grid(row=4, column=5)
        Button(master, text=board[4][6], bg='gray95', padx=12, pady=10).grid(row=4, column=6)
        Button(master, text=board[4][7], bg='gray95', padx=12, pady=10).grid(row=4, column=7)
        Button(master, text=board[4][8], bg='gray95', padx=12, pady=10).grid(row=4, column=8)

        Button(master, text=board[5][0], bg='gray95', padx=12, pady=10).grid(row=5, column=0)
        Button(master, text=board[5][1], bg='gray95', padx=12, pady=10).grid(row=5, column=1)
        Button(master, text=board[5][2], bg='gray95', padx=12, pady=10).grid(row=5, column=2)
        Button(master, text=board[5][3], bg='gray75', padx=12, pady=10).grid(row=5, column=3)
        Button(master, text=board[5][4], bg='gray75', padx=12, pady=10).grid(row=5, column=4)
        Button(master, text=board[5][5], bg='gray75', padx=12, pady=10).grid(row=5, column=5)
        Button(master, text=board[5][6], bg='gray95', padx=12, pady=10).grid(row=5, column=6)
        Button(master, text=board[5][7], bg='gray95', padx=12, pady=10).grid(row=5, column=7)
        Button(master, text=board[5][8], bg='gray95', padx=12, pady=10).grid(row=5, column=8)

        Button(master, text=board[6][0], bg='gray75', padx=12, pady=10).grid(row=6, column=0)
        Button(master, text=board[6][1], bg='gray75', padx=12, pady=10).grid(row=6, column=1)
        Button(master, text=board[6][2], bg='gray75', padx=12, pady=10).grid(row=6, column=2)
        Button(master, text=board[6][3], bg='gray95', padx=12, pady=10).grid(row=6, column=3)
        Button(master, text=board[6][4], bg='gray95', padx=12, pady=10).grid(row=6, column=4)
        Button(master, text=board[6][5], bg='gray95', padx=12, pady=10).grid(row=6, column=5)
        Button(master, text=board[6][6], bg='gray75', padx=12, pady=10).grid(row=6, column=6)
        Button(master, text=board[6][7], bg='gray75', padx=12, pady=10).grid(row=6, column=7)
        Button(master, text=board[6][8], bg='gray75', padx=12, pady=10).grid(row=6, column=8)

        Button(master, text=board[7][0], bg='gray75', padx=12, pady=10).grid(row=7, column=0)
        Button(master, text=board[7][1], bg='gray75', padx=12, pady=10).grid(row=7, column=1)
        Button(master, text=board[7][2], bg='gray75', padx=12, pady=10).grid(row=7, column=2)
        Button(master, text=board[7][3], bg='gray95', padx=12, pady=10).grid(row=7, column=3)
        Button(master, text=board[7][4], bg='gray95', padx=12, pady=10).grid(row=7, column=4)
        Button(master, text=board[7][5], bg='gray95', padx=12, pady=10).grid(row=7, column=5)
        Button(master, text=board[7][6], bg='gray75', padx=12, pady=10).grid(row=7, column=6)
        Button(master, text=board[7][7], bg='gray75', padx=12, pady=10).grid(row=7, column=7)
        Button(master, text=board[7][8], bg='gray75', padx=12, pady=10).grid(row=7, column=8)

        Button(master, text=board[8][0], bg='gray75', padx=12, pady=10).grid(row=8, column=0)
        Button(master, text=board[8][1], bg='gray75', padx=12, pady=10).grid(row=8, column=1)
        Button(master, text=board[8][2], bg='gray75', padx=12, pady=10).grid(row=8, column=2)
        Button(master, text=board[8][3], bg='gray95', padx=12, pady=10).grid(row=8, column=3)
        Button(master, text=board[8][4], bg='gray95', padx=12, pady=10).grid(row=8, column=4)
        Button(master, text=board[8][5], bg='gray95', padx=12, pady=10).grid(row=8, column=5)
        Button(master, text=board[8][6], bg='gray75', padx=12, pady=10).grid(row=8, column=6)
        Button(master, text=board[8][7], bg='gray75', padx=12, pady=10).grid(row=8, column=7)
        Button(master, text=board[8][8], bg='gray75', padx=12, pady=10).grid(row=8, column=8)

        def save_sudoku():
            master.destroy()

        Button(
            master,
            text='Close',
            command=save_sudoku,
            padx=20,
            pady=10,
            justify='center'
        ).grid(row=10, column=3, columnspan=3)
