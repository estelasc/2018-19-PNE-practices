# We are programming our first client

import socket

# Create a socker for communication with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 8080
IP = "212.128.253.64"

# Connect to the server
s.connect((IP, PORT))

s.send(str.encode("Hello from my client"))

msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER: ")
print(msg)

s.close()

print("The end.")
