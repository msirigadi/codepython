"""
The same information stored in __class__could be retrieved by calling a type()
function with one argument:
"""

for element in (1, 'a', True):
    print(element, 'is', element.__class__, type(element))