"""
A class expresses an idea; it’s a blueprint or recipe for an instance. The
class is something virtual, it can contain lots of different details, and there
is always one class of any given type. Think of a class as a building blueprint
that represents the architect’s ideas, and class instances as the actual
buildings.

Classes describe attributes and functionalities together to represent an idea
as accurately as possible.

You can build a class from scratch or, something that is more interesting and
useful, employ inheritance to get a more specialized class based on another
class.

Additionally, your classes could be used as superclasses for newly derived
classes (subclasses).

If you run the code, there are no visible effects. The class has been defined,
but there is no code making use of it — that’s why you see no effects.
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