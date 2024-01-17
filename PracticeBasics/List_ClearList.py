"""
In this article, let’s discuss different ways to clear a list in Python.
Python provides a lot of different ways to clear a list and we will discuss them in this article.

Example

Input: [2, 3, 5, 6, 7]
Output: []
Explanation: Python list is cleared and it becomes empty so we have returned empty list.
"""

# Solution1

lst = [2, 3, 5, 6, 7]
lst.clear()
print(lst)

# Solution2

lst = [2, 3, 54, 'b', 'c']
for i in range(len(lst)):
    lst.pop()

print(lst)

# Solution3
lst = [5, 7,8, 34, 467, 'mahi']
lst = lst[:0]
print(lst)

# Solution4
lst = [1, 2, 3]
del lst[:]
print(lst)
lst.append(1)
print(lst)

# Solution5
lst = [7, 8 ,8 ]
print(lst)
lst = []
print(lst)

# Solution6 using "*=0"

lst = [5, 7, 8, 9]
lst *= 0
print(lst)