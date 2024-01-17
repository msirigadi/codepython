"""
Given a list in Python and provided the positions of the elements,
write a program to swap the two elements in the list.

Examples:

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""

# Solution1

lst = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

lst[pos1-1], lst[pos2-1] = lst[pos2-1], lst[pos1-1]

print(lst)

# Solution2 using builtin pop()

def swapElem(lst, pos1, pos2):
    swap_elem1 = lst.pop(pos1)
    print(lst)
    swap_elem2 = lst.pop(pos2-1)

    print(lst)
    lst.insert(pos1, swap_elem2)
    lst.insert(pos2, swap_elem1)

    return lst

lst = [1, 2, 3, 4, 5]
pos1 = 2
pos2 = 5

print(swapElem(lst, pos1-1, pos2-1))