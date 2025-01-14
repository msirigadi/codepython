"""
- inheritance and composition are not mutually exclusive. Real-life problems are
hardly every pure “is a” or “has a” cases;
- treat both inheritance and composition as supplementary means for
solving problems;
- there is nothing wrong with composing objects of ... classes that were built
using inheritance. The next example code should shed some light on this case.

"""

class BaseComputer:
    def __init__(self, serial_number):
        self.serial_number = serial_number

class PersonalComputer(BaseComputer):
    def __init__(self, sn, connection):
        super().__init__(sn)
        self.connection = connection
        print('The computer costs $1000')

class Connection:
    def __init__(self, speed):
        self.speed = speed

    def download(self):
        print('Downloading at {}'.format(self.speed))

class DialUp(Connection):
    def __init__(self):
        super().__init__('9600bit/s')

    def download(self):
        print('Dialing the access number ... '.ljust(40), end='')
        super().download()

class ADSL(Connection):
    def __init__(self):
        super().__init__('2Mbit/s')

    def download(self):
        print('Waking up modem ... '.ljust(40), end='')
        super().download()

class Ethernet(Connection):
    def __init__(self):
        super().__init__('10Mbit/s')

    def download(self):
        print('Constantly connected .... '.ljust(40), end='')
        super().download()

# I started my IT adventure with an old-school dial up connection
my_computer = PersonalComputer('1995', DialUp())
my_computer.connection.download()

# then in the year 1999 I got ADSL
my_computer.connection = ADSL()
my_computer.connection.download()

# finally I upgraded to Ethernet
my_computer.connection = Ethernet()
my_computer.connection.download()
