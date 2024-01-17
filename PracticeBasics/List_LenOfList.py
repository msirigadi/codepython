"""
List being an integral part of Python day-to-day programming has to be learned by all
Python users and having a knowledge of its utility and operations is essential and always
a plus. So this article discusses one such utility of finding the no. of elements in a
list using Python.

Example:

Input: lst = [10,20,30,40]
Output: 4
Explanation: The output is 4 because the length of the list is  4.
"""

# Solution1 using len

lst = [10, 20, 30, 40]
print("Length:", len(lst))

# Solution2 using iteration

lst = [1,2,3,4,5]
cnt = 0
for elem in lst:
    cnt += 1

print("Length:", cnt)


# Solution3 using list comprehension
lst = [1, 24,54,657,2,5,7,8,88]

lst = [index + 1 for index,elem in enumerate(lst)]
print("Length: ", lst[-1])


