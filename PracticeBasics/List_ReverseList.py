"""
Python provides us with various ways of reversing a list. We will go through
some of the many techniques on how a list in Python can be reversed.

Example:

Input: list = [4, 5, 6, 7, 8, 9]
Output: [9, 8, 7, 6, 5, 4]
Explanation: The list we are having in the output is reversed to the list we have in the input.
"""

# Solution1

lst = [4, 5, 6, 7, 8, 9]
lst.reverse()
print(lst)

# Solution2
lst = [3, 5, 7, 89, 890]
print(lst[::-1])

# Solution3
lst = ['a', 1, 'c', 'd', 1000]
len = len(lst)
for i in range(len//2):
    j = len - i -1
    lst[i], lst[j] = lst[j], lst[i]

print(lst)

# Solution4
lst = [11, 22 ,33 ,44, 55 ,66]
rlst = list(reversed(lst))
print(rlst)

# Solution5

lst = ['m', 'a', 'h', 'i']
l = []
for elem in lst:
    l.insert(0, elem)

print(l)

