PLAYER_CHARACTER = 'O'
COMPUTER_CHARACTER = 'X'

board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}


def display_board(board):
    print(
        board[1].center(5, ' ') + '|' + 
        board[2].center(5, ' ') + '|' + 
        board[3].center(5, ' ')
    )
    print('-' * 17)
    print(
        board[4].center(5, ' ') + '|' + 
        board[5].center(5, ' ') + '|' + 
        board[6].center(5, ' ')
    )
    print('-' * 17)
    print(
        board[7].center(5, ' ') + '|' + 
        board[8].center(5, ' ') + '|' + 
        board[9].center(5, ' ')
    )
    print('\n')


def is_free(pos):
    return board[pos] == ' '


def is_draw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def somebody_won():
    # Row check
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True

    # Column check
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True

    # Diagonal check
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
        return True
    else:
        return False


def has_won(mark):
    # Row check
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True

    # Column check
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True

    # Diagoanl check
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] == mark:
        return True
    else:
        return False


def putchar(character, position):
    if is_free(position):
        board[position] = character
        display_board(board)

        if is_draw():
            print("\nIt was a tie 👨🤝💻")
            exit()

        if somebody_won():
            if character == COMPUTER_CHARACTER:
                print("\nThe computer wins 💻")
            else:
                print("\nThe player wins 🤴")
            exit()

    else:
        print("This slot is already used!")
        position = int(input("Enter new position: "))
        putchar(character, position)


def get_player_move():
    print(" Player's Turn ".center(40, '='))
    pos = int(input("Enter the position for 'O': "))
    putchar(PLAYER_CHARACTER, pos)


def get_computer_move():
    print(" Computer's Turn ".center(40, '='))
    best_score = -100
    best_move = 0

    for key in board.keys():
        if board[key] != ' ':
            continue

        board[key] = COMPUTER_CHARACTER
        score = minimax(board, False)
        board[key] = ' '

        if score > best_score:
            best_score = score
            best_move = key
        print(f"Computer found move {best_move} with score {best_score}")

    print(f"Computer picks move {best_move} with score {best_score}")
    putchar(COMPUTER_CHARACTER, best_move)


def minimax(board, maximising):
    if has_won(COMPUTER_CHARACTER):
        return 10
    if has_won(PLAYER_CHARACTER):
        return -10
    elif is_draw():
        return 0

    if maximising:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':

                board[key] = COMPUTER_CHARACTER
                score = minimax(board, False)
                board[key] = ' '

                if score > bestScore:
                    bestScore = score

        return bestScore

    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':

                board[key] = PLAYER_CHARACTER
                score = minimax(board, True)
                board[key] = ' '

                if score < bestScore:
                    bestScore = score

        return bestScore


def main():
    display_board(board)
    first = input("Do you wish to play first (Y/N): ").strip().upper()
    turn = first == 'Y'

    while not somebody_won():
        if turn:
            get_player_move()
        else:
            get_computer_move()
        turn = not turn

if __name__ == '__main__':
    main()