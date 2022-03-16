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

def row_words(grid: Board) -> list[str]:
    return [row for row in grid]

def col_words(grid: Board) -> list[str]:
    return [col_str(grid, i) for i in range(len(grid))]

def all_words_of(grid: Board) -> list[str]:
    words = row_words(grid)
    words.extend(col_words(grid))
    return words

def generate_trie(words: list[str]) -> dict:
    root = {}
    for word in words:
        current = root
        for letter in word:
            current[letter] = current.get(letter, {})
            current = current[letter]

    return root


def vertical_bucket_exists(trie: dict, grid: Board) -> bool:
    column_words = [col_str(grid, i) for i in range(4)]

    for word in column_words:
        current = trie
        for letter in word:
            current = current.get(letter, None)
            if current is None:
                return False

    return True


def word_exists(word: str, trie: dict) -> bool:
    current = trie

    for letter in word:
        current = current.get(letter, None)
        if current is None:
            return False

    return True


def start(size: int, words: list[str], trie: dict, grid: Board = [], 
        filter_duplicate_words: bool = False, max_count: int = 50) -> Board:
    # Pick the next word
    # check if vertical buckets for that word are not empty
    # if any bucket is empty then backtrack
    # else proceed further

    if len(grid) == size:
        column_words = [col_str(grid, i) for i in range(size)]
        column_words_exist = [
            word_exists(word, trie)
            for word in column_words
        ]

        if not all(column_words_exist):
            grid.pop()
            return None

        return grid

    for word in words:
        grid.append(word)

        if not vertical_bucket_exists(trie, grid):
            grid.pop()
            continue

        if len(RESULTS) >= max_count:
            return None

        if filter_duplicate_words:
            all_words = all_words_of(grid)
            if len(all_words) != len(set(all_words)):
                grid.pop()
                continue

        if val := start(size, words, trie, grid):
            if val not in RESULTS:
                RESULTS.append(val.copy())
                grid.pop()



def main() -> None:
    words = load_file()
    start(4, words, generate_trie(words))

    if len(RESULTS) == 0:
        print("Could not find any such combination")
    else:
        print(" All possible grids are ".center(40, '='))
        for i, matrix in enumerate(RESULTS):
            print(f" Part {i + 1} ".center(40, '-'))
            display_board(matrix)


if __name__ == '__main__':
    main()
    # print(word_exists("goat", load_file()) + 1)
    # from pprint import pprint
    # print(generate_trie(load_file()))
