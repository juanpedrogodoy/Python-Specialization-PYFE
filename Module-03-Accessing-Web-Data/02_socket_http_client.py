# Low-level HTTP Client (Sockets)
# PY4E - Module 3 (Network Programming)
# This script manually creates a TCP connection using sockets,
# sends an HTTP GET request, and decodes the server's response.

import socket

# Creating the socket: AF_INET (IPv4) and SOCK_STREAM (TCP)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# The request must be encoded to bytes before sending it over the network
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # Decoding bytes back to string for printing
    print(data.decode(), end='')

mysock.close()
