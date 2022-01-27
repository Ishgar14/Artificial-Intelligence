import random
from re import L
DEBUG = False

EMPTY = 0
O = 1
X = 2
PLAYER_CHARACTER = COMPUTER_CHARACTER = None

# Game Status
GAME_TIE = 0
GAME_ONGOING = 1
GAME_END = 2

board_array = [EMPTY for _ in range(9)]
visual_to_actual = {
    1: 4, 2: 9, 3: 2,
    4: 3, 5: 5, 6: 7,
    7: 8, 8: 1, 9: 6
}
actual_to_visual = {val: key for key, val in visual_to_actual.items()}

# this function takes *visual* index of a slot and inserts value into it
def put(index: int, val: int, original: bool = False) -> None:
    if original:
        if not (0 <= index <= 8):
            raise IndexError("Index out of bounds")
        board_array[index] = val
        return
    
    if not (1 <= index <= 9):
        raise IndexError("Index out of bounds")

    ind = visual_to_actual[index] - 1
    if board_array[ind] != EMPTY:
        raise IndexError("Index is already occupied")
    board_array[ind] = val
    pass


def accept_characters() -> None:
    global PLAYER_CHARACTER, COMPUTER_CHARACTER
    if DEBUG:
        PLAYER_CHARACTER = 'X'
        COMPUTER_CHARACTER = 'O'
        return

    PLAYER_CHARACTER = input("Pick your character (O/X): ")

    if PLAYER_CHARACTER.upper() == 'X':
        PLAYER_CHARACTER = 'X'
        COMPUTER_CHARACTER = 'O'
    elif PLAYER_CHARACTER.upper() == 'O':
        PLAYER_CHARACTER = 'O'
        COMPUTER_CHARACTER = 'X'
    else:
        print("Please enter a valid character!")
        accept_characters()


def display_board() -> None:
    counter = 1

    for _ in range(3):
        for _ in range(3):
            if board_array[counter - 1] == EMPTY:
                print(actual_to_visual[counter], end=' ')
            else:
                print(board_array[counter - 1], end=' ')
            counter += 1
        print()

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

def get_slots_of(character: str, display_mapped: bool = True) -> list:
    if display_mapped:
        return [actual_to_visual[i + 1] for i in range(9) if board_array[i] == character]
    else:
        return [i for i in range(9) if board_array[i] == character]


# This function computes computers moves and returns (visual) index of new move
def get_computer_move() -> int:
    # check if actual center slot is occupied
    if board_array[4] == EMPTY:
        return 5
    
    computer_places = get_slots_of(COMPUTER_CHARACTER)
    human_places = get_slots_of(PLAYER_CHARACTER)

    if len(human_places) == 2:
        block_human = 15 - (human_places[0] + human_places[1])
        if 0 <= block_human - 1 <= 8 and board_array[visual_to_actual[block_human] - 1] == EMPTY:
            return block_human

    # if computer has less than 1 move, randomly return second move
    if len(computer_places) <= 1:
        available = get_slots_of(EMPTY)
        return random.choice(available)

    
    if len(computer_places) == 2:
        visual_move = 15 - (computer_places[0] + computer_places[1])

        # Non collinear moves cannot result in a win
        # So just pick a random empty slot
        if visual_move < 0 or visual_move >= 9:
            available = get_slots_of(EMPTY)
            return random.choice(available)

        if board_array[visual_to_actual[visual_move] - 1] == EMPTY:
            return visual_move
        elif board_array[visual_to_actual[visual_move] - 1] == PLAYER_CHARACTER and len(human_places) == 2:
            # now computer cant win because place is already occupied by player
            # but it can stop player from winning
            visual_move = 15 - (human_places[0] + human_places[1])
            if 0 < visual_move < 9:
                return visual_move
    
    # If we couldn't win uptil now then we definitely wont win
    # So we just need to return random available indices to stall the game
    visual_blocks = []
    if len(human_places) == 3:
        visual_blocks = [
            15 - (human_places[0] + human_places[1]),
            15 - (human_places[2] + human_places[1]),
            15 - (human_places[0] + human_places[2]),
        ]
    
    if len(human_places) == 4:
        visual_blocks = [
            15 - (human_places[0] + human_places[1]),
            15 - (human_places[0] + human_places[2]),
            15 - (human_places[0] + human_places[3]),
            15 - (human_places[1] + human_places[3]),
            15 - (human_places[2] + human_places[1]),
            15 - (human_places[2] + human_places[3]),
        ]

    visual_blocks = list(filter(lambda x: 1 <= x <= 9 and board_array[visual_to_actual[x] - 1] == EMPTY, visual_blocks))
    if len(visual_blocks) > 0:
        return random.choice(visual_blocks)

    available = get_slots_of(EMPTY)
    return random.choice(available)


def main() -> None:
    accept_characters()
    turn = True # True = player's turn, False = computers's turn
    threats = [
        "Please enter a valid index 😊",
        "Enter a valid index 😶",
        "Are you serious? 😡",
        "Not going to ask you again 🔫"
    ]
    threat_counter = 0

    # X starts first, AWLAYS
    if PLAYER_CHARACTER == 'X':
        turn = True
        display_board()
        while True:
            position = int(input("Enter which position: "))
            try:
                put(position, 'X')
            except IndexError:
                print(threats[threat_counter])
                threat_counter = (threat_counter + 1) % len(threats)
                continue
            break
    else:
        # If computer is X pick center
        put(5, 'X')
        turn = False
    
    turn = not turn
    available = [i for i in range(9) if board_array[i] == EMPTY]

    while len(available) != 0:
        status, winner = game_status()
        if status == GAME_END:
            break

        display_board()
        if not turn:
            print(' Computers Turn [{}] '.format(COMPUTER_CHARACTER).center(40, '='))
            comp_move = get_computer_move()
            print("Computer picks", comp_move)
            put(comp_move, COMPUTER_CHARACTER)
        else:
            print(' Players Turn [{}] '.format(PLAYER_CHARACTER).center(40, '='))
            while True:
                position = int(input("Enter move position: "))
                try:
                    put(position, PLAYER_CHARACTER)
                except IndexError as e:
                    print(e, threats[threat_counter], sep='\n')
                    threat_counter = (threat_counter + 1) % len(threats)
                    continue
                threat_counter = 0
                break

        turn = not turn
        available = [i for i in range(9) if board_array[i] == EMPTY]
    

    display_board()
    _, winner = game_status()
    if winner is not None:
        if PLAYER_CHARACTER == winner:
            print("\nThe player wins 🤴")
        else:
            print("\nThe computer wins 💻")
    else:
        print("\nIt was a tie 👨🤝💻")


if __name__ == '__main__':
    main()
