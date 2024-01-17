"""
Given a list, print the value obtained after multiplying all numbers in a Python list.

Examples:

Input :  list1 = [1, 2, 3]
Output : 6
Explanation: 1*2*3=6

Input : list1 = [3, 2, 4]
Output : 24
"""

# Solution1
lst1 = [1, 2, 3]
prod = 1
for elem in lst1:
    prod *= elem

print("Prod:", prod)


# Solution2

def prod_of_elements(lst):
    print(lst)
    #if len(lst) == 0:
    if not lst:
        return 1

    return lst[0] * prod_of_elements(lst[1:])

if __name__ == "__main__":
    lst = [3, 2,4]
    lst = []
    print("Prod:", prod_of_elements(lst))


# Solution3
import math
lst =[1, 2 ,3]
print("Prod:", math.prod(lst))