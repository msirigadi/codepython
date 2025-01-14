"""
decorators can accept arguments

When you pass arguments to the decorator, the decorator mechanism behaves quite
differently than presented in example of decorator that does not accept
arguments (previous slide):

- the reference to function to be decorated is passed to __call__ method which
is called only once during decoration process,
- the decorator arguments are passed to __init__ method
"""

class WarehouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(
                own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()
        return internal_wrapper

@WarehouseDecorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)

@WarehouseDecorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("We'll pack books:", args)

pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')