"""
Class methods are methods that, like class variables, work on the class itself,
and not on the class objects that are instantiated. You can say that they are
methods bound to the class, not to the object.

When can this be useful?

There are several possibilities, here are the two most popular:

- we control access to class variables, e.g., to a class variable containing
information about the number of created instances or the serial number given
to the last produced object, or we modify the state of the class variables;
- we need to create a class instance in an alternative way, so the class method
can be implemented by an alternative constructor.

Convention
- To be able to distinguish a class method from an instance method, the
programmer signals it with the @classmethod decorator preceding the class
method definition.
- Additionally, the first parameter of the class method is cls, which is used
to refer to the class methods and class attributes.
"""

class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter += 1

    @classmethod
    def get_internal(cls):
        return 'No of objects created: {}'.format(cls.__internal_counter)

print(Example.get_internal())
example1 = Example(10)
print(Example.get_internal())
example2 = Example(20)
print(Example.get_internal())