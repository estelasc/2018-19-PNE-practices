# This is a client that want the server to analyze a DNA sequence
import socket

# Create a socker for communication with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 2000
IP = "192.168.1.38"

# Connect to the server
s.connect((IP, PORT))

# Operations the client wants to know about the DNA sequence
request = """ACGA
len
complement
reverse
countA
countT
countC
countG
percA
percC
percT
percG"""

# Here we send the request to the server
s.send(str.encode(request))

# Here we receive the answer of the server
msg = s.recv(2048).decode("utf-8")
print(msg)

s.close()
