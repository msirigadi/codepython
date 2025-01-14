"""
Inheritance is one of the fundamental concepts of object oriented programming,
and expresses the fundamental relationships between classes: superclasses
(parents) and their subclasses (descendants). Inheritance creates a class
hierarchy. Any object bound to a specific level of class hierarchy inherits all
the traits (methods and attributes) defined inside any of the superclasses.

This means that inheritance is a way of building a new class, not from scratch,
but by using an already defined repertoire of traits. The new class inherits
(and this is the key) all the already existing equipment, but is able to add
some new features if needed.

Each subclass is more specialized (or more specific) than its superclass.
Conversely, each superclass is more general (more abstract) than any of its
subclasses. Note that we've presumed that a class may only have one
superclass — this is not always true, but we'll discuss this issue more a
bit later.
"""

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass


v = Vehicle()
lv = LandVehicle()
tv = TrackedVehicle()
