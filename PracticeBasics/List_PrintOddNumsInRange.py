"""
Given starting and endpoints, write a Python program to print all odd numbers in that given range.

Example:

Input: start = 4, end = 15
Output: 5, 7, 9, 11, 13, 15

Input: start = 3, end = 11
Output: 3, 5, 7, 9, 11
Example #1: Print all odd numbers from the given list using for loop

Define the start and end limit of the range.
Iterate from start till the range in the list using for loop and
check if num % 2 != 0.
If the condition satisfies, then only print the number.
"""

# Solution1
start = 4
end = 15

lst = []
for elem in range(start, end + 1):
    if elem % 2:
        lst.append(elem)

print(lst)

# Solution2
start = 3
end = 11
lst1 = []

while (start <= end):
    if start % 2:
        lst1.append(start)
    start+=1

print(lst1)

# Solution3
start = 5
end = 10
odd_range = [elem for elem in range(start, end) if elem%2]
print(odd_range)

# Solution4
start = 10
end = 20

odd_list = list(filter(lambda x: x%2, range(start, end)))
print(odd_list)

# Solution5
start, end = 4, 19

for elem in range(start, end+1):
    if elem | 1 == elem:
        print(elem, end= " ")

print()

# Solution6
def odd_range(start, end):
    lst = []


    while start <= end:
        if start % 2:
            lst.append(start)

        return lst + odd_range(start+1, end)
    else:
        return lst

start, end = 30, 35
print(odd_range(start, end))
