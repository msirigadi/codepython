"""
Given a list of numbers, write a Python program to find the sum of all the elements in the list.

Example:

Input: [12, 15, 3, 10]
Output: 40

Input: [17, 5, 3, 5]
Output: 30
"""

# Solution1
lst = [12, 15, 3 ,10]
print("Sum:", sum(lst))

# Solution2
lst = [17, 5, 3 ,5]
sum = 0
for elem in lst:
    sum+= elem

print("Sum:", sum)

# Solution3 using recursion
def sum_of_elements(lst):
    if len(lst) == 0:
        return 0

    return lst[0] + sum_of_elements(lst[1:])

if __name__ == "__main__":
    lst = [10, 20, 30, 40, 50]
    #lst = []
    print("Sum:", sum_of_elements(lst))

