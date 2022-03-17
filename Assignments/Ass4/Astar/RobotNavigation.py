# Board Contents
EMPTY = 0
WALL = 1
SELECTED = 2

class Node:
    def __init__(self, x, y, prev = None):
        self.x = x
        self.y = y
        self.prev = prev
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
    
    def __repr__(self):
        return str((self.x, self.y))
    
    def __hash__(self):
        return (self.x, self.y).__hash__()

    def man_dist(self, to) -> int:
        return abs(self.x - to.x) + abs(self.y - to.y)

    def heu(self, goal) -> int:
        return self.man_dist(goal)

    def neighbours(self, board) -> list:
        neigh = [
            # No diagonal neighbours
            (self.x, self.y - 1), # Top
            (self.x - 1, self.y), # Left
            (self.x + 1, self.y), # Right
            (self.x, self.y + 1), # Bottom
        ]

        ugly_neighbours = []
        for n in neigh:
            x, y = n

            if x < 0 or y < 0:
                ugly_neighbours.append((x, y))
            elif x >= len(board) or y >= len(board[0]):
                ugly_neighbours.append((x, y))
            elif board[x][y] == WALL:
                ugly_neighbours.append((x, y))


        for ugly in ugly_neighbours:
            neigh.remove(ugly)

        return [Node(n[0], n[1], self) for n in neigh]

# Defining custom type
Board = list[list[Node]]

def display_board(board, initial: Node, goal: Node) -> None:
    print('', '-' * len(board[0] * 3))

    for i, row in enumerate(board):
        print(end='|')
        for j, col in enumerate(row):
            if Node(i, j) == initial:
                ch='S'
            elif Node(i, j) == goal:
                ch='E'
            elif col == EMPTY:
                ch=' '
            elif col == WALL:
                ch='#'
            elif col == SELECTED:
                ch='.'
            print("{:>3}".format(ch), end='')
        print(end='|\n')

    print('', '-' * len(board[0]) * 3)

def start(board, initial: Node, goal: Node) -> Node:
    opened = []
    closed = [Node(initial.x, initial.y)]
    # Create a copy of board to display the steps of A*
    d_board = []
    for row in board:
        d_board.append([])
        for col in row:
            d_board[-1].append(col)

    # Actual A* Logic
    previous = set()
    while len(closed) > 0:
        closed.sort(key = lambda n: n.heu(initial) + n.heu(goal))
        current = closed.pop(0)
        opened.append(current)
        
        if current in previous:
            continue
        else:
            previous.add(current)
        
        d_board[current.x][current.y] = SELECTED
        print('=' * 40)
        print("Open List:", opened)
        print("Close List:", closed)
        print("\n\nCurrently selected ({}, {})".format(current.x, current.y))
        display_board(d_board, initial, goal)

        if current == goal:
            print("Reached goal!")
            break

        for neighbour in current.neighbours(board):
            if neighbour not in previous:
                closed.append(neighbour)
        
    return current

# For test case validity check
def safety_check(board, initial: tuple[int, int], goal: tuple[int, int]):
    if board[initial[0]][initial[1]] == WALL:
        raise ValueError("Initial Position cannot be a wall")
    if board[goal[0]][goal[1]] == WALL:
        raise ValueError("Goal Position cannot be a wall")
    

def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 1, 0, 0, 1, 1, 1, 1, 0,],
        [0, 1, 0, 0, 0, 0, 0, 1, 0,],
        [0, 0, 1, 1, 1, 1, 1, 1, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]

    initial = (3, 0)
    goal = (2, 5)
    safety_check(board, initial, goal)

    end = start(board, Node(initial[0], initial[1]), Node(goal[0], goal[1]))
    print("\nThe best path is ")
    path = []
    while end:
        path.append((end.x, end.y))
        end = end.prev
    
    # Create a copy of board
    d_board = []
    for row in board:
        d_board.append([])
        for col in row:
            d_board[-1].append(col)
    
    # mutate it with path found
    for (x, y) in path:
        d_board[x][y] = SELECTED
    display_board(d_board, initial, goal)
    

if __name__ == '__main__':
    main()