"""
The except clause may specify a variable after the exception name.
In this example it’s an e_variable. This variable is bound to an exception
instance with the arguments stored in the args attribute of the
e_variable object.

try:
    print(int('a'))
except ValueError as e_variable:
    print(e_variable.args)

Some exception objects carry additional information about the exception itself.

The ImportError exception – raised when the import statement has trouble trying
to load a module. The attributes are:

name – represents the name of the module that was attempted to be imported;
path – represents the path to any file which triggered the exception,
respectively. Could be None.


The UnicodeError exception – raised when a Unicode-related encoding or decoding
error occurs. It is a subclass of ValueError.

The UnicodeError has attributes that describe an encoding or decoding error.

encoding – the name of the encoding that raised the error.
reason – a string describing the specific codec error.
object – the object the codec was attempting to encode or decode.
start – the first index of invalid data in the object.
end – the index after the last invalid data in the object.
See the output of this snippet to analyze the attributes' values.
"""

try:
    import abcdefghi
except ImportError as e:
    print(e.args)
    print(e.name)
    print(e.path)


try:
    b'\x80'.decode('utf-8')
except UnicodeError as e:
    print(e)
    print(e.encoding)
    print(e.reason)
    print(e.object)
    print(e.start)
    print(e.end)