# We are programming a client for connecting to the teacher's server.

import socket


PORT = 9797
IP = "212.128.253.69"


Chat = True
while Chat:

    # Create a socker for communication with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((IP, PORT))

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
