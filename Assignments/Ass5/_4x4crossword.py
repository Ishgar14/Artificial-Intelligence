Board = list[list[str]]
RESULTS: list[Board] = []


def load_file(fname='./gistfile1.txt') -> list[str]:
    with open(fname) as file:
        return [line.strip() for line in file.readlines()]


def col_str(grid: Board, col: int) -> str:
    # returns word in `col`th column of grid
    return ''.join([grid[i][col] for i in range(len(grid))])


def display_board(board: Board) -> None:
    for word in board:
        print(' '.join(word))


def get_row_words(grid: Board) -> list[str]:
    return [row for row in grid]


def get_col_words(grid: Board) -> list[str]:
    return [col_str(grid, i) for i in range(len(grid))]


def get_all_words(grid: Board) -> list[str]:
    return get_row_words(grid).extend(get_col_words(grid))


def vertical_bucket_exists(size: int, words: list[str], grid: Board) -> bool:
    existence = []
    for i in range(size):
        existence.append(
            any(filter(lambda word: word.startswith(col_str(grid, i)), words)))

    return all(existence)


def start(size: int, words: list[str], grid: Board = [], max_count: int = 50) -> Board:
    # Pick the next word
    # check if vertical buckets for that word are not empty
    # if any bucket is empty then backtrack
    # else proceed further

    for word in words:
        grid.append(word)

        if len(grid) != size and not vertical_bucket_exists(size, words, grid):
            grid.pop()
            continue

        if len(grid) == size:
            column_words = [col_str(grid, i) for i in range(len(grid))]
            column_words_exist = [word in words for word in column_words]

            if not all(column_words_exist):
                grid.pop()
                continue

            RESULTS.append(grid.copy())
            grid.clear()

            if len(RESULTS) >= max_count:
                return


def main() -> None:
    words = load_file()
    start(4, words)

    if len(RESULTS) == 0:
        print("Could not find any such combination")
    else:
        print(" All possible grids are ".center(40, '='))
        for i, matrix in enumerate(RESULTS):
            print(f" Part {i + 1} ".center(40, '-'))
            display_board(matrix)


if __name__ == '__main__':
    main()
