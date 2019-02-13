# Client created to connect to my own server.
import socket

# Create a socker for communication with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 1111
IP = "192.168.1.34"

# Connect to the server
s.connect((IP, PORT))

chat = True
while chat:
    mess = input("Write your message: ")
    s.send(str.encode(mess))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER: {}".format(msg))

    Exit = input("If you want to finish the chat, write 'yes': ")
    Exit = Exit.replace(" ", "").lower()
    if Exit == 'yes':
        chat = False

s.close()
