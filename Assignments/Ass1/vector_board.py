# Board Status
EMPTY = 0
O = 1
X = 2

# Game Status
GAME_TIE = 0
GAME_ONGOING = 1
GAME_END = 2

PLAYER_CHARACTER = COMPUTER_CHARACTER = None
board_array = [EMPTY for _ in range(9)]

def accept_characters() -> None:
    global PLAYER_CHARACTER, COMPUTER_CHARACTER
    PLAYER_CHARACTER = input('Enter your character (O/X):').strip().upper()

    if PLAYER_CHARACTER == 'X':
        COMPUTER_CHARACTER = 'O'
    elif PLAYER_CHARACTER == 'O':
        COMPUTER_CHARACTER = 'X'
    else:
        print("Please enter a valid character!")
        accept_characters()

def display_board() -> None:
    counter = 0
    for _ in range(3):
        for _ in range(3):
            if board_array[counter] == EMPTY:
                print(counter + 1, end=' ')
            else:
                print(board_array[counter], end=' ')
            counter += 1
        print()

def computer_move() -> int:
    str_arr = []
    for val in board_array:
        if val == EMPTY:
            str_arr.append('0')
        elif val == 'O':
            str_arr.append(str(O))
        elif val == 'X':
            str_arr.append(str(X))
    
    number = ''.join(str_arr)
    number = int(number, 3)
    # TODO: Fix indexing issue
    board_array[number % 9] = COMPUTER_CHARACTER


def game_status():
    # check for rows
    if board_array[0] == board_array[1] == board_array[2] and board_array[0] != EMPTY:
        return GAME_END, board_array[0]
    if board_array[3] == board_array[4] == board_array[5] and board_array[3] != EMPTY:
        return GAME_END, board_array[3]
    if board_array[6] == board_array[7] == board_array[8] and board_array[6] != EMPTY:
        return GAME_END, board_array[6]
    
    # check for colums
    if board_array[0] == board_array[3] == board_array[6] and board_array[0] != EMPTY:
        return GAME_END, board_array[0]
    if board_array[1] == board_array[4] == board_array[7] and board_array[1] != EMPTY:
        return GAME_END, board_array[1]
    if board_array[2] == board_array[5] == board_array[8] and board_array[2] != EMPTY:
        return GAME_END, board_array[2]

    # check for diagonals
    if board_array[0] == board_array[4] == board_array[8] and board_array[0] != EMPTY:
        return GAME_END, board_array[0]
    if board_array[2] == board_array[4] == board_array[6] and board_array[2] != EMPTY:
        return GAME_END, board_array[2]
    
    available = [i for i in range(9) if board_array[i] == EMPTY ]
    if len(available) == 0:
        return GAME_TIE, None
    return GAME_ONGOING, None


def main() -> None:
    turn = True # True -> Player's turn, False -> Computer's turn
    # display_board()
    available = [i for i in range(9) if board_array[i] == EMPTY]

    while len(available) != 0:
        status, winner = game_status()
        
        if status == GAME_END:
            break

        if turn:
            display_board()
            print(" Player's Turn ".center(40, '='))
            move = int(input("Enter your move: "))
            board_array[move - 1] = PLAYER_CHARACTER
        else:
            print(" Computer's Turn ".center(40, '='))
            move = computer_move()
            print("Computer picks", move)
            board_array[move] = COMPUTER_CHARACTER
            
        turn = not turn
        available = [i for i in range(9) if board_array[i] == EMPTY]
    
    print(" Final Board ".center(40, '='))
    display_board()
    if winner is not None:
        print("\nThe winner is", winner)
    else:
        print("\nThe game was a tie")


if __name__ == '__main__':
    accept_characters()
    main()