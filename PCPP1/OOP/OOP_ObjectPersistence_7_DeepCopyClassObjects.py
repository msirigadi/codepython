"""
Deep copy class objects

Pay attention to the fact that the __init__() method is executed only once,
despite the fact we own two instances of the example class.

This method is not executed for the b_example object as the deepcopy function
copies an already initialized object.
"""
import copy

class Example:
    def __init__(self):
        self.properties = ["112", "997"]
        print("Hello from __init__()")


a_example = Example()
b_example = copy.deepcopy(a_example)
print("Memory chunks:", id(a_example), id(b_example))
print("Same memory chunk?", a_example is b_example)
print("Properties:", a_example.__dict__, b_example.__dict__)
print()
b_example.properties.append("911")
print('a_example.properties:', a_example.properties)
print('b_example.properties:', b_example.properties)