"""
Given a list of numbers, write a Python program to remove multiple elements
from a list based on the given condition.

Example:

Input: [12, 15, 3, 10]
Output: Remove = [12, 3], New_List = [15, 10]

Input: [11, 5, 17, 18, 23, 50]
Output: Remove = [1:5], New_list = [11, 50]
"""

# Solution1
input_list = [12, 15, 3 ,10]
remove_list = [12, 3]

for elem in remove_list:
    input_list.remove(elem)

print(input_list)

# Solution2
input_list = [11, 5, 17, 18, 23, 50]

del input_list[1:5]
print(input_list)

# Solution3
input_list = [11, 5, 17, 18, 23, 50]
index = [0, 3, 4, 2]

for elem in sorted(index, reverse=True):
    del input_list[elem]

print(input_list)