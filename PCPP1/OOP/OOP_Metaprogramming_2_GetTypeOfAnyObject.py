"""
In Python's approach, everything is an object, and every object has some type
associated with it. To get the type of any object, make use of the type()
function.

We can see that objects in Python are defined by their inherent classes.

The example also shows that we can create our own classes, and those classes
will be instances of the type special class, which is the default metaclass
responsible for creating classes.

These observations lead us to the following conclusions:
- metaclasses are used to create classes;
- classes are used to create objects;
- the type of the metaclass type is type – no, that is not a typo.

metaclass
    |
class
    |
class object

To extend the above observations, it’s important to add:
- type is a class that generates classes defined by a programmer;
- metaclasses are subclasses of the type class.
"""

class Dog:
    pass

age = 10
codes = [33, 92]
dog = Dog()

print(type(age))
print(type(codes))
print(type(dog))
print(type(Dog))

print()

for t in (int, list, type):
    print(type(t))