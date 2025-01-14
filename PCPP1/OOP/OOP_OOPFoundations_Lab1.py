"""
Objectives
- creating classes, methods, and variables;
- calling methods;
- getting simple access to instance variables;

Scenario
- create a class representing a mobile phone;
- your class should implement the following methods:
    __init__ expects a number to be passed as an argument; this method
        stores the number in an instance variable self.number
    turn_on() should return the message 'mobile phone {number} is turned
        on'. Curly brackets are used to mark the place to insert the object's
        number variable;
    turn_off() should return the message 'mobile phone is turned off';
    call(number) should return the message 'calling {number}'. Curly brackets
        are used to mark the place to insert the object's number variable;

create two objects representing two different mobile phones; assign any random
phone numbers to them;
implement a sequence of method calls on the objects to turn them on, call any
number. Print the methods' outcomes;
turn off both mobiles.

Example output

mobile phone 01632-960004 is turned on
mobile phone 01632-960012 is turned on
calling 555-34343
mobile phone is turned off
mobile phone is turned off
"""

class MobilePhone:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return "mobile phone {} is turned on".format(self.number)

    def turn_off(self):
        return "mobile phone is turned off"

    def call(self, number):
        return "calling {}".format(number)

mp_1 = MobilePhone('233-481-2356')
mp_2 = MobilePhone('850-323-9340')

print(mp_1.turn_on())
print(mp_2.turn_on())
print(mp_1.call('234-5456-1288'))
print(mp_1.turn_off())
print(mp_2.turn_off())

