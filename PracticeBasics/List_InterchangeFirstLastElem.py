"""
Given a list, write a Python program to swap first and last element of the list.

Examples:

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
"""

# Solution1

lst = [12, 35, 9, 56, 24]

lst[0], lst[-1] = lst[-1], lst[0]
print(lst)

# Solution2 using temp variable

lst = [1, 2, 3]

length = len(lst)
temp = lst[0]
lst[0] = lst[length-1]
lst[length-1] = temp
print(lst)

