import socket
import termcolor

# SERVER IP, PORT
IP = "10.0.32.54"
PORT = 3000

work = True
while work:
    # Communicating our client with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting our client with the server
    s.connect((IP, PORT))

    message = input("Please, enter a message to the server: ")

    s.send(str.encode(message))

    msg = s.recv(2048).decode("utf-8")
    termcolor.cprint("Message from the server: {}".format(msg), 'red')

    s.close()

    if message == "EXIT":
        work = False
