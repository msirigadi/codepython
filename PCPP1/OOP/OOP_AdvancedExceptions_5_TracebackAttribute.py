"""
Each exception object owns a __traceback__ attribute.

Python allows us to operate on the traceback details because each exception
object (not only chained ones) owns a __traceback__ attribute.

Let's examine such an object while we’re preparing our rocket to launch.

Final check procedure
        The captain's name is John
        The pilot's name is Mary
        The mechanic's name is Mike
<traceback object at 0x00753300>
<class 'traceback'>

From the output presented on the previous page, we can conclude that we have to
deal with a traceback type object.

To achieve this, we could use the format_tb() method delivered by the built-in
traceback module to get a list of strings describing the traceback.

We could use the print_tb() method, also delivered by the traceback module, to
print strings directly to the standard output.

The corresponding output reveals the sequence of exceptions and proves that the
execution was not interrupted by the exceptions because we see the final
wording Final check is over.
"""

import traceback

class RocketNotReadyError(Exception):
    pass

def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))
    print('\nTraceback details')
    details = traceback.format_tb(f.__traceback__)
    print("\n".join(details))

print('Final check is over')
