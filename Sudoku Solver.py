
grid = 50 [[3, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 7, 0, 0, 0], [7, 0, 6, 0, 3, 0, 5, 0, 0], [0, 7, 0, 0, 0, 9, 0, 8, 0], [9, 0, 0, 0, 2, 0, 0, 0, 4], [0, 1, 0, 8, 0, 0, 0, 5, 0], [0, 0, 9, 0, 4, 0, 3, 0, 1], [0, 0, 0, 7, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 8, 0, 0, 6]]


def solve(board):
    position = find_empty(board)
    if position is None:
        return True
    for num in range(1, 10):
        if is_valid(board, position, num):
            board[position[0]][position[1]] = num
            if solve(board):
                return True
            board[position[0]][position[1]] = 0
    return False


def print_board(board):
    for n in board:
        print(n)


def find_empty(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return (y, x)
    return None


def is_valid(board, position, num):
    # Checks row
    for row in range(9):
        if board[position[0]][row] == num:
            return False

    # Checks column
    for col in range(9):
        if board[col][position[1]] == num:
            return False

    # Checks subgrid
    subgridY = (position[0] // 3)*3
    subgridX = (position[1] // 3)*3
    for y in range(subgridY, subgridY+3):
        for x in range(subgridX, subgridX+3):
            if board[y][x] == num:
                return False
    return True


print_board(grid)
solve(grid)
print("Solving")
print("------------------------")
print_board(grid)
print(grid[0][0])