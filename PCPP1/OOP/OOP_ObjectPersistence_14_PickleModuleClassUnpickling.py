"""
class unpickling

We see no errors, so we might conclude that the Cucumber class and object were
pickled successfully, and now we can retrieve them from the file. In fact,
only the object is persisted but not its definition allowing us to determine
the attribute layout:

The remedy for the above problems is: the code that calls the load() or loads()
functions of pickle should already know the function/class definition.
"""

import pickle

# NOTE: If the class is not defined during deserialization, then pickle module
# will throw AttributeError
class Cucumber:
    def __init__(self):
        self.size = 'small'

    def get_size(self):
        return self.size

with open('cucumber.pck1', 'rb') as file_in:
    data = pickle.load((file_in))

print(type(data))
print(data)
print(data.size)
print(data.get_size())