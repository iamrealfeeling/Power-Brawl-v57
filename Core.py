serverAddress = ("0.0.0.0", 9339)

import socket
from Classes.Connection import Connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(serverAddress)
print(f"Listening for new connection...")
while True:
    server.listen()
    socket, address = server.accept()
    print(f"New player: {address[0]}:{address[1]}")
    Connection(socket, address).start()