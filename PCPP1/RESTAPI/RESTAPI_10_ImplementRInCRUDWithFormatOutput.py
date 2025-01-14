"""
Reading raw JSON messages is not fun. We will format the output and present the
server response in an elegant and clear way
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

def show(json):
    show_header()
    for car in json:
        show_car(car)

try:
    reply = requests.get("http://localhost:3000/cars")
except requests.RequestException:
    print("Communication Error")
else:
    if reply.status_code == requests.codes.ok:
        if reply.headers['Content-Type'] == 'application/json':
            show(reply.json())
    else:
        print("Server Error")
