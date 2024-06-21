import socket

# Creating a socket object
s = socket.socket()
print('Socket Created')

# Binding the socket to a specific address and port number
s.bind(('localhost', 9999))

# Enable the socket to accept connections
s.listen(3)
print('Waiting for connection...')

while True:
    # Accept the connection from a client
    # Created a new socket object (c) of the client
    # addr is the address of the client
    c, addr = s.accept()

    # receive the data from the client, with a buffer size of 1024 bytes
    name = c.recv(1024).decode()

    print("Connected with: ", addr, name)

    # Sending a message to the client
    c.send(bytes('Message to client', 'utf-8'))

    # Closing the connection
    c.close()
