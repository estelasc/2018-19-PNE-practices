# We are programming our first client

import socket

# Create a socker for communication with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 8080
IP = "212.128.253.64"

# Connect to the server
Chat = True
while Chat:
    s.connect((IP, PORT))

    s.send(str.encode(input("Enter the message you want to send:")))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER: ")
    print(msg)

    s.close()

    Exit = input("Write 'yes' if you want to exit.")
    Exit.lower()
    if Exit == "yes":
        Chat = False

print("All is ok")