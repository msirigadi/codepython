"""
The same deepcopy() method could be utilized when you want to copy dictionaries
or custom class objects.
"""

import copy

a_dict = {
    'first name': 'James',
    'last name': 'Bond',
    'movies': ['Goldfinger (1964)', 'You only live twice']
}

b_dict = copy.deepcopy(a_dict)
print('Memory chunks:', id(a_dict), id(b_dict))
print('Same memory chunk?', a_dict is b_dict)
print("Let's modify the movies list")
a_dict['movies'].append('Diamonds are forever (1971)')
print('a_dict movies:', a_dict['movies'])
print('b_dict movies:', b_dict['movies'])