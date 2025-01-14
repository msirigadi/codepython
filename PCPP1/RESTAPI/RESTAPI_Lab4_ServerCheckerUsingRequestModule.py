"""
Objectives
Learn how to:

use the requests module facilities;
interpret server responses.

Scenario

Now we want to you to return to the issues discussed in lab #1. In fact, you
need to implement exactly the same functionality as you embedded in your code
previously, but this time you have to use the requests module instead of the
socket module. Everything else should remain the same: the command line
arguments and outputs have to be indistinguishable.

Hint: use the head() method instead of get(), as you don't need the whole root
document the server sends to you — the header is enough to test whether or not
the server is responding. Fortunately, head() has exactly the same interface
as get(). Don't forget to handle all needed exceptions — don't leave your user
without any clear explanations about anything that went wrong.
"""

import requests
import sys

args = len(sys.argv)

if args not in [2, 3]:
    print("Improper number of arguments: at least one is required and not more "
          "two are allowed\n"
          " - http server's address (required)\n"
          " - port number (defaults to 80 if not specified")
    exit(1)

server_addr = sys.argv[1]
port_num = 80

if args == 3:
    try:
        port_num = int(sys.argv[2])
    except:
        print("Port number is invalid - Exiting")
        exit(2)
    else:
        if port_num <= 1 or port_num >= 65535:
            print("Port number should be in the range 1 to 65535")
            exit(2)

uri = "http://" + server_addr + ":" + str(port_num) + '/'
try:
    reply = requests.head(uri)
except requests.exceptions.ConnectionError:
    print("Failed to connect to server")
    exit(3)
except requests.exceptions.Timeout:
    print("Timeout Error")
    exit(4)
except:
    print("Server Error")
    exit(5)
else:
    print(reply.status_code, reply.reason)
