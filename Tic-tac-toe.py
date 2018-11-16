#Tic-tac-toe game for player vs. player and player vs. AI

import random #for AI to make random moves

def print_board_and_legend(board):
    '''Prints board and legend. Legend shows which button to press to place O or
    X on the board
    board = 3x3 array which holds current X's and O's on the board
    '''
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2] #prints empty board
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) #prints legend
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

def make_empty_board():
    '''Returns 3x3 array of blank strings for an empty board
    '''
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def get_coord(square_num):
    '''Gets 2D array index for a square at position square_num
    square_num = int from 1 to 9; position on board
    '''
    coord = [(square_num - 1) // 3, (square_num - 1) % 3]
    return coord

def put_in_board(board, mark, square_num):
    '''Puts mark on square_num of board
    board = 3x3 array which holds current X's and O's on the board
    mark = "X" or "O"
    square_num = int from 1 to 9; position on board
    '''
    if board[get_coord(square_num)[0]][get_coord(square_num)[1]] == " ":
        board[get_coord(square_num)[0]][get_coord(square_num)[1]] = mark

def play():
    '''Function to be called for player vs. player play
    '''
    global board
    board = make_empty_board()
    print_board_and_legend(board)
    last_mark = 'O' #initialize for if statements
    while " " in board[0] or " " in board[1] or " " in board[2]:
        if last_mark == 'O': #check if it is X's turn
            square_num = int(input("\nIt is X's turn. Enter your move (number from 1 to 9 according to legend on the right): "))
            if 1 <= square_num <= 9:
                if board[get_coord(square_num)[0]][get_coord(square_num)[1]] == " ":
                    put_in_board(board, 'X', square_num)
                    last_mark = 'X'
                else:
                    print('Sorry, that is not a valid move.')
            else:
                print('Sorry, that is not a valid move.')
        elif last_mark == 'X': #check if it is O's turn
            square_num = int(input("\nIt is O's turn. Enter your move (number from 1 to 9 according to legend on the right): "))
            if 1 <= square_num <= 9:
                if board[get_coord(square_num)[0]][get_coord(square_num)[1]] == " ":
                    put_in_board(board, 'O', square_num)
                    last_mark = 'O'
                else:
                    print('Sorry, that is not a valid move.')
            else:
                print('Sorry, that is not a valid move.')
        print_board_and_legend(board)
        if is_win(board, 'X'):
            print('X has won!')
            return
        elif is_win(board, 'O'):
            print('O has won!')
            return
    print('Draw!')

#----------------------------------
#Additional code for player vs. AI:

def get_free_squares(board):
    '''Returns array of board indices where there is a free (empty) square
    board = 3x3 array which holds current X's and O's on the board
    '''
    free_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_squares.append([i, j])
    return free_squares

def make_random_move(board, mark):
    '''Puts mark at a random free spot on the board for AI
    
    '''
    num_free_squares = len(get_free_squares(board))
    if num_free_squares > 0:
        random_coords = get_free_squares(board)[int(num_free_squares * random.random())]
        board[random_coords[0]][random_coords[1]] = mark

def play_vs_cpu():
    '''Function to be called for player vs. AI play
    '''
    global board
    board = make_empty_board()
    print_board_and_legend(board)
    while " " in board[0] or " " in board[1] or " " in board[2]:
        square_num = int(input("\nIt is X's turn. Enter your move: "))
        if 1 <= square_num <= 9:
            if board[get_coord(square_num)[0]][get_coord(square_num)[1]] == " ":
                put_in_board(board, 'X', square_num)
                make_random_move(board, 'O')
            else:
                print('Sorry, that is not a valid move.')
        else:
            print('Sorry, that is not a valid move.')
        print_board_and_legend(board)
        if is_win(board, 'X'):
            print('X has won!')
            return
        elif is_win(board, 'O'):
            print('O has won!')
            return
    print('Draw!')

def is_row_all_marks(board, row_i, mark):
    '''Returns True if a given row has all X's or O's, False otherwise
    '''
    for marks_in_row in range(3):
        if board[row_i][marks_in_row] != mark:
            return False
    return True

def is_col_all_marks(board, col_i, mark):
    '''Returns True if a given column has all X's or O's, False otherwise
    '''
    for marks_in_col in range(3):
        if board[marks_in_col][col_i] != mark:
            return False
    return True

def is_win(board, mark):
    for i in range(3):
        if is_row_all_marks(board, i, mark) or is_col_all_marks(board, i, mark):
            return True
        if (board[0][0] == mark and board[1][1] == mark and board [2][2] == mark) or (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
            return True
    return False

def start_game():
    print('You are at the main menu.')
    while True:
        command = input('What would you like to do? Type:\n\t"2p" for 2 player (player vs player)\n\t"1p" for 1 player (player vs computer)\n\t"exit" to exit\n')
        if command == '2p':
            print('Player vs Player:')
            play()
        elif command == '1p':
            print('Player vs AI:')
            play_vs_cpu()
        elif command == 'exit':
            return
        else:
            print('That is not a valid command.')

if __name__ == '__main__':
    start_game()
