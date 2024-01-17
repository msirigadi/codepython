"""
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
Test your code using the data we've provided.

Test data
Sample input:

295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
"""
sudoku = [[2, 9, 5, 7, 4, 3, 8, 6, 1],
          [4, 3, 1, 8, 6, 5, 9, 2, 7],
          [8, 7, 6, 1, 9, 2, 5, 4, 3],
          [3, 8, 7, 4, 5, 9, 2, 1, 6],
          [6, 1, 2, 3, 8, 7, 4, 9, 5],
          [5, 4, 9, 2, 1, 6, 7, 3, 8],
          [7, 6, 3, 5, 2, 4, 1, 8, 9],
          [9, 2, 8, 6, 7, 1, 3, 5, 4],
          [1, 5, 4, 9, 3, 8, 6, 7, 2]]

is_sudoku = True

elems_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for row in sudoku:
    for elem in elems_to_check:
        if elem not in row:
            is_sudoku = False
            break

matrix1 = [[sudoku[j][i] for j in range(9)] for i in range(9)]
for row in matrix1:
    for elem in elems_to_check:
        if elem not in row:
            is_sudoku = False
            break

if is_sudoku:
    print("Yes")
else:
    print("No")