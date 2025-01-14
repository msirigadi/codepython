"""
When you want to set or change a value of the class variable, you should access
it via the class, but not the class instance, as you can do for reading.

When you try to set a value for the class variable using the object (a variable
referring to the object or self keyword) but not the class, you are creating an
instance variable that holds the same name as the class variable.
"""

class Demo:
    class_var = 'shared variable'

d1 = Demo()
d2 = Demo()

# both instances allow access to the class variable
print(d1.class_var)
print(d2.class_var)
print('.' * 20)

# d1 object has no instance variable
print('contents of d1:', d1.__dict__)
print('.' * 20)

# d1 object receives an instance variable named 'class_var'
d1.class_var = "I'm messing with the class variable"

# d1 object owns the variable named 'class_var' which holds a different value
# than the class variable
print('contents of d1:', d1.__dict__)
print(d1.class_var)
print('.' * 20)

# d2 object variables were not influenced
print(d2.__dict__)

# d2 class variables were not influenced
print('contents of class variables accessed via d2:', d2.class_var)