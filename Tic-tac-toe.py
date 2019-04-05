'''
UI Layout:

   |   |         1 | 2 | 3
---+---+---     ---+---+---
   |   |         4 | 5 | 6
---+---+---     ---+---+---
   |   |         7 | 8 | 9
   board          legend

User presses a number from the legend to place their mark (X / O) on the board
'''

import random

def start():
    '''
    Main function to start program; user interface
    '''
    print('You are at the main menu.')
    while True:
        command = input('What would you like to do? Type:\n - "2p" for 2 player (player vs player)\n - "1p" for 1 player (player vs computer)\n - "exit" to exit\n')
        if command == '2p':
            print('Player vs Player:')
            play()
        elif command == '1p':
            print('Player vs CPU:')
            play_vs_cpu()
        elif command == 'exit':
            return
        else:
            print('That is not a valid command.')


def play():
    '''
    Player vs. player game handler
    '''
    board = make_empty_board()
    print_board_and_legend(board)

    last_mark = 'O' #initialize for if statements
    while " " in board[0] or " " in board[1] or " " in board[2]:

        # X's turn
        if last_mark == 'O':
            try:
                square_num = int(input("\nIt is X's turn. Enter your move (number from 1 to 9 according to legend on the right): "))
                if 1 <= square_num <= 9:
                    coord = get_coord(square_num)
                    if board[coord[0]][coord[1]] == " ":
                        board = put_in_board(board, 'X', square_num)
                        last_mark = 'X'
                    else:
                        print('Sorry, that is not a valid move.')
                else:
                    print('Sorry, that is not a valid move.')
            except:
                print('Sorry, that is not a valid move.')

        # O's turn
        elif last_mark == 'X':
            try:
                square_num = int(input("\nIt is O's turn. Enter your move (number from 1 to 9 according to legend on the right): "))
                if 1 <= square_num <= 9:
                    coord = get_coord(square_num)
                    if board[coord[0]][coord[1]] == " ":
                        put_in_board(board, 'O', square_num)
                        last_mark = 'O'
                    else:
                        print('Sorry, that is not a valid move.')
                else:
                    print('Sorry, that is not a valid move.')
            except:
                print('Sorry, that is not a valid move.')

        print_board_and_legend(board)

        if is_win(board, 'X'):
            print('X has won!')
            return
        elif is_win(board, 'O'):
            print('O has won!')
            return
    print('Draw!')
    return


def play_vs_cpu():
    '''
    Player vs. CPU game handler
    '''
    board = make_empty_board()
    print_board_and_legend(board)
    while " " in board[0] or " " in board[1] or " " in board[2]:
        try:
            square_num = int(input("\nIt is X's turn. Enter your move: "))
            if 1 <= square_num <= 9:
                coord = get_coord(square_num)
                if board[coord[0]][coord[1]] == " ":
                    board = put_in_board(board, 'X', square_num)
                    board = make_random_move(board, 'O')
                else:
                    print('Sorry, that is not a valid move.')
            else:
                print('Sorry, that is not a valid move.')
        except:
            print('Sorry, that is not a valid move.')

        print_board_and_legend(board)

        if is_win(board, 'X'):
            print('X has won!')
            return
        elif is_win(board, 'O'):
            print('O has won!')
            return
    print('Draw!')
    return


def make_empty_board():
    '''
    Return 3x3 2D array of blank strings for an empty board
    '''
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board


def print_board_and_legend(board):
    '''
    Print <board> and legend; legend shows number to press to place on board
    Inputs: board -- 3x3 2D array which holds current marks on the board
    '''
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2] #prints empty board
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) #prints legend
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")


def get_coord(square_num):
    '''
    Return 2D array index for a square at position <square_num> as tuple
    Inputs: square_num -- int from 1 to 9; position on board
    '''
    coord = (square_num - 1) // 3, (square_num - 1) % 3
    return coord


def put_in_board(board, mark, square_num):
    '''
    Put <mark> at square corresponding to <square_num> on <board>
    Inputs: board -- 3x3 2D array which holds current marks on the board
            mark -- "X" or "O"
            square_num -- int from 1 to 9; position on board
    '''
    if board[get_coord(square_num)[0]][get_coord(square_num)[1]] == " ":
        board[get_coord(square_num)[0]][get_coord(square_num)[1]] = mark
    return board


def is_row_all_marks(board, row_i, mark):
    '''
    Return True if <row_i> on <board> has all <mark>, else False
    '''
    for marks_in_row in range(3):
        if board[row_i][marks_in_row] != mark:
            return False
    return True


def is_col_all_marks(board, col_i, mark):
    '''
    Return True if <col_i> on <board> has all <mark>, else False
    '''
    for marks_in_col in range(3):
        if board[marks_in_col][col_i] != mark:
            return False
    return True


def is_diag_all_marks(board, mark):
    '''
    Return True if either diagonal on <board> has all <mark>, else False
    '''
    if (board[0][0] == mark and board[1][1] == mark and board [2][2] == mark):
        return True
    if (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
        return True
    return False


def is_win(board, mark):
    '''
    Return True if <mark> has won on <board>, else False
    '''
    for i in range(3):
        if is_row_all_marks(board, i, mark) or is_col_all_marks(board, i, mark):
            return True
    if is_diag_all_marks(board, mark):
        return True
    return False


def get_free_squares(board):
    '''
    Return list of indices where there is a free (empty) square on <board>
    Inputs: board -- 3x3 2D array which holds current marks on the board
    '''
    free_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_squares.append([i, j])
    return free_squares


def make_random_move(board, mark):
    '''
    Place <mark> at a random free spot on <board> for CPU
    '''
    num_free_squares = len(get_free_squares(board))
    if num_free_squares > 0:
        random_coords = get_free_squares(board)[int(num_free_squares * random.random())]
        board[random_coords[0]][random_coords[1]] = mark
    return board


if __name__ == '__main__':
    start()
