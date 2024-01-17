"""
Given a list of numbers, the task is to write a Python program to find the second largest number in the given list.

Examples:

Input: list1 = [10, 20, 4]
Output: 10

Input: list2 = [70, 11, 20, 4, 100]
Output: 70
"""

# Solution1
lst = [10, 20, 4]
n = 2
lst.sort()
print(n, "largest num is", lst[n-1])

# Solution2
lst = [70, 11, 20, 4 ,100]
n=2
lst.sort(reverse=True)
print("Second largest num:", lst[-n])



