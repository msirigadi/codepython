"""
Implement R(Read) in CRUD(create, read, update, delete)
"""

import requests

try:
    reply = requests.get("http://localhost:3000/cars")
except requests.RequestException:
    print("Communication Error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.headers)
        print(reply.text)
        print(reply.headers['Content-Type'])
        print(reply.json())
    else:
        print("Server Error")
