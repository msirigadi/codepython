"""
Given the start and end of a range, write a Python program to print all negative numbers in a given range.

 Examples:

Input: a = -4, b = 5
Output: -4, -3, -2, -1

Input: a = -3, b= 4
Output: -3, -2, -1
"""

# Solution1
a = -4
b = 5
for i in range(-4, 5):
    if i < 0:
        print(i, end=" ")
print()

# Solution2
a = -3
b = 4
nlist = list(filter(lambda x: (x < 0), range(-3,4)))
print(nlist)
