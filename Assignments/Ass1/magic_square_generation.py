def generate(size: int) -> list:
    EMPTY = 0
    square = []

    # Generate a square of dimensions `size`
    for _ in range(size):
        buffer = []
        
        for _ in range(size):
            buffer.append(EMPTY)

        square.append(buffer)

    counter = 1

    row = 0
    col = len(square) // 2

    # Pick middle of first row as 1
    square[row][col] = counter

    while counter != size ** 2:
        print("\n", f" Step {counter} ".center(20, '='), sep='')
        display(square)
        counter       += 1
        cyclic_row    = row - 1
        cyclic_column = col + 1

        cyclic_row    = cycle(cyclic_row, size)
        cyclic_column = cycle(cyclic_column, size)

        # Check if North-East slot is available
        if square[cyclic_row][cyclic_column] == 0:
            square[cyclic_row][cyclic_column] = counter
            row, col = cyclic_row, cyclic_column
        else:
            # Otherwise go South
            row += 1
            square[row][col] = counter

    return square

# For verbosity ... The entire thing could've been a single % opeartion lmao
def cycle(number: int, size: int) -> int:
    if number == size:
        return 0

    elif number > size:
        return number % size

    elif number < 0:
        number *= -1
        number %= size
        number = size - number
        return number
        
    else:
        return number


def display(board: list) -> None:
    for row in board:
        for col in row:
            print('{:5}'.format(col), end='')
        print()


def main():
    while True:
        size = int(input("Enter size of square: "))
        if size % 2 == 0:
            print("Please type an odd number!")
            continue

        board = generate(size)
        print("\n", f" Step {size ** 2} ".center(20, '='))
        display(board)
        break


if __name__ == '__main__':
    main()
