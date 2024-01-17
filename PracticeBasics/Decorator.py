"""
Create a function decorator that prints a timestamp (in a form like
year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)

Create a few ordinary functions that do some simple tasks, like adding or
multiplying two numbers.
Apply your decorator to those functions to ensure that the time of the
function executions can be monitored.
"""


def number_decorator(number_function):
    import datetime

    def wrapper(*args):
        now = datetime.datetime.now()
        print(now)

        print("Calling func {} with args {}".format(number_function.__name__, args))
        return number_function(*args)

    return wrapper


@number_decorator
def mul_numbers(*args):
    print("Multipying two numbers")
    prod = 1
    for elem in args:
        prod *= elem

    return prod


@number_decorator
def add_numbers(*args):
    print("Adding two numbers")
    sum = 0
    for elem in args:
        sum += elem

    return sum


result1 = add_numbers(3, 5)
result2 = mul_numbers(3, 5)

print("Sum = ", result1)
print("Product = ", result2)