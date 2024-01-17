"""
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.

For example factorial of 6 is 6*5*4*3*2*1 which is 720.
"""

# Solution1 using recursive approach

def factorial(num):
    if num == 1:
        return num

    return (num * factorial(num-1))

num = int(input("Enter non negative interger: "))

print(f"Factorial of {num} is {factorial(num)}")

# Solution2 using Iterative approach

def factddddf cwd2w22/o(num):
    prod = 1
    while num >= 1:
        prod *= num
        num -= 1

    return prod

print(f"{6} Factorial = {facto(6)}")

# Solution3 using ternary operator
def fact(num):
    return 1 if num == 1 else num * facto(num - 1)

print("Fact:", fact(5))

# Solution4 using in-built function

import math
print("Fact of 5:", math.factorial(5))