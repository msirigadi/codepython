"""
A decorator is one of the design patterns that describes the structure of
related objects. Python is able to decorate functions, methods, and classes.

The decorator's operation is based on wrapping the original function with a new
"decorating" function (or class), hence the name "decoration". This is done by
passing the original function (i.e., the decorated function) as a parameter to
the decorating function so that the decorating function can call the passed
function. The decorating function returns a function that can be called later.

Of course, the decorating function does more, because it can take the
parameters of the decorated function and perform additional actions and that
make it a real decorating function.

The same principle is applied when we decorate classes

decorated = simple_decorator(simple_hello)
decorated()
"""

def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

@simple_decorator
def simple_hello():
    print("Hello from simple function")

# These lines can be replace by a decorator @simple_decorator
#decorated_function = simple_decorator(simple_hello)
#decorated_function()

simple_hello()