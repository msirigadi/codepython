"""
Sometimes, while working with data, we can have problem in which we need to perform
the extraction of only unique values from dictionary values list.
This can have application in many domains such as web development.
Lets discuss certain ways in which this task can be performed.

The original dictionary is : {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]
"""

# Solution1

input_dict = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}

unique_list = []

for val in input_dict.values():
    for elem in val:
        if elem not in unique_list:
            unique_list.append(elem)

print(sorted(unique_list))

# Solution 2

unique_list = list({elem for val in input_dict.values() for elem in val})
print(unique_list)