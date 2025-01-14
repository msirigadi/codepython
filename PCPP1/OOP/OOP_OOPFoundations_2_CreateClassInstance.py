"""
An instance is one particular physical instantiation of a class that occupies
memory and has data elements. This is what 'self' refers to when we deal with
class instances.

An object is everything in Python that you can operate on, like a class,
instance, list, or dictionary.

The term instance is very often used interchangeably with the term object,
because object refers to a particular instance of a class. It’s a bit of a
simplification, because the term object is more general than instance.

The relation between instances and classes is quite simple: we have one class
of a given type and an unlimited number of instances of a given class.

Each instance has its own, individual state (expressed as variables, so objects
again) and shares its behavior (expressed as methods, so objects again).

To create instances, we have to instantiate the class:

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")


In the example presented above, we have created three different instances based
on the Duck class: duckling, drake and hen. We haven't called any object
attributes.
"""

class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print("Quack")

# NOTE: You can use named variable like x=abc instead of passing just abc

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")