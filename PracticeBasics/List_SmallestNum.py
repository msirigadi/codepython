"""
We are given a list of numbers and our task is to write a Python program to
find the smallest number in given list. For the following program we can use various methods
including the built-in min method, sorting the  array and returning the last element, etc.
Example:

Input : list1 = [10, 20, 4]
Output : 4

Input : list2 = [20, 10, 20, 1, 100]
Output : 1
"""

# Solution1
lst1 = [10, 20 ,4]
print("Min:", min(lst1))

# Solution2
lst2 = [20, 10, 20, 1, 100]
lst2.sort()
print(lst2)
print("Min:", lst2[0])

# Solution3
lst = [ 11, 34, 67, 21, 8, 100, 8]
min = lst[0]
for elem in lst[1:]:
    if elem < min:
        min = elem

print("Min:", min)
