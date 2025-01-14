"""
Objectives
Learn how to:
    use the socket module and its basic functionalities;
    manage simple http connections.

Scenario
We want you to write a simple CLI (Command Line Interface) tool which can be
used in order to diagnose the current status of a particular http server. The
tool should accept one or two command line arguments:

1. (obligatory) the address (IP or qualified domain name) of the server to be
diagnosed (the diagnosis will be extremely simple, we just want to know if the
server is dead or alive)
2. (optional) the server's port number (any absence of the argument means that
the tool should use port 80)
3. use the HEAD method instead of GET — it forces the server to send the full
response header but without any content; it's enough to check if the server is
working properly; the rest of the request remains the same as for GET.

We also assume that:

the tool checks if it is invoked properly, and when the invocation lacks any
arguments, the tool prints an error message and returns an exit code equal to 1;

if there are two arguments in the invocation line and the second one is not an
integer number in the range 1..65535, the tool prints an error message and
returns an exit code equal to 2;

if the tool experiences a timeout during connection, an error message is
printed and 3 is returned as the exit code;

if the connection fails due to any other reason, an error message appears and 4
is returned as the exit code;

if the connection succeeds, the very first line of the server’s response is
printed.

Hints:

to access command line arguments, use the argv variable from the sys module;
its length is always one more than the actual number of arguments, as argv[0]
stores your script's name; this means that the first argument is at argv[1] and
the second at argv[2]; don't forget that the command line arguments are always
strings!

returning an exit code equal to n can be achieved by invoking the exit(n)
function.

Assuming that the tool is placed in a source file name sitechecker.py, here are
some real-use cases:

python sitechecker.py
Improper number of arguments: at least one is required and not more than two
are allowed
- http server's address (required)
- port number (defaults to 80 if not specified)

python sitechecker.py education.pythoninstitute.org port
Port number is invalid - exiting

python sitechecker.py education.pythoninstitute.org 80
HTTP/1.1 302 Found

python sitechecker.py education.pythoninstitute.org
HTTP/1.1 302 Found
"""

import sys
import socket

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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    #sock.settimeout(0.00001)
    sock.settimeout(10)
    sock.connect((server_addr, port_num))
except socket.timeout:
    print("Timeout Error")
    exit(3)
except:
    print("Connection to server failed")
    exit(4)

sock.send(b'HEAD / HTTP/1.1\r\nHost: ' +
          bytes(server_addr, "utf-8") +
          b'\r\nConnection: close\r\n\r\n')
reply = sock.recv(100).decode("utf8")
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(reply[:reply.find('\r')])