"""
When you want to forward arguments received by your very smart and universal
function (defined with *args and **kwargs, of course) to another handy and
smart function, you should do that in the following way:

If we remove the asterisks from the function call, then both tuple and
dictionary would be captured by my_args, as it is supposed to handle all
positional arguments (none of them is keyworded).
"""

def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)

def super_combiner(*my_args, **my_kwargs):
    print(my_args)
    print(my_kwargs)

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')