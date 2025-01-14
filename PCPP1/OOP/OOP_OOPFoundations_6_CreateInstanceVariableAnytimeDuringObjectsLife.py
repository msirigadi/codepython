"""
Instance variables can be created during any moment of an object's life.
Moreover, it lists the contents of each object, using the built-in __dict__
property that is present for every Python object.

This example shows that modifying the instance variable of any object has no
impact on all the remaining objects. Instance variables are completely isolated
from each other.
"""

class Demo:
    def __init__(self, value):
        self.instance_var = value


d1 = Demo(100)
d2 = Demo(200)

d1.another_var = 'another variable in the object'

print('contents of d1:', d1.__dict__)
print('contents of d2:', d2.__dict__)
