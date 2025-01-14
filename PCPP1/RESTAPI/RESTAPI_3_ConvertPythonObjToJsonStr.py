"""
Convert python object to json string
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


def encode_portable(p):
    if isinstance(p, Person):
        return p.__dict__
    else:
        raise TypeError(p.__class__.__name__ + ' is not JSON serializable')

person = Person("Mahi", 39)
#print(json.dumps(person.__dict__))

print(json.dumps(person, default = encode_portable))


w = Who("Mahi", "age")
try:
    print(json.dumps(w, default=encode_portable))
except Exception as e:
    print(e)

print("*** Done ***")

