"""
Class decorators strongly refer to function decorators, because they use the
same syntax and implement the same concepts.

Instead of wrapping individual methods with function decorators, class
decorators are ways to manage classes or wrap special method calls into
additional logic that manages or extends instances that are created.

If we consider syntax, class decorators appear just before the 'class'
instructions that begin the class definition (similar to function decorators,
they appear just before the function definitions).

The simplest use can be presented as follows:

@my_decorator
class MyClass:

obj = MyClass()

Like function decorators, the new (decorated) class is available under the name
'MyClass' and is used to create an instance. The original class named 'MyClass'
is no longer available in your name space. The callable object returned by the
class decorator creates and returns a new instance of the original class,
extended in some way.
"""

def object_counter(class_):
    class_.__getattr__orig = class_.__getattribute__

    def new_getattr(self, name):
        if name == 'mileage':
            print('We noticed that the mileage attribute was read')
        return class_.__getattr__orig(self, name)

    class_.__getattribute__ = new_getattr
    return class_

@object_counter
class Car:
    name="Mahi"
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car('ABC123')
print('The mileage is', car.mileage)
print('The VIN is', car.VIN)