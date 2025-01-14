"""
Python allows for variables to be used at the instance level or the class
level. Those used at the instance level are referred to as instance variables,
whereas variables used at the class level are referred to as class variables.

Instance variables
This kind of variable exists when and only when it is explicitly created and
added to an object. This can be done during the object's initialization,
performed by the __init__ method, or later at any moment of the object's life.
Furthermore, any existing property can be removed at any time.

Each object carries its own set of variables – they don't interfere with one
another in any way. The word instance suggests that they are closely connected
to the objects (which are class instances), not to the classes themselves. To
get access to the instance variable, you should address the variable in the
following way: objectdotvariable_name.
"""

class Demo:
    def __init__(self, value):
        self.instance_var = value

d1 = Demo(100)
d2 = Demo(200)

print("d1's instance variable is equal to:", d1.instance_var)
print("d2's instance variable is equal to:", d2.instance_var)