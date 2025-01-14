"""
Objectives
Learn how to:

use the json module and its basic facilities;
encode and decode JSON strings from/to Python objects.

Scenario
Take a look at these two screenshots. They present two different use cases of
the same program:


What can I do for you?
1 - produce a JSON string describing a vehicle
2 - decode a JSON string into vehicle class
Your choice: 1
Registration number: PC38927Z
Year of production: 2018
Passenger [y/n]: n
Vehicle mass: 1543.2
Resulting JSON string is: {"registration_number": "PC38927Z" ..... }

Z:/>python 02.py
What can I do for you?
1 - produce a JSON string describing a vehicle
2 - decode a JSON string into vehicle class
Your choice: 2
Enter vehicle JSON string: {"registration_number": "PC38927Z" ...... }


Your task is to write a code which has exactly the same conversation with the
user and:

1. defines a class named Vehicle, whose objects can carry the vehicle data
shown above (the structure of the class should be deducted from the above
dialog — call it "reverse engineering" if you want)
2. defines a class able to encode the Vehicle object into an equivalent JSON
string;
3. defines a class able to decode the JSON string into the newly created
Vehicle object.

Of course, some basic data validity checks should be done, too. We're sure
you're careful enough to protect your code from reckless users.

"""

import json

class Vehicle:
    def __init__(self, regno, yop, psgr, mass):
        self.registration_number = regno
        self.year_of_production = yop
        self.passenger = psgr
        self.mass = mass

class MyEncoder(json.JSONEncoder):
    def default(self, v):
        if isinstance(v, Vehicle):
            return v.__dict__
        else:
            super().default(v)

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_veh)

    def decode_veh(self, veh):
        return Vehicle(veh["registration_number"], veh["year_of_production"],
                       veh["passenger"], veh["mass"])
        #Bug: This call is resulting in error. Need to understand and fix
        #return Vehicle(**veh)

def data_encode(v):
    if isinstance(v, Vehicle):
        return v.__dict__
    else:
        raise TypeError("v.__class__.__dict__" + " is not JSON serializable")

def data_decode(v):
    return Vehicle(v["registration_number"], v["year_of_production"], v["passenger"], v["mass"])


print("What can I do for you?")
print("1 - produce a JSON string describing a vehicle")
print("2 - decode a JSON string into vehicle class")
choice = ""
while choice not in ['1', '2']:
    choice = input("Your choice: ")
    if choice == '1':
        regno = input("Registration number: ")
        yop = int(input("Year of production: "))
        psgr = input("Passenger [y/n]: ").upper() == 'Y'
        mass = float(input("Vehicle mass: "))

        veh = Vehicle(regno, yop, psgr, mass)
        #jstr = json.dumps(veh, default=data_encode)
        jstr = json.dumps(veh, cls=MyEncoder)
        print("Resulting JSON string is: \n" + jstr)
    else:
        jstr = input("Enter vehicle JSON string: ")
        #vobj = json.loads(jstr, object_hook=data_decode)
        vobj = json.loads(jstr, cls=MyDecoder)
        print("Resulting PYTHON Obj is: ")
        print(vobj.__dict__)
    print("Done")



