"""
program making use of network sockets. Of course, we'll harness Python for this
purpose.

Here are our goals:

we want to write a program which reads the address of a WWW site
(e.g., pythoninstitute.org) using the standard input() function and fetches the
root document (the main HTML document of the WWW site) of the specified site;
the program outputs the document to the screen;
the program uses TCP to connect to the HTTP server.
Our program has to perform the following steps:

create a new socket able to handle connection-oriented transmissions based on TCP;
connect the socket to the HTTP server of a given address;
send a request to the server (the server wants to know what we want from it)
receive the server's response (it will contain the requested root document of the site)
close the socket (end the connection)
"""

import socket

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply))