"""
We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.
Use the following hints:

all object's properties should be private;
consider writing a separate function (not method!) to format the time string.
Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.

Expected output
23:59:59
00:00:00
23:59:59
"""


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        #
        # Write code here
        #
        self.__hrs = hours
        self.__mins = minutes
        self.__secs = seconds

    def __str__(self):
        #
        # Write code here
        #
        return format_string(self.__hrs, self.__mins, self.__secs)

    def next_second(self):
        #
        # Write code here
        #
        self.__secs += 1
        if self.__secs > 59:
            self.__secs = 0
            self.__mins += 1
            if self.__mins > 59:
                self.__mins = 0
                self.__hrs += 1
                if self.__hrs > 23:
                    self.__hrs = 0
        else:
            self._secs += 1

    def prev_second(self):
        #
        # Write code here
        #
        self.__secs -= 1
        if self.__secs < 0:
            self.__secs = 59
            self.__mins -= 1
            if self.__mins < 0:
                self.__mins = 59
                self.__hrs -= 1
                if self.__hrs < 0:
                    self.__hrs = 23
        else:
            self._secs += 1


def format_string(hrs, mins, secs):
    time_str = ""
    if hrs < 10:
        hrs = '0' + str(hrs)
    else:
        hrs = str(hrs)

    if mins < 10:
        mins = '0' + str(mins)
    else:
        mins = str(mins)

    if secs < 10:
        secs = '0' + str(secs)
    else:
        secs = str(secs)

    time_str += (hrs + ':' + mins + ':' + secs)
    return time_str


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
