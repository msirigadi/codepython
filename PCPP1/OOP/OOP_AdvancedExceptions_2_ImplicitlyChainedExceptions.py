"""
Imagine a situation where you are already handling an exception and your code
incidentally triggers an additional exception. Should your code lose the
information about the previous exception? Of course not. So the information
should be available to the code following the erroneous code. This is an
example of implicit chaining.

Another case pops up when we knowingly wish to handle an exception and
translate it to another type of exception. Such a situation is typical when you
have a good reason for the unifying behavior of one piece of code to act
similarly to another piece of code, like a legacy code. In this situation it
would also be nice to keep the details of the former exception. This is an
example of explicit chaining.

This chaining concept introduces two attributes of exception instances:
- the __context__ attribute, which is inherent for implicitly chained exceptions;
- the __cause__ attribute, which is inherent for explicitly chained exceptions.

Those attributes help the programmer to keep a reference to the original
exception object in a handy and consistent way for later processing like
logging, etc.

a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    print(0 / 0)

Traceback (most recent call last):
  File "exceptions#030.py", line 6, in <module>
    print(a_list[3])
IndexError: list index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "exceptions#030.py", line 8, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero
"""

a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print
        # progress as 1/10	but wrote 1/0
        print(0/0)
    except ZeroDivisionError as f:
        print('Inner exception (f):', f)
        print('Outer exception (e):', e)
        print('Outer exception referenced:', f.__context__)
        print('Is it the same object:', f.__context__ is e)
