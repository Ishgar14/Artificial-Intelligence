STUCK = 0
DONE  = 1

def generate(size: int) -> list:
    EMPTY  = 0
    square = []

    # Generate a square of dimensions `size`
    for _ in range(size):
        buffer = []
        
        for _ in range(size):
            buffer.append(EMPTY)

        square.append(buffer)

    return square

# This function reutrns true if given position is safe for new queen
def is_safe(board: list, row: int, col: int) -> bool:
    # Check the row
    for i in range(len(board)):
        if board[row][i] == 1:
            return False

    # Check the column
    for i in range(len(board)):
        if board[i][col] == 1:
            return False
    
    # Check the left diagonal
    for difference in range(1, len(board)):
        _row = row - difference
        _col = col - difference

        if _row < 0 or _col < 0:
            break
        if board[_row][_col] == 1:
            return False

    for difference in range(1, len(board)):
        _row = row + difference
        _col = col + difference

        if _row >= len(board) or _col >= len(board):
            break

        if board[_row][_col] == 1:
            return False
    
    
    # Check the right diagonal
    for difference in range(1, len(board)):
        _row = row + difference
        _col = col - difference

        if _row >= len(board) or _col < 0:
            break
        if board[_row][_col] == 1:
            return False

    for difference in range(1, len(board)):
        _row = row - difference
        _col = col + difference

        if _row < 0 or _col >= len(board):
            break

        if board[_row][_col] == 1:
            return False
    
    return True

# This function takes board and row and returns all safe column spots of that row
def get_all_safe_spots(board: list, row: int) -> list:
    spots = []
    for column in range(len(board)):
        if is_safe(board, row, column):
            spots.append(column)
    return spots


def solve(board: list, row: int = 0) -> int:
    if row >= len(board):
        return DONE

    spots = get_all_safe_spots(board, row)
    if len(spots) == 0:
        return STUCK

    for spot in spots:
        board[row][spot] = 1

        # If we can't place next queen then backtrack and select next position for current queen
        if solve(board, row + 1) == STUCK:
            board[row][spot] = 0

    # If every position of queen is filled then its done
    if sum([sum(row) for row in board]) == len(board):
        return DONE
    else:
        # Otherwise backtrack
        return STUCK
            

def display_board(board: list, special: bool = True) -> None:
    if not special:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                   print('{:3}'.format(1), end='')
                else:
                    print('{:>3}'.format('.'), end='')
            print()
        return
    
    # Solid: █   ⬛
    # Empty: ░   ⬜
    # Queen: ♕  👑
    for i in range(len(board)):
        solid = i % 2 == 0
        for j in range(len(board)):
            if board[i][j] == 1:
                print('{:>3}'.format('👑'), end='')
            else:
                if solid:
                    print('{:>3}'.format('⬛'), end='')
                else:
                    print('{:>3}'.format('⬜'), end='')
            solid = not solid
        print()
        
def main() -> None:
    size  = int(input("Enter size of chessboard: "))
    board = generate(size)
    solve(board)

    if sum([sum(row) for row in board]) != len(board):
        print("There are no valid queen positions for given dimensions of board")
        return

    display_board(board, True)

if __name__ == '__main__':
    main()