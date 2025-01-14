"""
Convert json str to python object
"""

import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode(p):
    if isinstance(p, Person):
        return p.__dict__
    else:
        return TypeError(p.__class__.__name__ + " is not JSON serializable")

def decode(p):
    print(type(p))
    return Person(p["name"], p["age"])

p = Person("Mahi", 39)
jstr = json.dumps(p, default=encode)
print(jstr)
print(type(jstr))
pobj = json.loads(jstr, object_hook=decode)
print(type(pobj))
print(pobj.__dict__)