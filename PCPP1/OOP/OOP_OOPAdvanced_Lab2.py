"""
Objectives
improving the student's skills in operating with special methods

Scenario
- Extend the class implementation prepared in the previous lab to support the
addition and subtraction of integers to time interval objects;
- to add an integer to a time interval object means to add seconds;
- to subtract an integer from a time interval object means to remove seconds.

Hint
in the case when a special method receives an integer type argument, instead of
a time interval object, create a new time interval object based on the integer
value.

Test data:
the time interval (tti) is hours=21, minutes=58, seconds=50
the expected result of addition (tti + 62) is 21:59:52
the expected result of subtraction (tti - 62) is 21:57:48
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
        if isinstance(other, TimeInterval):
            another = other.hours * 3600 + other.minutes * 60 + other.seconds
        elif isinstance(other, int):
            another = other

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
        if isinstance(other, TimeInterval) or isinstance(other, int):
            return self.__add_sub(other, 'addition')
        else:
            raise TypeError('can only add TimeInterval objects')

    def __sub__(self, other):
        if isinstance(other, TimeInterval) or isinstance(other, int):
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

assert str(t1 + 62) == '21:59:52'
assert str(t1 - 62) == '21:57:48'

print('It works like a charm')