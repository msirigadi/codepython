"""
The code presented in the editor shows how to use the class method as an
alternative constructor, allowing you to handle an additional argument.

The including_brand method is a class method, and expects a call with two
parameters ('vin' and 'brand'). The first parameter is used to create an object
using the standard __init__ method.

In accordance with the convention, the creation of a class object (i.e.,
calling the __init__ method, among other things) is done using cls(vin).

Then the class method performs an additional task – in this case, it
supplements the brand instance variable and finally returns the newly
created object.
"""

class Car:
    def __init__(self, vin):
        print("Ordinary __init__ was called for", vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):
        print('Class method was called')
        _car = cls(vin)
        _car.brand = brand
        return _car

car1 = Car('ABCD1234')
car2 = Car.including_brand('DEF567', 'NewBrand')

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)