"""
Connect to JSON server running on localhost at port 3000
"""

import requests

reply = requests.get("http://localhost:3000")
if reply.status_code == requests.codes.ok:
    print(reply.headers)
    print(reply.text)

