"""
Class variables are defined within the class construction, so these variables
are available before any class instance is created. To get access to a class
variable, simply access it using the class name, and then provide the
variable name.

Similarly to instance variables, class variables are shown in the
's __dict__ dictionary.
"""

class Demo:
    class_var = 'shared variable'

print(Demo.class_var)
print(Demo.__dict__)