"""
Given two matrices X and Y, the task is to compute the sum of two matrices and then print it in Python.

Examples:

Input :
 X= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

Output :
 result= [[10,10,10],
         [10,10,10],
         [10,10,10]]
"""

# Solution1

x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[9, 8 , 7],
     [6, 5, 4],
     [3, 2, 1]]

sum = []

for i in range(len(x)):
     r1 =[]
     for j in range(len(x[i])):
          r1.append(x[i][j] + y[i][j])
     sum.append(r1)

print(sum)

# Solution2
x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[9, 8 , 7],
     [6, 5, 4],
     [3, 2, 1]]

sum = [[x[i][j] + y[i][j] for j in range(len(x[i]))] for i in range(len(x))]
print(sum)

# Solution3
     

