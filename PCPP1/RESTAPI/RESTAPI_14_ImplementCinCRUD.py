"""
Implement C(create) in CRUD
Add new car

if we’re going to send anything to the server, the server must be aware of what
it actually is; as you already know, the server informs us about the type of the
 contents using the Content-Type field; we can use the same technique to warn
 the server that we’re sending something more than a bare request. This is why
 we prepare our Content-Type field with the appropriate value
"""

import requests
import json

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 15, 20, 20]

def show_header():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end = '|  ')
    print()

def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end = '|  ')
    print()

def show_empty():
    for w in key_widths:
        print(" ". ljust(w), end = '|  ')
    print()

def show(json):
    show_header()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()

h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}

new_car = {'id': 1,
           'brand': 'Toyota',
           'model': 'Corolla',
           'production_year': 2004,
           'convertible': False}

print(json.dumps(new_car))

try:
    reply = requests.post("http://localhost:3000/cars", headers=h_content,
                          data=json.dumps(new_car))
    print("res=" + str(reply.status_code))
    reply = requests.get("http://localhost:3000/cars", headers=h_close)
except requests.RequestException:
    print("Communication Error")
else:
    print("Connection=" + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("Server Error")