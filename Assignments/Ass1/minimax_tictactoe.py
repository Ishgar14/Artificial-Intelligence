EMPTY = ' '
PLAYER_CHARACTER = 'O'
COMPUTER_CHARACTER = 'X'


def display_board(board: dict[int, str]) -> None:
    vals = []
    for i, val in board.items():
        if val == ' ':
            vals.append(str(i))
        else:
            vals.append(val)

    vals = [val.center(3, ' ') for val in vals]

    print('|'.join(vals[:3]))
    print('-' * 10)
    print('|'.join(vals[3:6]))
    print('-' * 10)
    print('|'.join(vals[6:]))


def has_empty_slots(board: dict[int, str]) -> bool:
    return ' ' in board.values()


def is_winner(board: dict[int, str], mark: str) -> bool:
    # Row check
    if board[1] == board[2] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] == board[9] and board[7] == mark:
        return True
    
    # Column check
    elif board[1] == board[4] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] == board[9] and board[3] == mark:
        return True

    # Diagonal check
    elif board[1] == board[5] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] == board[3] and board[7] == mark:
        return True
    
    return False

def has_winner(board: dict[int, str]) -> bool:
    return is_winner(board, PLAYER_CHARACTER) or is_winner(board, COMPUTER_CHARACTER)


def game_status(board, char: str):
    if has_winner(board):
        if char == COMPUTER_CHARACTER:
            print("\nThe computer wins 💻")
        else:
            print("\nThe player wins 🤴")
        display_board(board)
        exit()

    if not has_empty_slots(board):
        print("\nIt was a tie 👨🤝💻")
        display_board(board)
        exit()

def player_move(board) -> None:
    print(f" Player's Turn [{PLAYER_CHARACTER}] ".center(40, '='))
    display_board(board)
    while True:
        position = int(input("Enter the position: "))
        if board[position] != EMPTY:
            print("Position is already occupied")
            continue
        break
    
    board[position] = PLAYER_CHARACTER


def computer_move(board) -> None:
    print(f" Computer's Turn [{COMPUTER_CHARACTER}] ".center(40, '='))
    display_board(board)
    bestScore = -1000
    bestMove = 0

    for key in board:
        if board[key] != EMPTY:
            continue

        board[key] = COMPUTER_CHARACTER
        score = minimax(board, False)
        board[key] = EMPTY
        
        if(score > bestScore):
            bestScore = score
            bestMove = key

    board[bestMove] = COMPUTER_CHARACTER
    print(f"Computer picked {bestMove}")

def heuristic(board: dict[int, str]) -> int:
    if is_winner(board, COMPUTER_CHARACTER) :
        return 10
    elif is_winner(board, PLAYER_CHARACTER):
        return -10
    elif has_empty_slots(board):
        return 0

    return None
    

def minimax(board: dict[int, str], maximise: bool) -> int:
    if val := heuristic(board):
        return val

    if maximise:
        bestScore = -1000
        for key in board.keys():
            if board[key] != EMPTY:
                continue
            
            board[key] = COMPUTER_CHARACTER
            score = minimax(board, False)
            board[key] = EMPTY
            
            if score > bestScore:
                bestScore = score
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] != EMPTY:
                continue
            
            board[key] = PLAYER_CHARACTER
            score = minimax(board, True)
            board[key] = EMPTY
            
            if score < bestScore:
                bestScore = score
    
    return bestScore

def get_characters():
    global PLAYER_CHARACTER, COMPUTER_CHARACTER
    PLAYER_CHARACTER = input("Enter your character(X/O): ").strip().upper()

    if PLAYER_CHARACTER == 'X':
        COMPUTER_CHARACTER = 'O'
    else:
        COMPUTER_CHARACTER = 'X'

def main(board):
    turn = True
    while has_empty_slots(board) or not has_winner(board):
        if turn:
            computer_move(board)
            game_status(board, COMPUTER_CHARACTER)
        else:
            player_move(board)
            game_status(board, PLAYER_CHARACTER)
        turn = not turn


if __name__ == '__main__':
    board = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
    get_characters()
    main(board)