"""
If you want to make an independent copy of a compound object (list, dictionary,
custom class instance) you should make use of deep copy, which:

- constructs a new compound object and then, recursively, inserts copies into it
of the objects found in the original;
- takes more time to complete, as there are many more operations to be performed;
- is implemented by the deepcopy() function, delivered by the python 'copy'
module

The general idea should be depicted like this:

    Shallow copy                Deep copy
a_list      b_list          a_list                b_list
    |       |                   |                   |
        |                       |                   |
    memory chunk            memory chunk        memory chunk
                                #1                  #2

The 'copy' module contains a function for shallow copying: copy(). Of course,
you could say that for copying lists there is already the [:] notation, or
a_list=list(b_list), and for dictionaries you could use a_dict = dict(b_dict).

But think about making use of polymorphism when you need a universal function
to copy any type object, so that in that case using a copy() function is the
smart way to accomplish the task.
"""

import copy

print("Let's make a deep copy")
a_list = [10, 'banana', [997, 123]]
b_list = copy.deepcopy(a_list)
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print()
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)