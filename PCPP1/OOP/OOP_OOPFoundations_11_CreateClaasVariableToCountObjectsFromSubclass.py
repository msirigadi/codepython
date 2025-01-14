"""
Another example shows that a class variable of a super class can be used to
count the number of all objects created from the descendant classes
(subclasses). We'll achieve this by calling the superclass __init__ method.

Another class variable is used to keep track of the serial numbers (which in
fact are also counters) of particular subclass instances. In this example, we
are also storing instance data (phone numbers) in instance variables.

The class Phone is a class representing a blueprint of generic devices used for
calling. This class definition delivers the call method, which displays the
object’s variable, which holds the phone number. This class also holds a class
variable that is used to count the number of instances created by its
subclasses.

Subclasses make use of the superclass __init__ method, then instances are
created. This gives us the possibility to increment the superclass variable.
"""

class Phone:
    counter = 0

    def __init__(self, number):
        self.number = number
        Phone.counter += 1

    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message

class FixedPhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)

class MobilePhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)


print('Total number of phones devices created:', Phone.counter)
print('Creating 2 devices')
fphone = FixedPhone('555-2368')
mphone = MobilePhone('02378-34930')

print('Total number of phone devices created:', Phone.counter)
print('Total number of mobile phones created:', MobilePhone.last_SN)

print(fphone.call('34950-29480'))
print('Fixed phone received "{}" serial number'.format(fphone.SN))
print('Mobile phone received "{}" serial number'.format(mphone.SN))
