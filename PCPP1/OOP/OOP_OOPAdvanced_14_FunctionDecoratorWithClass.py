"""
Decorating functions with classes
A decorator does not have to be a function. In Python, it could be a class that
plays the role of a decorator as a function.

We can define a decorator as a class, and in order to do that, we have to use a
__call__ special class method. When a user needs to create an object that acts
as a function (i.e., it is callable) then the function decorator needs to
return an object that is callable, so the __call__ special method will be
very useful.

"""

class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('{} was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorating is still operating')

@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')