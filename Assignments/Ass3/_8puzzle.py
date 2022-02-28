GOAL = {
    1: 1, 2: 2, 3: 3,
    4: 8, 5: None, 6: 4,
    7: 7, 8: 6, 9: 5,
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
    
    display_board(puzzle)
    print(f"Heuristic is {heuristic(puzzle)}")
    best_score = heuristic(puzzle)

    for operation in get_available_operations(puzzle):
        board = operation(puzzle)
        score = heuristic(board)
        print(f"We {operation.__name__} the empty slot")

        if score >= best_score:
            print("We got a better heuristic score, lets keep it\n")
            best_score = score
            return start(board)
        else:
            display_board(puzzle)
            print(f"Heuristic is {heuristic(puzzle)}")
            print("Didn't get better score, backtracking...\n")
            board = revert(board, operation)
    
    return puzzle

def main():
    print("Menu for initial configurations of board")
    print("1. Optimal Solution")
    print("2. Suboptimal Solution")
    choice = int(input("Which initial configuration do you want?\n>").strip())

    if choice == 1:
        puzzle = {
            1: 1, 2: 2, 3: 3,
            4: 8, 5: 6, 6: None,
            7: 7, 8: 5, 9: 4,
        }
    elif choice == 2:
        puzzle = {
            1: 4, 2: None, 3: 7,
            4: 2, 5: 8, 6: 1,
            7: 3, 8: 6, 9: 5,
        }
    else:
        print("Please enter a valid number!")
        main()
        exit()

    print("The initial board configuration is ")
    puzzle = start(puzzle)
    print("The final board configuration achieved by hill climbing is ")
    display_board(puzzle)
    print(f"The heuristic of this board is {heuristic(puzzle)}")


if __name__ == '__main__':
    main()
