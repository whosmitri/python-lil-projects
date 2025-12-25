## PYTHON 3.13 64-bit

# IMPORT LIBRARIES
import tkinter
from tkinter import *
from tkinter import ttk

# SETTING COLORS
white = '#ffffff'
smoke_white = '#fcfbf7'
light_gray = '#e2e2e2'
gray = '#c2c1c1'
dark_gray = '#7e7e7e'
black = '#333333'
blue = '#3297a8'
red = '#e85151'

# CREATING MAIN WINDOW
app = Tk()
app.title('TicTacToe')
app.geometry('260x380')
app.configure(bg=smoke_white)

# CREATING TOW SECTIOS
# top frame
frame_top = Frame(app, width=240, height=100, bg=light_gray,relief='raised')
frame_top.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

# bottom frame
frame_bottom = Frame(app, width=240, height=240, bg=light_gray,relief='flat')
frame_bottom.grid(row=1, column=0, sticky=NW, padx=10)

# CONFIGURING SECTIONS
# top frame
app_x = Label(frame_top, text='X', height=1, relief='flat', anchor='center', font='Ivy 40 bold', bg=light_gray, fg=red)
app_x.place(x=25, y=10)

app_x_player = Label(frame_top, text='Player One', height=1, relief='flat', anchor='center', font='Ivy 7 bold', bg=light_gray, fg=black)
app_x_player.place(x=17, y=70)

app_x_score = Label(frame_top, text='0', height=1, relief='flat', anchor='center', font='Ivy 30 bold', bg=light_gray, fg=black)
app_x_score.place(x=80, y=20)

##
app_separador = Label(frame_top, text=':', height=1, relief='flat', anchor='center', font='Ivy 30 bold', bg=light_gray, fg=black)
app_separador.place(x=110, y=20)
##

app_o = Label(frame_top, text='O', height=1, relief='flat', anchor='center', font='Ivy 40 bold', bg=light_gray, fg=blue)
app_o.place(x=170, y=10)

app_o_player = Label(frame_top, text='Player Two', height=1, relief='flat', anchor='center', font='Ivy 7 bold', bg=light_gray, fg=black)
app_o_player.place(x=165, y=70)

app_o_score = Label(frame_top, text='0', height=1, relief='flat', anchor='center', font='Ivy 30 bold', bg=light_gray, fg=black)
app_o_score.place(x=130, y=20)


# GAME LOGIC
# players
player_1 = 'X'
player_2 = 'O'

# scores
score_1 = 0
score_2 = 0

# game board
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

# buttons
btns = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


# controls
current_player = 'X'
play = ''
moves = 0


def start_game():
    # control game
    def control(row, col):
        global current_player, moves, score_1, score_2

        if board[row][col] == '':
            board[row][col] = current_player
            btns[row][col]['text'] = current_player
            btns[row][col]['fg'] = red if current_player == 'X' else blue

            moves += 1

            if check_winner():
                if current_player == 'X':
                    score_1 += 1
                    app_x_score.config(text=str(score_1))
                else:
                    score_2 += 1
                    app_o_score.config(text=str(score_2))

                end_game()
                return

            if moves == 9:
                end_game()
                return

            current_player = 'O' if current_player == 'X' else 'X'

    # to end the game
    def end_game():
        global board, moves, current_player

        for i in range(3):
            for j in range(3):
                btns[i][j]['state'] = 'disabled'

        app.after(1200, reset_board)
    
    def reset_board():
        global board, moves, current_player

        board = [['', '', ''], ['', '', ''], ['', '', '']]
        moves = 0
        current_player = 'X'

        for i in range(3):
            for j in range(3):
                btns[i][j]['text'] = ''
                btns[i][j]['state'] = 'normal'


    def check_winner():
        # lines
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '':
                return True

        # columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] != '':
                return True

        # diagonals
        if board[0][0] == board[1][1] == board[2][2] != '':
            return True

        if board[0][2] == board[1][1] == board[2][0] != '':
            return True

        return False
    
    # PLAY BUTTON
    btn_play.place_forget()

    # CONFIGURING SECTIONS
    # bottom frame
    ## vertical lines
    app_vline1 = Label(frame_bottom, text='', height=27, relief='flat', pady=5, anchor='center', font='Ivy 5', bg=black)
    app_vline1.place(x=80, y=15)

    app_vline2 = Label(frame_bottom, text='', height=27, relief='flat', pady=5, anchor='center', font='Ivy 5', bg=black)
    app_vline2.place(x=150, y=15)

    ## horizontal lines
    app_hline1 = Label(frame_bottom, text='', width=192, relief='flat', padx=2, anchor='center', font='Ivy 1', bg=black)
    app_hline1.place(x=20, y=80)

    app_hline2 = Label(frame_bottom, text='', width=192, relief='flat', padx=2, anchor='center', font='Ivy 1', bg=black)
    app_hline2.place(x=20, y=150)

    # BUTTONS
    # line 0
    btns[0][0] = Button(frame_bottom, command=lambda:control(0, 0), text='', width=3, height=1, relief='flat', font='Ivy 20', overrelief=RIDGE, bg=light_gray)
    btns[0][0].place(x=20, y=20)

    btns[0][1] = Button(frame_bottom, command=lambda:control(0, 1), text='', width=3, height=1, relief='flat', font='Ivy 20', overrelief=RIDGE, bg=light_gray)
    btns[0][1].place(x=89, y=20)

    btns[0][2] = Button(frame_bottom, command=lambda:control(0, 2), text='', width=3, height=1, relief='flat', font='Ivy 20', overrelief=RIDGE, bg=light_gray)
    btns[0][2].place(x=160, y=20)

    # line 1
    btns[1][0] = Button(frame_bottom, command=lambda:control(1, 0), text='', width=3, height=1, relief='flat', font='Ivy 20', overrelief=RIDGE, bg=light_gray)
    btns[1][0].place(x=20, y=90)

    btns[1][1] = Button(frame_bottom, command=lambda:control(1, 1), text='', width=3, height=1, relief='flat', font='Ivy 20', overrelief=RIDGE, bg=light_gray)
    btns[1][1].place(x=89, y=90)

    btns[1][2] = Button(frame_bottom, command=lambda:control(1, 2), text='', width=3, height=1, relief='flat', font='Ivy 20', overrelief=RIDGE, bg=light_gray)
    btns[1][2].place(x=160, y=90)

    # line 2
    btns[2][0] = Button(frame_bottom, command=lambda:control(2, 0), text='', width=3, height=1, relief='flat', font='Ivy 20', overrelief=RIDGE, bg=light_gray)
    btns[2][0].place(x=20, y=160)

    btns[2][1] = Button(frame_bottom, command=lambda:control(2, 1), text='', width=3, height=1, relief='flat', font='Ivy 20', overrelief=RIDGE, bg=light_gray)
    btns[2][1].place(x=89, y=160)

    btns[2][2] = Button(frame_bottom, command=lambda:control(2, 2), text='', width=3, height=1, relief='flat', font='Ivy 20', overrelief=RIDGE, bg=light_gray)
    btns[2][2].place(x=160, y=160)


# PLAY BUTTON
btn_play = Button(frame_bottom, command=start_game, text='Play', width=10, height=1, font='Ivy 10 bold', overrelief=RIDGE, bg=light_gray)
btn_play.place(x=72, y=100)


# RUN
app.mainloop()
