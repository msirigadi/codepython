"""
Given a list of numbers, write a Python program to print all positive numbers in given list.

Example:

Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64

Input: list2 = [12, 14, -95, 3]
Output: [12, 14, 3]
"""

# Solution1

list1 = [12, -7, 5, 64, -14]

for elem in list1:
    if elem >= 0:
        print(elem, end=" ")

print()

# Solution2
list2 = [12, 14, -95, 3]
plist = list(filter(lambda x: x >= 0, list2))
print(plist)

# Solution3
list3 = [-1, - 30, -43, 43, 5, -6]
plist = [elem for elem in list3 if elem >= 0]
print(plist)

