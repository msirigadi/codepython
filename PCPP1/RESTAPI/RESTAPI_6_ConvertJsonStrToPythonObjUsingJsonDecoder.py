"""
Convert json str to python object using json decoder
"""

import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Myencoder(json.JSONEncoder):
    def default(self, p):
        if isinstance(p, Person):
            return p.__dict__
        else:
            super().default(p)

class Mydecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_person)

    def decode_person(self, d):
        print(d["name"], d["age"])
        return Person(**d)

p = Person("Mahi", 39)
jstr = json.dumps(p, cls=Myencoder)
print(type(jstr), jstr)
pobj = json.loads(jstr, cls=Mydecoder)
print(type(pobj), pobj.__dict__)