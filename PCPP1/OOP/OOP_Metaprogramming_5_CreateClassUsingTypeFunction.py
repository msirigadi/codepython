"""
When the type() function is called with three arguments, then it dynamically
creates a new class.

For the invocation of type(, , ):

- the argument specifies the class name; this value becomes the __name__
attribute of the class;
- the argument specifies a tuple of the base classes from which the newly
created class is inherited; this argument becomes the __bases__ attribute of
the class;
- the argument specifies a dictionary containing method definitions and
variables for the class body; the elements of this argument become the __dict__
attribute of the class and state the class namespace.

As a result, we have created the simple class “Dog”.
"""

Dog = type('Dog', (), {})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class atrributes are:', Dog.__dict__)