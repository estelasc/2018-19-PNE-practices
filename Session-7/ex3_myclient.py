# Client created to connect to my partner server.
import socket

# Create a socker for communication with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 1111
IP = "192.168.1.34"

# Connect to the server
s.connect((IP, PORT))

mess = input("Write your message: ")
s.send(str.encode(mess))

msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER: {}".format(msg))

s.close()
