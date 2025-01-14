"""
Objectives
improving the student's skills in operating with inheritance and composition

Scenario
Imagine that you are an automotive fan, and you are able to build a car from a
limited set of components.

Your task is to :
- define classes representing:
        - tires (as a bundle needed by a car to operate); methods available:
        get_pressure(), pump(); attribute available: size
        - engine; methods available: start(), stop(), get_state(); attribute
        available: fuel type
        - vehicle; method available: __init__(VIN, engine, tires); attribute
        available: VIN

- based on the classes defined above, create the following objects:
    - two sets of tires: city tires (size: 15), off-road tires (size: 18)
    - two engines: electric engine, petrol engine
- instantiate two objects representing cars:
    - the first one is a city car, built of an electric engine and city tires
    - the second one is an all-terrain car build of a petrol engine and
    off-road tires
- play with the cars by calling methods responsible for interaction with
components.
"""

class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0
    def get_pressure(self):
        return self.pressure

    def pump(self, psi):
        self.pressure = psi

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = 'off'
    def start(self):
        self.state = 'on'

    def stop(self):
        self.state = 'off'

    def get_state(self):
        return self.state

class Car:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

city_tires = Tires(15)
off_road_tires = Tires(18)

electric_engine = Engine('electric')
petrol_engine = Engine('Petrol')

city_car = Car('111A', electric_engine, city_tires)
all_terrain_car = Car('124B', petrol_engine, off_road_tires)

# prepare all_terrain_car for a rally
print('All-terrain car engine is', all_terrain_car.engine.get_state())
all_terrain_car.tires.pump(10)
all_terrain_car.engine.start()
print('All-terrain car engine is', all_terrain_car.engine.get_state())

# prepare city car for a shopping
print('City car engine is', city_car.engine.get_state())
city_car.tires.pump(3)
city_car.engine.start()
print('City car engine is', city_car.engine.get_state())
city_car.engine.stop()
print('City car engine is', city_car.engine.get_state())
