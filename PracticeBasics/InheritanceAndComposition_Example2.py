"""
Look at the code presented in the editor pane.

There is a “Base_Computer” class that represents a generic computer. A generic computer has only a serial number;
there is a “Personal_Computer” class that is built upon the “Base_Computer” class and represents a computer that is able to connect to the internet;
there is a generic “Connection” class that holds information about the connection speed and handles the download() method. This class is independent of any computer class;
there are the “Connection” subclasses, more specialized than the “Connection” class:
“Dialup”
“ADSL”
“Ethernet”
* When we start with our personal computer, we set the serial number to 1995 and equip it with a dialup connection. This an example of composition.

It is possible to download some data using a slow dialup connection;
later, we equip our personal computer with a more advanced connection device. There is no need to recreate the computer object – we just arm it with a new component;
the last steps are about arming our old computer with a fast connection and downloading some data.
When you run the code, you should see the following:

The computer costs $1000
Dialling the access number ...          Downloading at 9600bit/s
Waking up modem  ...                    Downloading at 2Mbit/s
Constantly connected...                 Downloading at 10Mbit/s

"""

class Base_Computer:
    def __init__(self, serial_number):
        self.serial_number = serial_number


class Personal_Computer(Base_Computer):
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
        print('Dialling the access number ... '.ljust(40), end='')
        super().download()


class ADSL(Connection):
    def __init__(self):
        super().__init__('2Mbit/s')

    def download(self):
        print('Waking up modem  ... '.ljust(40), end='')
        super().download()


class Ethernet(Connection):
    def __init__(self):
        super().__init__('10Mbit/s')

    def download(self):
        print('Constantly connected... '.ljust(40), end='')
        super().download()

# I started my IT adventure with an old-school dial up connection
my_computer = Personal_Computer('1995', DialUp())
my_computer.connection.download()

# then in the year 1999 I got ADSL
my_computer.connection = ADSL()
my_computer.connection.download()

# finally I upgraded to Ethernet
my_computer.connection = Ethernet()
my_computer.connection.download()
