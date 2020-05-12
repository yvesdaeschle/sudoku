#https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

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
        
print_board(board)
