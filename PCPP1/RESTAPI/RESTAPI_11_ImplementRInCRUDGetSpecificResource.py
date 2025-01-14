"""
Instead of getting entire contents of resource, get specific resource using id
"""

import requests

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

try:
    reply = requests.get("http://localhost:3000/cars/2")
except requests.RequestException:
    print("Communication Error")
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    else:
        print("Server Error")