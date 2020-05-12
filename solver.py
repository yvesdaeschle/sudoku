#https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/

#Lösung:
#864537192
#235981647
#917246583
#173852964
#592164378
#648379251
#781693425
#359428716
#426715839

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

def next_field(board, row, col):

    while row < len(board):
        while col < len(board[row]):
            if col > 7:
                col = 0
                row += 1

            if board[row][col] == 0:
                return (row, col)

            col += 1

    return (len(board), len(board[0]))

print_board(board)
print(next_field(board, 0, 0))
