GOAL = {
    1: 5, 5: 4, 4: 3,
    4: 6, 5: None, 6: 2,
    7: 7, 8: 8, 9: 1,
}

#  ============================= Helper Functions ==================================
def get_empty_pos(puzzle) -> int:
    for key in puzzle:
        if puzzle[key] is None:
            return key


def move_up(puzzle):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos - 3] = puzzle[pos - 3], puzzle[pos]
    return puzzle


def move_down(puzzle):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos + 3] = puzzle[pos + 3], puzzle[pos]
    return puzzle


def move_right(puzzle):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos + 1] = puzzle[pos + 1], puzzle[pos]
    return puzzle


def move_left(puzzle):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos - 1] = puzzle[pos - 1], puzzle[pos]
    return puzzle


def revert(puzzle, operation):
    return {
        move_up: move_down,
        move_down: move_up,
        move_left: move_right,
        move_right: move_left,
    }[operation](puzzle)

def get_available_operations(puzzle):
    operations = {
        move_up,
        move_left, move_right,
        move_down,
    }
    empty_pos = get_empty_pos(puzzle)

    if empty_pos in {1, 2, 3}:
        operations.remove(move_up)
    if empty_pos in {7, 8, 9}:
        operations.remove(move_down)
    if empty_pos in {3, 6, 9}:
        operations.remove(move_right)
    if empty_pos in {1, 4, 7}:
        operations.remove(move_left)

    return operations

def heuristic(puzzle: dict) -> int:
    score = 0

    for key in puzzle:
        # print((puzzle[key], GOAL[key]))
        if puzzle[key] == GOAL[key]:
            score += 1

    return score

def safe_get(puzzle, key):
    if puzzle[key]:
        return puzzle[key]
    return '@'

def display_board(puzzle: dict[int, int]):
    print("The board looks like")
    print(
        str(safe_get(puzzle, 1)).center(3, ' ') + 
        str(safe_get(puzzle, 2)).center(3, ' ') +
        str(safe_get(puzzle, 3)).center(3, ' ')
    )
    print('-' * 10)
    print(
        str(safe_get(puzzle, 4)).center(3, ' ') + 
        str(safe_get(puzzle, 5)).center(3, ' ') +
        str(safe_get(puzzle, 6)).center(3, ' ')
    )
    print('-' * 10)
    print(
        str(safe_get(puzzle, 7)).center(3, ' ') + 
        str(safe_get(puzzle, 8)).center(3, ' ') +
        str(safe_get(puzzle, 9)).center(3, ' ')
    )

# ========================= Actual Hill Climbing Logic ====================================
def start(puzzle):
    if heuristic(puzzle) == heuristic(GOAL):
        return puzzle
    
    best_score = heuristic(puzzle)

    for operation in get_available_operations(puzzle):
        board = operation(puzzle)
        score = heuristic(board)

        if score >= best_score:
            print(f"We {operation.__name__} the empty slot")
            display_board(puzzle)
            print(f"Objective function value is {heuristic(puzzle)}")
            print("We got a better objective score, lets go ahead\n")
            print("=" * 40)
            best_score = score
            return start(board)
        else:
            board = revert(board, operation)
    
    print(" We hit a plateau! Stopping the algorithm ".center(80, '~'), sep='\n', end='\n\n')
    return puzzle

def main():
    STATE_GLOBAL = {
            1: 1, 2: 2, 3: 3,
            4: 8, 5: 6, 6: None,
            7: 7, 8: 5, 9: 4,
    }
    STATE_LOCAL = {
            1: 4, 2: None, 3: 7,
            4: 2, 5: 8, 6: 1,
            7: 3, 8: 6, 9: 5,
    }
    print("Menu for initial states of board")
    print("1. State which can reach global maxima")
    display_board(STATE_GLOBAL)
    print("2. State which cannot reach global maxima")
    display_board(STATE_LOCAL)
    choice = int(input("Which initial state do you want?\n>").strip())

    if choice == 1:
        puzzle = STATE_GLOBAL
    elif choice == 2:
        puzzle = STATE_LOCAL
    else:
        print("Please enter a valid number!")
        main()
        exit()

    print("The initial board state is ")
    display_board(puzzle)
    print('=' * 40)
    print("The goal is")
    display_board(GOAL)
    print('=' * 40)

    puzzle = start(puzzle)
    print("The final board state achieved by hill climbing is ")
    display_board(puzzle)
    print(f"The objective function value of this board is {heuristic(puzzle)}")

    if puzzle != GOAL:
        print("We could not reach final goal state👎")
    else:
        print("🎉We reached final goal state!🎉")


if __name__ == '__main__':
    main()
