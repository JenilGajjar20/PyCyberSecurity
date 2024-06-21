import socket

# Creating a socket object
c = socket.socket()

# Connecting the socket object to the specified address and port
c.connect(('localhost', 9999))

# Prompt the user to enter name
name = input('Enter your name: ')

# Sending the entered name to the server
c.send(bytes(name, 'utf-8'))

# Receiving the message from the server
print(c.recv(1024).decode())
