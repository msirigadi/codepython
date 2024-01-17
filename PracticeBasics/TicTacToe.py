from random import randrange

free_fields = []

board = [[(c + 1) + (3 * r) for c in range(3)] for r in range(3)]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    for r in range(3):
        for c in range(3):
            print(board[r][c], end=' ')
        print()


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    if len(free_fields) == 0:
        return

    while True:
        try:
            user_move = int(input("Enter integer from 1 to 9: "))
        except:
            print("Enter a valid number between 1 to 9")
            continue

        for r in range(3):
            for c in range(3):
                if board[r][c] == user_move:
                    board[r][c] = 'O'
                    make_list_of_free_fields(board)
                    return


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_fields
    free_fields = []

    for r in range(3):
        for c in range(3):
            if board[r][c] != 'X' and board[r][c] != 'O':
                free_fields.append((r, c))

    print("Free fields", free_fields)


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    if ((board[0][0] == board[0][1] == board[0][2] == sign) or \
            (board[1][0] == board[1][1] == board[1][2] == sign) or \
            (board[2][0] == board[2][1] == board[2][2] == sign) or \
            (board[0][0] == board[1][0] == board[2][0] == sign) or \
            (board[0][1] == board[1][1] == board[2][1] == sign) or \
            (board[0][2] == board[1][2] == board[2][2] == sign) or \
            (board[0][0] == board[1][1] == board[2][2] == sign) or \
            (board[0][2] == board[1][1] == board[2][0] == sign)):
        return True


def draw_move(board):
    # The function draws the computer's move and updates the board.
    if board[1][1] != 'X':
        board[1][1] = 'X'
        return

    if len(free_fields) == 0:
        return

    while True:
        update = False
        random_num = randrange(1, 10)
        for r in range(3):
            for c in range(3):
                if board[r][c] == random_num:
                    board[r][c] = 'X'
                    make_list_of_free_fields(board)
                    return


display_board(board)
make_list_of_free_fields(board)

while len(free_fields):
    draw_move(board)
    display_board(board)
    enter_move(board)
    display_board(board)

if victory_for(board, 'X'):
    print("Computer wins")
elif victory_for(board, 'O'):
    print("User wins")
else:
    print("It's a Tie")