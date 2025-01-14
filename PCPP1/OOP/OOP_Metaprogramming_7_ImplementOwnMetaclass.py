"""
The way of creating classes, using the type function, is substantial for
Python's way of creating classes using the class instruction:

- after the class instruction has been identified and the class body has been
executed, the class = type(, , ) code is executed;
- the type is responsible for calling the __call__ method upon class instance
creation; this method calls two other methods:
- __new__(), responsible for creating the class instance in the computer
memory; this method is run before __init__();
- __init__(), responsible for object initialization.

Metaclasses usually implement these two methods (__init__, __new__), taking
control of the procedure of creating and initializing a new class instance.
Classes receive a new layer of logic.

It’s important to remember that metaclasses are classes that are instantiated
to get classes.

The first step is to define a metaclass that derives from the type type and
arms the class with a 'custom_attribute'

Pay attention to the fact that:

* the class My_Meta is derived from type. This makes our class a metaclass;
* our own __new__ method has been defined. Its role is to call the __new__
method of the parent class to create a new class;
* __new__ uses 'mcs' to refer to the class – it’s just a convention;
* a class attribute is created additionally;
* the class is returned.

Pay attention to the fact that:

* a new class has been defined in a way where a custom metaclass is listed in
the class definition as a metaclass. This is a way to tell Python to use
My_Meta as a metaclass, not as an ordinary superclass;
* we are printing the contents of the class __dict__ attribute to check if the
custom attribute is present.
"""

class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'
        return obj

class My_Object(metaclass=My_Meta):
    pass

print(My_Object.__dict__)