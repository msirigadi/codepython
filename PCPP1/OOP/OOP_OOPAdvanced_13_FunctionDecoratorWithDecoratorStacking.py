"""
Python allows you to apply multiple decorators to a callable object (function,
method or class).

The most important thing to remember is the order in which the decorators are
listed in your code, because it determines the order of the executed
decorators. When your function is decorated with multiple decorators:

@outer_decorator
@inner_decorator
def function():
    pass

abcd = subject_matter_function()


the call sequence will look like the following:
- the outer_decorator is called to call the inner_decorator, then the
inner_decorator calls your function;
- when your function ends it execution, the inner_decorator takes over control,
and after it finishes its execution, the outer_decorator is able to finish
its job.

This routing mimics the classic stack concept.
"""

def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> The whole order would be packed with', collective_material)
            print()
        return internal_wrapper
    return wrapper

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
        return internal_wrapper
    return wrapper

@big_container('plain cardboard')
@warehouse_decorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)

@big_container('colourful cardboard')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
