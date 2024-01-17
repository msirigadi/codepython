class Timer:
    def __init__(self, hrs=0, mins=0, secs=0):
        #
        # Write code here
        #
        self.__hrs = hrs
        self.__mins = mins
        self.__secs = secs

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
        if self.__secs == 60:
            self.__secs = 0
            self.__mins += 1
            if self.__mins == 60:
                self.__mins = 0
                self.__hrs += 1
                if self.__hrs == 24:
                    self.__hrs = 0

    def prev_second(self):
        #
        # Write code here
        #

        self.__secs -= 1
        if self.__secs == -1:
            self.__secs = 59
            self.__mins -= 1
            if self.__mins == -1:
                self.__mins = 59
                self.__hrs -= 1
                if self.__hrs == -1:
                    self.__hrs = 23


def format_string(hrs, mins, secs):
    strg = ""

    if hrs < 10:
        hours = ("0" + str(hrs))
    else:
        hours = str(hrs)

    if mins < 10:
        minutes = ("0" + str(mins))
    else:
        minutes = str(mins)

    if secs < 10:
        seconds = ("0" + str(secs))
    else:
        seconds = str(secs)

    strg = strg + hours + ":" + minutes + ":" + seconds
    return strg


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)