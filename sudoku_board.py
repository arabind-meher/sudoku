# SUDOKU BOARD

from tkinter import *

# 9X9 sudoku board
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


# Print the board
def print_board(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            print(b[i][j], end=' ')
        print()


# Class to entry the board details
class EntryBoard:
    def __init__(self, master):
        self.master = master

        master.title('Entry Board')
        master.geometry('400x510')
        master.resizable(0, 0)

        master.head = Label(master, text='ENTER THE NUMBERS', font=['bold', 20], pady=10).pack()

        master.note = Label(master, text="**USE '0' FOR BLANK\n**ENTER SPACE BETWEEN NUMBERS", padx=10).pack()

        text0 = StringVar()
        master.entry0 = Entry(master, textvariable=text0, width=14, font=['bold', 20]).pack()

        text1 = StringVar()
        master.entry1 = Entry(master, textvariable=text1, width=14, font=['bold', 20]).pack()

        text2 = StringVar()
        master.entry2 = Entry(master, textvariable=text2, width=14, font=['bold', 20]).pack()

        text3 = StringVar()
        master.entry3 = Entry(master, textvariable=text3, width=14, font=['bold', 20]).pack()

        text4 = StringVar()
        master.entry4 = Entry(master, textvariable=text4, width=14, font=['bold', 20]).pack()

        text5 = StringVar()
        master.entry5 = Entry(master, textvariable=text5, width=14, font=['bold', 20]).pack()

        text6 = StringVar()
        master.entry6 = Entry(master, textvariable=text6, width=14, font=['bold', 20]).pack()

        text7 = StringVar()
        master.entry7 = Entry(master, textvariable=text7, width=14, font=['bold', 20]).pack()

        text8 = StringVar()
        master.entry8 = Entry(master, textvariable=text8, width=14, font=['bold', 20]).pack()

        master.note2 = Label(master, text='PRESS START TO CONTINUE', padx=10, pady=10).pack()

        def button_clicked():
            try:
                print('Button Clicked')

                line0 = text0.get()
                if len(line0) != 0:
                    board[0] = line0.split()

                line1 = text1.get()
                if len(line1) != 0:
                    board[1] = line1.split()

                line2 = text2.get()
                if len(line2) != 0:
                    board[2] = line2.split()

                line3 = text3.get()
                if len(line3) != 0:
                    board[3] = line3.split()

                line4 = text4.get()
                if len(line4) != 0:
                    board[4] = line4.split()

                line5 = text5.get()
                if len(line5) != 0:
                    board[5] = line5.split()

                line6 = text6.get()
                if len(line6) != 0:
                    board[6] = line6.split()

                line7 = text7.get()
                if len(line7) != 0:
                    board[7] = line7.split()

                line8 = text8.get()
                if len(line8) != 0:
                    board[8] = line8.split()

            except Exception:
                print('An exception occur')

            finally:
                for i in range(9):
                    for j in range(9):
                        board[i][j] = int(board[i][j])

                master.destroy()

        button = Button(master, text='START', command=button_clicked, padx=10, pady=10).pack()

        master.mainloop()


# root1 = Tk()
# entryBoard = EntryBoard(root1)
# root1.mainloop()


# Class to display board details
class DisplayBoard:
    def __init__(self, master):
        self.master = master

        master.title('Solution')
        master.geometry('350x395')
        master.resizable(0, 0)

        button00 = Button(master, text=board[0][0], bg='gray75', padx=12, pady=10).grid(row=0, column=0)
        button01 = Button(master, text=board[0][1], bg='gray75', padx=12, pady=10).grid(row=0, column=1)
        button02 = Button(master, text=board[0][2], bg='gray75', padx=12, pady=10).grid(row=0, column=2)
        button03 = Button(master, text=board[0][3], bg='gray95', padx=12, pady=10).grid(row=0, column=3)
        button04 = Button(master, text=board[0][4], bg='gray95', padx=12, pady=10).grid(row=0, column=4)
        button05 = Button(master, text=board[0][5], bg='gray95', padx=12, pady=10).grid(row=0, column=5)
        button06 = Button(master, text=board[0][6], bg='gray75', padx=12, pady=10).grid(row=0, column=6)
        button07 = Button(master, text=board[0][7], bg='gray75', padx=12, pady=10).grid(row=0, column=7)
        button08 = Button(master, text=board[0][8], bg='gray75', padx=12, pady=10).grid(row=0, column=8)

        button10 = Button(master, text=board[1][0], bg='gray75', padx=12, pady=10).grid(row=1, column=0)
        button11 = Button(master, text=board[1][1], bg='gray75', padx=12, pady=10).grid(row=1, column=1)
        button12 = Button(master, text=board[1][2], bg='gray75', padx=12, pady=10).grid(row=1, column=2)
        button13 = Button(master, text=board[1][3], bg='gray95', padx=12, pady=10).grid(row=1, column=3)
        button14 = Button(master, text=board[1][4], bg='gray95', padx=12, pady=10).grid(row=1, column=4)
        button15 = Button(master, text=board[1][5], bg='gray95', padx=12, pady=10).grid(row=1, column=5)
        button16 = Button(master, text=board[1][6], bg='gray75', padx=12, pady=10).grid(row=1, column=6)
        button17 = Button(master, text=board[1][7], bg='gray75', padx=12, pady=10).grid(row=1, column=7)
        button18 = Button(master, text=board[1][8], bg='gray75', padx=12, pady=10).grid(row=1, column=8)

        button20 = Button(master, text=board[2][0], bg='gray75', padx=12, pady=10).grid(row=2, column=0)
        button21 = Button(master, text=board[2][1], bg='gray75', padx=12, pady=10).grid(row=2, column=1)
        button22 = Button(master, text=board[2][2], bg='gray75', padx=12, pady=10).grid(row=2, column=2)
        button23 = Button(master, text=board[2][3], bg='gray95', padx=12, pady=10).grid(row=2, column=3)
        button24 = Button(master, text=board[2][4], bg='gray95', padx=12, pady=10).grid(row=2, column=4)
        button25 = Button(master, text=board[2][5], bg='gray95', padx=12, pady=10).grid(row=2, column=5)
        button26 = Button(master, text=board[2][6], bg='gray75', padx=12, pady=10).grid(row=2, column=6)
        button27 = Button(master, text=board[2][7], bg='gray75', padx=12, pady=10).grid(row=2, column=7)
        button28 = Button(master, text=board[2][8], bg='gray75', padx=12, pady=10).grid(row=2, column=8)

        button30 = Button(master, text=board[3][0], bg='gray95', padx=12, pady=10).grid(row=3, column=0)
        button31 = Button(master, text=board[3][1], bg='gray95', padx=12, pady=10).grid(row=3, column=1)
        button32 = Button(master, text=board[3][2], bg='gray95', padx=12, pady=10).grid(row=3, column=2)
        button33 = Button(master, text=board[3][3], bg='gray75', padx=12, pady=10).grid(row=3, column=3)
        button34 = Button(master, text=board[3][4], bg='gray75', padx=12, pady=10).grid(row=3, column=4)
        button35 = Button(master, text=board[3][5], bg='gray75', padx=12, pady=10).grid(row=3, column=5)
        button36 = Button(master, text=board[3][6], bg='gray95', padx=12, pady=10).grid(row=3, column=6)
        button37 = Button(master, text=board[3][7], bg='gray95', padx=12, pady=10).grid(row=3, column=7)
        button38 = Button(master, text=board[3][8], bg='gray95', padx=12, pady=10).grid(row=3, column=8)

        button40 = Button(master, text=board[4][0], bg='gray95', padx=12, pady=10).grid(row=4, column=0)
        button41 = Button(master, text=board[4][1], bg='gray95', padx=12, pady=10).grid(row=4, column=1)
        button42 = Button(master, text=board[4][2], bg='gray95', padx=12, pady=10).grid(row=4, column=2)
        button43 = Button(master, text=board[4][3], bg='gray75', padx=12, pady=10).grid(row=4, column=3)
        button44 = Button(master, text=board[4][4], bg='gray75', padx=12, pady=10).grid(row=4, column=4)
        button45 = Button(master, text=board[4][5], bg='gray75', padx=12, pady=10).grid(row=4, column=5)
        button46 = Button(master, text=board[4][6], bg='gray95', padx=12, pady=10).grid(row=4, column=6)
        button47 = Button(master, text=board[4][7], bg='gray95', padx=12, pady=10).grid(row=4, column=7)
        button48 = Button(master, text=board[4][8], bg='gray95', padx=12, pady=10).grid(row=4, column=8)

        button50 = Button(master, text=board[5][0], bg='gray95', padx=12, pady=10).grid(row=5, column=0)
        button51 = Button(master, text=board[5][1], bg='gray95', padx=12, pady=10).grid(row=5, column=1)
        button52 = Button(master, text=board[5][2], bg='gray95', padx=12, pady=10).grid(row=5, column=2)
        button53 = Button(master, text=board[5][3], bg='gray75', padx=12, pady=10).grid(row=5, column=3)
        button54 = Button(master, text=board[5][4], bg='gray75', padx=12, pady=10).grid(row=5, column=4)
        button55 = Button(master, text=board[5][5], bg='gray75', padx=12, pady=10).grid(row=5, column=5)
        button56 = Button(master, text=board[5][6], bg='gray95', padx=12, pady=10).grid(row=5, column=6)
        button57 = Button(master, text=board[5][7], bg='gray95', padx=12, pady=10).grid(row=5, column=7)
        button58 = Button(master, text=board[5][8], bg='gray95', padx=12, pady=10).grid(row=5, column=8)

        button60 = Button(master, text=board[6][0], bg='gray75', padx=12, pady=10).grid(row=6, column=0)
        button61 = Button(master, text=board[6][1], bg='gray75', padx=12, pady=10).grid(row=6, column=1)
        button62 = Button(master, text=board[6][2], bg='gray75', padx=12, pady=10).grid(row=6, column=2)
        button63 = Button(master, text=board[6][3], bg='gray95', padx=12, pady=10).grid(row=6, column=3)
        button64 = Button(master, text=board[6][4], bg='gray95', padx=12, pady=10).grid(row=6, column=4)
        button65 = Button(master, text=board[6][5], bg='gray95', padx=12, pady=10).grid(row=6, column=5)
        button66 = Button(master, text=board[6][6], bg='gray75', padx=12, pady=10).grid(row=6, column=6)
        button67 = Button(master, text=board[6][7], bg='gray75', padx=12, pady=10).grid(row=6, column=7)
        button68 = Button(master, text=board[6][8], bg='gray75', padx=12, pady=10).grid(row=6, column=8)

        button70 = Button(master, text=board[7][0], bg='gray75', padx=12, pady=10).grid(row=7, column=0)
        button71 = Button(master, text=board[7][1], bg='gray75', padx=12, pady=10).grid(row=7, column=1)
        button72 = Button(master, text=board[7][2], bg='gray75', padx=12, pady=10).grid(row=7, column=2)
        button73 = Button(master, text=board[7][3], bg='gray95', padx=12, pady=10).grid(row=7, column=3)
        button74 = Button(master, text=board[7][4], bg='gray95', padx=12, pady=10).grid(row=7, column=4)
        button75 = Button(master, text=board[7][5], bg='gray95', padx=12, pady=10).grid(row=7, column=5)
        button76 = Button(master, text=board[7][6], bg='gray75', padx=12, pady=10).grid(row=7, column=6)
        button77 = Button(master, text=board[7][7], bg='gray75', padx=12, pady=10).grid(row=7, column=7)
        button78 = Button(master, text=board[7][8], bg='gray75', padx=12, pady=10).grid(row=7, column=8)

        button80 = Button(master, text=board[8][0], bg='gray75', padx=12, pady=10).grid(row=8, column=0)
        button81 = Button(master, text=board[8][1], bg='gray75', padx=12, pady=10).grid(row=8, column=1)
        button82 = Button(master, text=board[8][2], bg='gray75', padx=12, pady=10).grid(row=8, column=2)
        button83 = Button(master, text=board[8][3], bg='gray95', padx=12, pady=10).grid(row=8, column=3)
        button84 = Button(master, text=board[8][4], bg='gray95', padx=12, pady=10).grid(row=8, column=4)
        button85 = Button(master, text=board[8][5], bg='gray95', padx=12, pady=10).grid(row=8, column=5)
        button86 = Button(master, text=board[8][6], bg='gray75', padx=12, pady=10).grid(row=8, column=6)
        button87 = Button(master, text=board[8][7], bg='gray75', padx=12, pady=10).grid(row=8, column=7)
        button88 = Button(master, text=board[8][8], bg='gray75', padx=12, pady=10).grid(row=8, column=8)

# root2 = Tk()
# displayBoard = DisplayBoard(root2)
# root2.mainloop()
