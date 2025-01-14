"""
We can create a decorator with arguments. Let’s create a program in which the
decorator will be more generic – we’ll allow you to pass the packing material
in the argument.

See the code presented

The warehouse_decorator() function created in this way has become much more
flexible and universal than 'simple_decorator', because it can handle different
materials.

Note that our decorator is enriched with one more function to make it able to
handle arguments at all call levels.

The pack_books function will be executed as follows:
- the warehouse_decorator('kraft') function will return the wrapper function;
- the returned wrapper function will take the function it is supposed to
decorate as an argument;
- the wrapper function will return the internal_wrapper function, which adds
new functionality (material display) and runs the decorated function.

The biggest advantage of decorators is now clearly visible:
- we don’t have to change every 'pack' function to display the material
being used;
- we just have to add a simple one liner in front of each function definition.
"""

def warehouse_decorator(material):
    def wrapper(own_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(
                own_function.__name__, material))
            own_function(*args)
            print()
        return internal_wrapper
    return wrapper

@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)

@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)

pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')