"""
Given a list of integers, the task is to find N largest elements assuming
size of list is greater than or equal o N.

Examples :

Input : [4, 5, 1, 2, 9]
        N = 2
Output :  [9, 5]

Input : [81, 52, 45, 10, 3, 2, 96]
        N = 3
Output : [81, 96, 52]
"""

# Solution1

lst = [4, 5, 1, 2, 9]
n = 2

largest_elem_list = []

lst.sort()
for i in range(1, n +1):
    largest_elem_list.append(lst[-i])

print(n, "largest elems:", largest_elem_list)

# Solution2
lst1 = [81, 52, 45, 10, 3, 2, 96]
lst = lst1[:]
n = 3
lar_elem_list = []
for i in range(3):
    lar = max(lst)
    lar_elem_list.append(lar)
    lst.remove(lar)

print(lar_elem_list)
print(lst1)

# Solution3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 7 ,1 , 8, 2]
n = 3
lst.sort()
set_list = set(lst)
print(set_list)
list = list(set_list)
lar_elem_list = []

for i in range(3):
    lar_elem_list.append(list.pop())

print(lar_elem_list)
