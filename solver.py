#https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/

board = [
    [0,0,0,0,0,0,1,9,0],
    [2,3,0,0,0,0,6,0,0],
    [0,0,0,2,4,0,0,0,0],
    [0,0,0,0,0,0,9,6,0],
    [0,0,0,1,6,0,0,7,0],
    [0,4,8,0,7,0,0,0,0],
    [0,0,1,0,0,3,4,0,5],
    [0,0,9,0,0,8,0,0,0],
    [0,0,6,0,0,5,8,0,0]
]

def solve(board):
    next = next_field(board)
    if not next: #end of board
        return True
    else:
        row, col = next

    for n in range(1, 10):
        if check(board, n, row, col):
            board[row][col] = n
            
            if solve(board):
                return True

            board[row][col] = 0

    return False

def print_board(board):
    for n in range(len(board)):
        if n % 3 == 0 and n != 0:
            print('- - - - - - - - - - - -')

        for i in range(len(board[n])):
            if i % 3 == 0 and i !=0:
                print(' | ', end='')

            print(board[n][i], end=' ')

            if i == 8:
                print()

def next_field(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)

    return None

def check(board, val, row, col):
    # check row
    for i in range(len(board[row])):
        if board[row][i] == val:
            return False

    # check col
    for i in range(len(board)):
        if board[i][col] == val:
            return False

    # check section
    for i in range(row // 3 * 3, row // 3 * 3 + 3):
        for j in range(col // 3 * 3, col // 3 * 3 + 3):
            if board[i][j] == val:
                return False

    return True

print_board(board)
solve(board)
print('- - - - - - - - - - - ')
print_board(board)
