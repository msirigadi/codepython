"""
As a class variable is present before any instance of the class is created, it
can be used to store some meta data relevant to the class, rather than to the
instances:

- fixed information like description, configuration, or identification values;
- mutable information like the number of instances created (if we add a code to
increment the value of a designated variable every time we create a class
instance)

A class variable is a class property that exists in just one copy, and it is
stored outside any class instance. Because it is owned by the class itself,
all class variables are shared by all instances of the class. They will
therefore generally have the same value for every instance; but as the class
variable is defined outside the object, it is not listed in the
object's __dict__.

Conclusion: when you want to read the class variable value, you can use a class
or class instance to access it.
"""

class Demo:
    class_var = 'shared variable'

d1 = Demo()
d2 = Demo()

print(Demo.class_var)
print(d1.class_var)
print(d2.class_var)

print("contents of d1:", d1.__dict__)
