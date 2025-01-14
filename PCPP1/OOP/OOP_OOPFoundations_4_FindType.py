"""
A type is one of the most fundamental and abstract terms of Python:

*   it is the foremost type that any class can be inherited from;
    as a result, if you’re looking for the type of class, then type is returned;
*   in all other cases, it refers to the class that was used to instantiate the
    object; it’s a general term describing the type/kind of any object;
*   it’s the name of a very handy Python function that returns the class
    information about the objects passed as arguments to that function;
*   it returns a new type object when type() is called with three arguments;
    we'll talk about this in the 'metaclass' section.

Python comes with a number of built-in types, like numbers, strings, lists,
etc., that are used to build more complex types.Creating a new class creates
a new type of object, allowing new instances of that type to be made.

Information about an object’s class is contained in __class__.
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

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

print(Duck.__class__)
print(duckling.__class__)
print(duckling.sex.__class__)
print(duckling.quack.__class__)