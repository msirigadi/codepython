"""
Now it’s time to unpickle the contents of the file.

The presented code is quite simple:

- we’re importing a pickle module;
- the file is opened in binary mode and the file handle is associated with
the file;
- we consecutively read some portions of data and deserialize it with the
load() function;
- finally, we examine the type and contents of the objects.

Pay attention to the fact that with the 'pickle' module, you have to remember
the order in which the objects were persisted and the deserialization code
should follow the same order.
"""

import pickle

with open('multidata.pck1', 'rb') as file_in:
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)

print(data1)
print(type(data1))
print(data2)
print(type(data2))