"""
Special attributes:

* __name__ – inherent for classes; contains the name of the class;
* __class__ – inherent for both classes and instances; contains information
about the class to which a class instance belongs;
* __bases__ – inherent for classes; it’s a tuple and contains information about
the base classes of a class;
* __dict__ – inherent for both classes and instances; contains a dictionary
(or other type mapping object) of the object's attributes.
"""

class Dog:
    pass

dog = Dog()

print('"dog" is an object of class named:', Dog.__name__)
print()
print('class "Dog" is an instance of:', Dog.__class__)
print('instance "dog" is an instance of:', dog.__class__)
print()
print('class "Dog" is ', Dog.__bases__)
print()
print('class "Dog" attributes:', Dog.__dict__)
print('instance "dog" attributed:', dog.__dict__)