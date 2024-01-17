"""
Given a list of numbers, write a Python program to print all even numbers in the given list.

Example:

Input: list1 = [2, 7, 5, 64, 14]
Output: [2, 64, 14]
Input: list2 = [12, 14, 95, 3]
Output: [12, 14]
"""

# Solution1
list1 = [2,7,5,64,14]

for elem in list1:
    if elem % 2 == 0:
        print(elem, end = " ")
print()


# Solution2
lst = [12, 14, 95, 3]
even_list = [elem for elem in lst if elem%2 == 0]
print(even_list)

# Solution3
lst = [22, 45, 67,88, 10]

even_list = list(filter(lambda x: (x%2 == 0), lst))
print(even_list)

# Solution4
def even_num(lst):
    even_lst = []

    if not lst:
        return even_lst

    if lst[0] % 2 == 0:
        even_lst.append(lst[0])

    return even_lst + even_num(lst[1:])

if __name__=="__main__":
    lst = [3, 4, 5, 7, 8, 9, 11]
    print(even_num(lst))

