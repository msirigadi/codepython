"""
Add two numbers
"""

# Solution 1
num1 = 5
num2 = 3

print("Addition of {} and {} is {}".format(num1, num2, num1 + num2))

# Solution 2 using input()

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("sum of", num1, "and", num2, "is", num1 + num2)

# Solution3 defining add function

def add(num1, num2):
    return num1 + num2

num1 = 10
num2 = 5

print("Sum of {0} and {1} is {2}".format(num1, num2, add(num1, num2)))

# Solution4 using operator.add()

num1 = 20
num2 = 30

import operator

sum_nums = operator.add(num1, num2)
print("Sum of {0} and {1} is {2}".format(num1, num2, sum_nums))

# Solution5 using lambda functions

num1 = 100
num2 = 200

sn = lambda num1, num2:  num1 + num2

print("Sum: ", sn(num1, num2))