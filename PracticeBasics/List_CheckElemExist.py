"""
The list is an important container in Python as it stores elements of all the data types
as a collection. Knowledge of certain list operations is necessary for day-day programming.
This article discusses the Fastest way to check if a value exists in a list or not using Python.

Example

Input: test_list = [1, 6, 3, 5, 3, 4]
            3  # Check if 3 exist or not.
Output: True
Explanation: The output is True because the element we are looking is exist in the list.
"""

# Solution1 using in

test_list = [1, 6, 3, 5, 3, 4]

print("Elem 3 in list:", 3 in test_list)

# Solution 2
elem_to_search = 3

exist = False

for item in test_list:
    if item == elem_to_search:
        exist = True
        break

print("Elem in list:", exist)

# Solution3 using find
lst = list(map(str, test_list))
str = "".join(lst)
if str.find('3') != -1:
    found = True
else:
    found = False

print("Elem exist:", found)

# Solution4 try except
try:
    test_list.index(3)
    found = True
except:
    found = False

print("Elem exist:", found)