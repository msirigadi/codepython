"""
Composition is the process of composing an object using other different
objects. The objects used in the composition deliver a set of desired traits
(properties and/or methods) so we can say that they act like blocks used to
build a more complicated structure.

It can be said that:
- inheritance extends a class's capabilities by adding new components and
modifying existing ones; in other words, the complete recipe is contained
inside the class itself and all its ancestors; the object takes all the class's
belongings and makes use of them;
- composition projects a class as a container (called a composite) able to
store and use other objects (derived from other classes) where each of the
objects implements a part of a desired class's behavior. It’s worth mentioning
that blocks are loosely coupled with the composite, and those blocks could be
exchanged any time, even during program runtime.

The “Car” class is loosely coupled with the “engine” component. It’s a
composite object.

The main advantages are:
- whenever a change is applied to the engine object, it does not influence the
“Car” class object structure;
- you can decide what your car should be equipped with.

Our “Car” could be equipped with two different kinds of engine – a gas one or a
diesel one. The developer's responsibility is to provide methods for both
engine classes, named in the same way (here is the start() method) to make it
work in a polymorphic manner.
"""

class Car:
    def __init__(self, engine):
        self.engine = engine

class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))


class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))


my_car = Car(GasEngine(4))
my_car.engine.start()
my_car.engine = DieselEngine(2)
my_car.engine.start()
