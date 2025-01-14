"""
Convert python object into json
Converting an object to any other portable aspect is called serialization
"""

"""
Method 1
"""

import json
class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + "is not JSON serializable")

someone = Who("Mahi", 39)
#print(json.dumps(someone.__dict__))
print(json.dumps(someone, default=encode_who))

"""
Method 2
"""

import json

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)


some_man = Who('John Doe', 42)
print(json.dumps(some_man, cls=MyEncoder))