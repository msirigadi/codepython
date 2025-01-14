"""
Encapsulation is used to hide the attributes inside a class like in a capsule,
preventing unauthorized parties' direct access to them. Publicly accessible
methods are provided in the class to access the values, and other objects call
those methods to retrieve and modify the values within the object. This can be
a way to enforce a certain amount of privacy for the attributes.

Python introduces the concept of properties that act like proxies to
encapsulated attributes.

Python allows you to control access to attributes with the built-in property()
function and corresponding decorator @property.

This decorator plays a very important role:
- it designates a method which will be called automatically when another object
wants to read the encapsulated attribute value;
- the name of the designated method will be used as the name of the instance
attribute corresponding to the encapsulated attribute;
- it should be defined before the method responsible for setting the value of the
encapsulated attribute, and before the method responsible for deleting the
encapsulated attribute.

As those attribute name repetitions could be misleading, let's explain the
naming convention:
- the getter method is decorated with '@property'. It designates the name of
the attribute to be used by the external code;
- the setter method is decorated with '@name.setter'. The method name should be
the attribute name;
- the deleter method is decorated with '@name.deleter'. The method name should
should be the attribute name.
"""

class TankError(Exception):
    pass

class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, amount):
        if amount > 0:
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError('Too much liquid in the tank')
        else:
            raise TankError('Not possible to set negative liquid level')

    @level.deleter
    def level(self):
        if self.__level > 0:
            print('It is good to remember to sanitize the remains from the '
                  'tank')
        self.__level = None

# Our tank object has the capacity of 20 units
our_tank = Tank(20)

# Our tank's current liquid level is set to 10 units
our_tank.level = 10
print('Current liquid level:', our_tank.level)

# adding additional 3 units (setting liquid level to 13)
our_tank.level += 3
print('Current liquid level:', our_tank.level)

# let's try to set the current liquid level to 21
# this should be rejected as the tank's capacity is 20 units
try:
    our_tank.level = 21
except TankError as e:
    print('Trying to set liquid level to 21 units, result:', e)

# similar example - let's try to add an additional 15 units
# this should be rejected as the total capacity is 20 units
try:
    our_tank.level += 15
except TankError as e:
    print('Trying to add an additional 15 units, result:', e)

# let's try to set the liquid level to a negative amount
# this should be rejected as it is senseless
try:
    our_tank.level = -3
except TankError as e:
    print('Trying to set liquid level to -3 units, result:', e)

print('Current liquid level:', our_tank.level)

del our_tank.level