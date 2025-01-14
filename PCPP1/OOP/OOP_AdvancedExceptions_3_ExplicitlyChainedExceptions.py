"""
convert an explicit type of exception object to another type of exception
object at the moment when the second exception is occurring.

Imagine that your code is responsible for the final checking process before the
rocket is launched. The list of checks is a long one, and different checks
could result in different exceptions.

But as it is a very serious process, you should be sure that all checks are
passed. If any fails, it should be marked in the log book and re-checked
next time.

Now you see that it would be convenient to convert each type of exception into
its own exception (like RocketNotReadyError) and to log the origin of the
exception.

Final check procedure
        The captain's name is John
        The pilot's name is Mary
        The mechanic's name is Mike
Traceback (most recent call last):
  File "exceptions#050.py", line 10, in personnel_check
    print("\tThe navigator's name is", crew[3])
IndexError: list index out of range

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "exceptions#050.py", line 19, in
    personnel_check()
  File "exceptions#050.py", line 12, in personnel_check
    raise RocketNotReadyError('Crew is incomplete') from e
__main__.RocketNotReadyError: Crew is incomplete
output

Once again, the result of the code execution contains an interesting piece of
information indicating that we have just witnessed a chain of exceptions:

The above exception was the direct cause of the following exception:
"""
class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is:", crew[0])
        print("\tThe pilot's name is:", crew[1])
        print("\tThe mechanic's name is:", crew[2])
        print("\tThe navigator's name is:", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

crew = ['John', 'Mary', 'Mike']
print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print('General exception: "{}", caused by "{}"'.format(f, f.__cause__))