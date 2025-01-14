"""
Objectives
improving the student's skills in operating with special methods

Scenario
- Create a class representing a time interval;
- the class should implement its own method for addition, subtraction on time
interval class objects;
- the class should implement its own method for multiplication of time interval
class objects by an integer-type value;
- the __init__ method should be based on keywords to allow accurate and
convenient object initialization, but limit it to hours, minutes, and seconds
parameters;
- the __str__ method should return an HH:MM:SS string, where HH represents hours,
- MM represents minutes and SS represents the seconds attributes of the time
interval object;

check the argument type, and in case of a mismatch, raise a TypeError exception.

Hint #1
- just before doing the math, convert each time interval to a corresponding
number of seconds to simplify the algorithm;
- for addition and subtraction, you can use one internal method, as subtraction
is just ... negative addition.

Test data:

the first time interval (fti) is hours=21, minutes=58, seconds=50
the second time interval (sti) is hours=1, minutes=45, seconds=22
the expected result of addition (fti + sti) is 23:44:12
the expected result of subtraction (fti - sti) is 20:13:28
the expected result of multiplication (fti * 2) is 43:57:40

Hint #2
you can use the assert statement to validate if the output of the __str__
method applied to a time interval object equals the expected value.
"""

class TimeInterval:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return '{}:{}:{}'.format(self.hours, self.minutes, self.seconds)

    def __add_sub(self, other, operation):
        own = self.hours * 3600 + self.minutes * 60 + self.seconds
        another = other.hours * 3600 + other.minutes * 60 + other.seconds

        if operation == 'addition':
            new_time = own + another
        elif operation == 'subtraction':
            new_time = own - another
        else:
            raise Exception('Unknown operation')

        new_hours = new_time // 3600
        new_minutes = (new_time % 3600) // 60
        new_seconds = new_time % 60

        return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)

    def __add__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'addition')
        else:
            raise TypeError('can only add TimeInterval objects')

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'subtraction')
        else:
            raise TypeError('can only subtract TimeInterval objects')

    def __mul__(self, other):
        if isinstance(other, int):
            new_time = ((self.hours * 3600) + (self.minutes * 60) + self.seconds) * other
            new_hours = new_time // 3600
            new_minutes = (new_time % 3600) // 60
            new_seconds = new_time % 60
            return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)
        else:
            raise TypeError('can only multiply TimeInterval object by integers')

t1 = TimeInterval(hours=21, minutes=58, seconds=50)
t2 = TimeInterval(1, 45, 22)

assert str(t1 + t2) == '23:44:12'
assert str(t1 - t2) == '20:13:28'
assert str(t1 * 2) == '43:57:40'

print('It works like a charm')