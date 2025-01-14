"""
Update one of the existing element
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

update_car = {'id': 3,
              'brand': 'Aston Martin',
              'model': 'Rapide',
              'production_year': 2015,
              'convertible': True}

print(json.dumps(update_car))

ucar = {'id': 1,
        'brand': 'Toyota',
        'model': 'Corolla',
        'production_year': 2005,
        'convertible': False}

print(json.dumps(ucar))

try:
    reply = requests.put("http://localhost:3000/cars/3", headers=h_content,
                          data=json.dumps(update_car))
    print("res=" + str(reply.status_code))

    reply = requests.put("http://localhost:3000/cars/1", headers=h_content,
                          data=json.dumps(ucar))
    print(requests.codes.__dict__)

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