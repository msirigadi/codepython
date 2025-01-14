"""
An attribute is a capacious term that can refer to two major kinds of class
traits:

variables, containing information about the class itself or a class instance;
classes and class instances can own many variables;
methods, formulated as Python functions; they represent a behavior that could
be applied to the object.
Each Python object has its own individual set of attributes. We can extend that
set by adding new attributes to existing objects, change (reassign) them or
control access to those attributes.

It is said that methods are the 'callable attributes' of Python objects. By
'callable' we should understand anything that can be called; such objects allow
you to use round parentheses () and eventually pass some parameters, just like
functions.

This is a very important fact to remember: methods are called on behalf of an
object and are usually executed on object data.

Class attributes are most often addressed with 'dot' notation, i.e.,
<class>dot<attribute>. The other way to access attributes (variables) it to use
the getattr() and setattr() functions.

In our 'duckish' example, there are the following attributes:

variables: self.height, self.weight, self.sex — containing different values for
each object;
methods: __init__, walk, quack — common to all objects so far.
Examples:
To call a method, issue: drake.quack();
To access an attribute, issue: print(duckling.height).
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

drake.quack()
print(duckling.height)