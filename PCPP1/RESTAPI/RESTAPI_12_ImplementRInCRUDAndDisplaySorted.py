"""
A particular server may manipulate data before sending it to the client.
The json server is able to sort the items using any of the properties as a sort
key

The json-server assumes that a URI formed in the following way
http://server:port/resource?_sort=property

The json-server is also able to reverse the sort order – you just have to
rewrite the URI in the following way:

http://server:port/resource?_sort=property&_order=desc

Note the & character – it separates additional request parameters from each
other
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
    reply = requests.get("http://localhost:3000/cars?_sort=production_year")
    #reply = requests.get("http://localhost:3000/cars?_sort=production_year&_order=desc")
except requests.RequestException:
    print("Communication Error")
else:
    print("Connection=", reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    else:
        print("Server Error")