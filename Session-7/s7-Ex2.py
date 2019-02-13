# We are programming our first clientç
# I know there is an error here that I must fix, but I don't know how to do it right know. I will fix it soon.

import socket

# Create a socker for communication with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 9797
IP = "192.168.1.34"

# Connect to the server
s.connect((IP, PORT))


Chat = True
while Chat:

    # Why when I send the third message to the server, it stop working (BrokenPipeError)???
    mess = input("Enter the message you want to send to the teacher's server: ")
    s.send(str.encode(mess))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER: ")
    print(msg)

    Exit = input("Write 'yes' if you want to exit.")
    Exit = Exit.lower()
    Exit = Exit.replace(" ", "")
    if Exit == "yes":
        Chat = False


s.close()
print("The chat has finished.")
