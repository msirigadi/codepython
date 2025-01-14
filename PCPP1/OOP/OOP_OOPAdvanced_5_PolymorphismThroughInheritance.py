"""
One way to carry out polymorphism is inheritance, when subclasses make use of
base class methods, or override them. By combining both approaches, the
programmer is given a very convenient way of creating applications, as:

- most of the code could be reused and only specific methods are implemented,
which saves a lot of development time and improves code quality;
- the code is clearly structured;
- there is a uniform way of calling methods responsible for the same
operations, implemented accordingly for the types.

Remember
You can use inheritance to create polymorphic behavior, and usually that's what
you do, but that's not what polymorphism is about.

In the right pane, there is a code implementing both inheritance and
polymorphism:

inheritance: class Radio inherits the turn_on() method from its superclass —
that is why we see The device was turned on string twice. Other subclasses
override that method and as a result we see different lines being printed;

polymorphism: all class instances allow the calling of the turn_on() method,
even when you refer to the objects using the arbitrary variable element.
"""

class Device:
    def turn_on(self):
        print('The device was turned on')

class Radio(Device):
    pass

class PortableRadio(Device):
    def turn_on(self):
        print('PortableRadio type object was turned on')

class TvSet(Device):
    def turn_on(self):
        print('TvSet type object was turned on')

device = Device()
radio = Radio()
portableRadio = PortableRadio()
tvset = TvSet()

for element in (device, radio, portableRadio, tvset):
    element.turn_on()