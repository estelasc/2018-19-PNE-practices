# This is a client that ask the user for a DNA sequence. Then it will send this sequence to the server that must return
# the complement of that sequence.
import socket

Port = 3000
IP = "192.168.1.34"


not_exit = True
while not_exit:

    # First of all, we create the socket for communication with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Now, we connect to the server
    s.connect((IP, Port))

    # Here we ask for a DNA sequence
    chain = input("Please, enter a valid DNA sequence: ")

    # Then we send the message to the server
    s.send(str.encode(chain))

    msg = s.recv(2048).decode("utf-8")
    print("Message from the server: {}".format(msg))

    # Here, you give the user the opportunity to go out
    Bye_bye = input("Write 'yes' if you want to exit: ")
    Bye_bye = Bye_bye.lower()
    if Bye_bye == 'yes':
        print("Bye bye.")
        not_exit = False

    s.close()
