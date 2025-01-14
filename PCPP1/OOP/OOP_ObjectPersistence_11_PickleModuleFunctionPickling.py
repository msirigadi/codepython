"""
functions (both built-in and user-defined) are pickled by their name reference,
not by any value. This means that only the function name is pickled; neither
the function’s code, nor any of its function attributes, are pickled.

Similarly, classes are pickled by named reference, so the same restrictions in
the unpickling environment apply. Note that none of the class’s code or data
are pickled.

This is done on purpose, so you can fix bugs in a class or add methods to the
class, and still load objects that were created with an earlier version of the
class.

Hence, your role is to ensure that the environment where the class or function
is unpickled is able to import the class or function definition. In other
words, the function or class must be available in the namespace of your code
reading the pickle file.

Otherwise, an AtrributeError exception will be raised.
"""

import pickle

def f1():
    print('Hello from the jar!')

with open('function.pck1', 'wb') as file_out:
    pickle.dump(f1, file_out)

