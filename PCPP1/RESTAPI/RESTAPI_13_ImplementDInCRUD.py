"""
Implement http DELETE method
And close the server connection
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

headers = {'Connection': 'Close'}
try:
    reply = requests.delete("http://localhost:3000/cars/2")
    print("res=" + str(reply.status_code))
    reply = requests.get("http://localhost:3000/cars", headers=headers)
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