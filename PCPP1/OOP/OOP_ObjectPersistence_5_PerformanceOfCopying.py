"""
we'll compare the performance of three ways of copying a large compound object
(a million three-element tuples).

The first approach is a simple reference copy. This is done very quickly, as
there’s nearly nothing to be done by the CPU – just a copy of a reference to
'a_list'.

The second approach is a shallow copy. This is slower than the previous code,
as there are 1,000,000 references (not objects) created.

The third approach is a deep copy. This is the most comprehensive operation,
as there are 3,000,000 objects created.
"""

import copy
import time

a_list = [(1, 2, 3) for x in range(1_000_000)]

print('Single reference copy')
time_start = time.time()
b_list = a_list
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)

print()
print('Shallow copy')
time_start = time.time()
b_list = a_list[:]
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)

print()
print('Deep copy')
time_start = time.time()
b_list = copy.deepcopy(a_list)
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)
