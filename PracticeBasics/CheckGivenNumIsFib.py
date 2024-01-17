"""
Given a number \’n\’, how to check if n is a Fibonacci number. First few
Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ..
Examples :

Input: 8
Output: Yes

Input: 34
Output: Yes

Input: 41
Output: No

Following is an interesting property about Fibonacci numbers that can also
be used to check if a given number is Fibonacci or not.

A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
"""

import math
def perfect_square(num):
    s = int(math.sqrt(num))
    return s * s == num

def fibonacci(num):
    return perfect_square(5 * n**2 + 4) or perfect_square(5 * n**2 - 4)

for n in range(1, 11):
    if fibonacci(n) == True:
        print(n, "is a fibonacci num")
    else:
        print(n, "is not a fibonacci num")

