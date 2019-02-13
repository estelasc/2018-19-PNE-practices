# Client created to connect to my partner server.
import socket


PORT = 1111
IP = "212.128.253.69"


ok = True
while ok:

    # Create a socker for communication with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((IP, PORT))

    mess = input("Write your message: ")
    s.send(str.encode(mess))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER: {}".format(msg))

    Exit = input("If you want to finish the chat, write 'yes': ")
    Exit = Exit.replace(" ", "").lower()
    if Exit == 'yes':
        ok = False

    s.close()
