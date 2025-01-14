"""
Convert python object into json string using method overloading
"""

import json

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Myencoder(json.JSONEncoder):
    def default(self, p):
        if isinstance(p, Person):
            return p.__dict__
        else:
            return super().default(p)


#p = Person("Mahi", 39)
#print(json.dumps(p, cls=Myencoder))

w=Who("Mahi", 39)
print(json.dumps(w, cls=Myencoder))

