# def load_file(fname='./gistfile1.txt') -> list[str]:
def load_file(fname='C:\VS_Workshop\Sem 6\Artificial Intelligence\Assignments\Ass5\gistfile1.txt') -> list[str]:
    with open(fname) as file:
        return [line.strip() for line in file.readlines()]


Board = list[list[str]]
RESULTS: list[Board] = []


def col_str(grid: Board, col: int) -> str:
    # returns string of `col`th column of grid
    return ''.join([grid[i][col] for i in range(len(grid))])


def display_board(board: Board) -> None:
    for word in board:
        print(' '.join(word))


def start(size: int, words: list[str], grid: Board = [], counter: int = 0) -> Board:
    if len(grid) == size:
        return grid

    # TODO: Create a better filter to match the words
    for word in filter(lambda w: w.startswith(col_str(grid, counter)), words):
        grid.append(word)

        if new_state := start(size, words, grid, counter + 1):
            if new_state not in RESULTS:
                RESULTS.append(new_state.copy())

            start(size, words)
            # return new_state
        else:
            grid.pop()


def main() -> None:
    words = load_file()
    start(4, words)

    print(" All possible grids are ".center(40, '='))
    for i, matrix in enumerate(RESULTS):
        print(f" Part {i + 1} ".center(40, '-'))
        display_board(matrix)


if __name__ == '__main__':
    main()
