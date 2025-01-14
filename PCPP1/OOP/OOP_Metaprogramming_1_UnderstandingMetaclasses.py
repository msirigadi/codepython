"""
Metaprogramming is a programming technique in which computer programs have the
ability to modify their own or other programs’ codes

Example of metaprogramming is the metaclass concept

In Python, a metaclass is a class whose instances are classes. Just as an
ordinary class defines the behavior of certain objects, a metaclass allows for
the customization of class instantiation.

The functionality of the metaclass partly coincides with that of class
decorators, but metaclasses act in a different way than decorators:

- decorators bind the names of decorated functions or classes to new callable
objects. Class decorators are applied when classes are instantiated;
- metaclasses redirect class instantiations to dedicated logic, contained in
metaclasses. Metaclasses are applied when class definitions are read to create
classes, well before classes are instantiated.

Metaclasses usually enter the game when we program advanced modules or
frameworks, where a lot of precise automation must be provided.

The typical use cases for metaclasses:
- logging;
- registering classes at creation time;
- interface checking;
- automatically adding new methods;
- automatically adding new variables.


Metaclasses are the 'stuff' that creates classes.

You define classes in order to create objects, right?

But we learned that Python classes are objects.

Well, metaclasses are what create these objects. They are the classes' classes,
you can picture them this way:

MyClass = MetaClass()
my_object = MyClass()
"""

class Dog:
    pass

print(type(Dog))