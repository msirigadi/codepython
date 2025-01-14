"""
Two special parameters are responsible for handling any number of additional
arguments (placed next after the expected arguments) passed to a called
function:

*args – refers to a tuple of all additional, not explicitly expected positional
arguments, so arguments passed without keywords and passed next after the
expected arguments. In other words, *args collects all unmatched positional
arguments;

**kwargs (keyword arguments) – refers to a dictionary of all unexpected
arguments that were passed in the form of keyword=value pairs. Likewise,
**kwargs collects all unmatched keyword arguments.

In Python, asterisks are used to denote that args and kwargs parameters are not
ordinary parameters and should be unpacked, as they carry multiple items.
"""

def combiner(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))


combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')