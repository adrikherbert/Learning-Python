# Sudoku Solver -- Adrik Herbert
# Dec 24 2020

board = [['-', 7, '-', 2, '-', 5, '-', '-', '-'],
         [4, '-', '-', 9, 8, '-', '-', '-', '-'],
         ['-', '-', 8, '-', '-', '-', 6, '-', '-'],
         [3, 8, '-', '-', 2, '-', '-', '-', 4],
         ['-', 1, '-', '-', '-', '-', '-', 6, '-'],
         [9, '-', '-', '-', 1, '-', '-', 3, 8],
         ['-', '-', 5, '-', '-', '-', 9, '-', '-'],
         ['-', '-', '-', '-', 5, 4, '-', '-', 3],
         ['-', '-', '-', 7, '-', 8, '-', 4, '-']]


def print_board(board):
    for i in range(9):
        for j in range(9):
            print(f'{board[i][j]} ', end='')
        print()


def check_candidate(num, row, col):
    if num in board[row]:
        return False

    for i in range(len(board)):
        if board[i][col] == num:
            return False

    sq_coord = ()
    if row < 3 and col < 3:
        sq_coord = (0, 0)
    elif row < 3 and col < 6:
        sq_coord = (0, 3)
    elif row < 3 and col < 9:
        sq_coord = (0, 6)
    elif row < 6 and col < 3:
        sq_coord = (3, 0)
    elif row < 6 and col < 6:
        sq_coord = (3, 3)
    elif row < 6 and col < 9:
        sq_coord = (3, 6)
    elif row < 9 and col < 3:
        sq_coord = (6, 0)
    elif row < 9 and col < 6:
        sq_coord = (6, 3)
    elif row < 9 and col < 9:
        sq_coord = (6, 6)

    sq_coords = []
    for i in range(9):
        if i < 3:
            sq_coords.append((sq_coord[0], sq_coord[1] + i))
        elif i < 6:
            sq_coords.append((sq_coord[0] + 1, sq_coord[1] + i - 3))
        elif i < 9:
            sq_coords.append((sq_coord[0] + 2, sq_coord[1] + i - 6))

    for i in range(9):
        if board[sq_coords[i][0]][sq_coords[i][1]] == num:
            return False

    return True


def solve():
    for row in range(9):
        for col in range(9):
            if board[row][col] == '-':
                for i in range(1, 10):
                    if check_candidate(i, row, col):
                        board[row][col] = i
                        solve()
                        board[row][col] = '-'
                return

    print_board(board)


solve()
