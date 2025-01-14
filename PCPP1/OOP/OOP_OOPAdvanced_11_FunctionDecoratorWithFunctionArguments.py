"""
Consider a function that accepts arguments and should also be decorated.
Decorators, which should be universal, must support any function, regardless of
the number and type of arguments passed. In such a situation, we can use the
*args and **kwargs concepts. We can also employ a closure technique to
persist arguments.

The code presented in the right pane shows how the decorator can handle the
arguments of the function being decorated.

Arguments passed to the decorated function are available to the decorator, so
the decorator can print them. This is a simple example, as the arguments were
just printed, but not processed further.

A nested function (internal_wrapper) could reference an object (own_function)
in its enclosing scope thanks to the closure.
"""

def simple_decorator(own_function):
    def internal_wrapper(*args, **kwargs):
        print('{} was called with following arguments:'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper

@simple_decorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received argumens:", args, kwargs)

combiner('a', 'b', exec='yes')