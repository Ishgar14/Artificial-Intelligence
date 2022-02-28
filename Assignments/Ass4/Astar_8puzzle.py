GOAL = {
    1: 1, 2: 2, 3: 3,
    4: 8, 5: -1, 6: 4,
    7: 7, 8: 6, 9: 5,
}
t_board = dict[int, int]

#  ============================= Helper Functions ==================================


class Node:
    def __init__(self, board: dict[int, int], steps: int, prev=None, op=None):
        self.board = board.copy()
        self.steps = steps
        self.prev = prev
        self.operation = op

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self) -> int:
        return heuristic(self.board)

    def __repr__(self):
        return str(heuristic(self.board))

    def heu(self) -> int:
        return self.steps + heuristic(self.board)


def get_empty_pos(puzzle: t_board) -> int:
    for key in puzzle:
        if puzzle[key] == -1:
            return key


def move_up(puzzle: t_board):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos - 3] = puzzle[pos - 3], puzzle[pos]
    return puzzle


def move_down(puzzle: t_board):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos + 3] = puzzle[pos + 3], puzzle[pos]
    return puzzle


def move_right(puzzle: t_board):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos + 1] = puzzle[pos + 1], puzzle[pos]
    return puzzle


def move_left(puzzle: t_board):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos - 1] = puzzle[pos - 1], puzzle[pos]
    return puzzle


def get_available_operations(puzzle: t_board):
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

def get_operation_name(op):
    return {
        move_up: "Move the empty slot above",
        move_left: "Move the empty slot left",
        move_right: "Move the empty slot right",
        move_down: "Move the empty slot down",
    }[op]

# This function takes a board and returns heuristic value of it
# Heuristic is how many board are misplaced
def heuristic(puzzle: t_board) -> int:
    score = 0

    for key in puzzle:
        if puzzle[key] != GOAL[key]:
            score += 1

    return score


def safe_get(puzzle: t_board, key: int) -> str:
    if puzzle[key] != -1:
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


def start(puzzle) -> Node:
    root = Node(puzzle, 0)
    queue = [root]
    steps = 0
    previous = set()
    best_score = 1000

    while len(queue) > 0:
        steps += 1
        queue.sort(key=lambda n: n.heu())
        current = queue.pop(0)
        score = heuristic(current.board)

        if score == 0:
            return current

        if current in previous:
            # print("Skipping current state because it was repeated previously ...")
            continue
        else:
            previous.add(current)

        if score < best_score:
            best_score = score

        for operation in get_available_operations(current.board):
            child = Node(operation(current.board.copy()), steps, current, operation)
            queue.append(child)


    return current


def main():
    puzzle = {
        1: 1, 2: -1, 3: 3,
        4: 8, 5: 2, 6: 6,
        7: 7, 8: 5, 9: 4,
    }

    print("The initial board configuration is ")
    display_board(puzzle)
    print(f"The heuristic of this board is {heuristic(puzzle)}")
    node = start(puzzle)

        
    path: list[Node] = []

    while node:
        path.append(node)
        node = node.prev
    path = path[::-1]
    path = path[1:]

    for i, node in enumerate(path):
        print(f" Step {i + 1} ".center(40, '='))
        if node.operation:
            print(get_operation_name(node.operation))

        display_board(node.board)
        print(f"The heuristic of this board is {heuristic(node.board)}")
        # print(f"The f(x) of this board is {node.heu()}")

    if heuristic(path[-1].board) != 0:
        print("Not found ideal board position")
    else:
        print("This is the required solution✅")


if __name__ == '__main__':
    main()
