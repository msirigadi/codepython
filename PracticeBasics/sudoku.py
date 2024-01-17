rows = 9
cols = 9

sudoku = True

board1 = [[2, 9, 5, 7, 4, 3, 8, 6, 1],
          [4, 3, 1, 8, 6, 5, 9, 2, 7],
          [8, 7, 6, 1, 9, 2, 5, 4, 3],
          [3, 8, 7, 4, 5, 9, 2, 1, 6],
          [6, 1, 2, 3, 8, 7, 4, 9, 5],
          [5, 4, 9, 2, 1, 6, 7, 3, 8],
          [7, 6, 3, 5, 2, 4, 1, 8, 9],
          [9, 2, 8, 6, 7, 1, 3, 5, 4],
          [1, 5, 4, 9, 3, 8, 6, 7, 2]]
"""
board = [[1 for c in range(cols)]for r in range(rows)]

for r in range(rows):
    for c in range(cols):
        board[r][c] = int(input("Enter int val: "))

    print()
"""

for r in range(rows):
    for c in range(cols):
        print(board1[r][c], end=" ")

    print()

uniq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for r in range(rows):
    for elem in uniq:
        if board1[r].count(elem) > 1:
            sudoku = False
            break

    if not sudoku:
        break

if sudoku:
    print("Yes")
else:
    print("No")



