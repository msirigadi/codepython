"""
Given a positive integer N. The task is to find 1**2 + 2**2 + 3**2 + ….. + N**2.

Input : N = 4
Output : 30
12 + 22 + 32 + 42
= 1 + 4 + 9 + 16
= 30

Input : N = 5
Output : 55
"""

def sum_of_squares(num):
    sum = 0
    for i in range(1, num+1):
        sum += i** 2

    return sum

print(sum_of_squares(4))
print(sum_of_squares(5))

