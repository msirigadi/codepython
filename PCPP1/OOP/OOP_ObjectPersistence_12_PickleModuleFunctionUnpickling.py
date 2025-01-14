"""
Function unpickling
"""

import pickle

# If this function does't exist then the pickle module will throw AttributeError
def f1():
    print('Hello from the jar!')

with open('function.pck1', 'rb') as file_in:
    data = pickle.load(file_in)

print(data)
print(type(data))
data()