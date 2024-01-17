"""
Objectives
improving the student's skills in operating with special methods
Scenario
Create a class representing a time interval;
the class should implement its own method for addition, subtraction on time interval class objects;
the class should implement its own method for multiplication of time interval class objects by an integer-type value;
the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
check the argument type, and in case of a mismatch, raise a TypeError exception.

Hint #1
just before doing the math, convert each time interval to a corresponding number of seconds to simplify the algorithm;
for addition and subtraction, you can use one internal method, as subtraction is just ... negative addition.
Test data:

the first time interval (fti) is hours=21, minutes=58, seconds=50
the second time interval (sti) is hours=1, minutes=45, seconds=22
the expected result of addition (fti + sti) is 23:44:12
the expected result of subtraction (fti - sti) is 20:13:28
the expected result of multiplication (fti * 2) is 43:57:40

Hint #2
you can use the assert statement to validate if the output of the __str__ method applied to a time interval object equals the expected value.
"""


class Timeinterval:
    def __init__(self, hrs, mins, secs):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs

    def __str__(self):
        return "{}:{}:{}".format(self.hrs, self.mins, self.secs)

    def __add__(self, other):
        secs = self.secs + other.secs
        if secs >= 60:
            secs = secs % 60
            mins = self.mins + other.mins + 1
            if mins >= 60:
                mins = mins % 60
                hrs = self.hrs + other.hrs + 1
                if hrs >= 24:
                    hrs = hrs % 24

        return Timeinterval(hrs, mins, secs)

    def __sub__(self, other):
        secs = self.secs - other.secs
        if secs <= 0:
            secs = abs(secs) % 60
            mins = self.mins - other.mins
            if mins <= 0:
                mins = abs(mins) % 60
                hrs = self.hrs - other.hrs
                if hrs <= 0:
                    hrs = abs(hrs) % 24

        return Timeinterval(hrs, mins, secs)

    def __mul__(self, val):
        secs = self.secs * 2
        mins = self.mins * 2
        hrs = self.hrs * 2

        while secs >= 60:
            secs = secs % 60
            mins += 1

        while mins >= 60:
            mins = mins % 60
            hrs += 1

        return Timeinterval(hrs, mins, secs)
        # return Timeinterval(self.hrs * val, self.mins * val, self.secs * val)


t1 = Timeinterval(21, 58, 50)
t2 = Timeinterval(1, 45, 22)
print(t1)
print(t2)
print(t1 + t2)
print(t2 - t1)
print(t1 * 2)