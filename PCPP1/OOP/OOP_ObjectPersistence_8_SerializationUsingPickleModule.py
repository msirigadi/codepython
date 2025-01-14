"""
Pickle module is used to persist python objects for later use

The simplest way to persist outcomes is to generate a flat text file and to
write your outcomes. It’s a very simple thing to do way which is not suitable
for persisting sets of different types of objects or nested structures.

In Python, object serialization is the process of converting an object
structure into a stream of bytes to store the object in a file or database, or
to transmit it via a network. This byte stream contains all the information
necessary to reconstruct the object in another Python script.

This reverse process is called deserialization.

Python objects can also be serialized using a module called 'pickle', and using
this module, you can 'pickle' your Python objects for later use.

The 'pickle' module is a very popular and convinient module for data
serialization in the world of Pythonistas.

So, what can be pickled and then unpickled?

The following types can be pickled:

- None, booleans;
- integers, floating-point numbers, complex numbers;
- strings, bytes, bytearrays;
- tuples, lists, sets, and dictionaries containing pickleable objects;
- objects, including objects with references to other objects (remember to
avoid cycles!)
- references to functions and classes, but not their definitions.

Let's pickle our first set of data consisting of:

a nested dictionary carrying some information about currencies;
a list containing a string, an integer, and a list.

In this result, we have created a file that retains the pickled objects.
"""

import pickle

a_dict = dict()
a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]

with open('multidata.pck1', 'wb') as file_out:
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)
