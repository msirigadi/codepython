"""
Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
Apply your decorator to those functions to ensure that the time of the function executions can be monitored.

Hint
To print the current time, you could use the following code:

# import module responsible for time processing
from datetime import datetime

# get current time using now() method
timestamp = datetime.now()

# convert timestamp to human-readable string, following passed pattern:
string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

print(string_timestamp)

"""

from datetime import datetime


def timestamp_decorator(function):
    def wrapper(*args):
        timestamp = datetime.now()
        string_timestamp = timestamp.strftime('%y-%m-%d %H:%M:%S')
        print(string_timestamp)
        function(*args)

    return wrapper


@timestamp_decorator
def addition(val1, val2):
    print("Addition of {} and {} is {}".format(val1, val2, val1 + val2))


@timestamp_decorator
def multiplication(val1, val2):
    print("Multiplication of {} and {} is {}".format(val1, val2, val1 * val2))


addition(2, 3)
multiplication(2, 3)