# This is a client that will ask the user for a DNA sequence. Then thanks to the class Seq that is in other file,
# it will calculate the reverse of the original sequence and the complement of the reverse of the original sequence.
# Then it will sent all three sequences to the server.
from SeqP1 import Seq
import socket

Port = 5015
IP = "192.168.1.34"


run = True
while run:

    # First of all, we create the socket for communication with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Now, we connect to the server
    s.connect((IP, Port))

    chain = input("Please, enter a valid DNA sequence: ")
    seq1 = Seq(chain)
    seq2 = seq1.reverse()
    seq3 = seq2.complement()

    s.send(str.encode("The original sequence is: {}, the reverse of the original sequence is: {}, and the complement of"
                      " the reverse sequence is: {}".format(seq1.strbase, seq2.strbase, seq3.strbase)))

    msg = s.recv(2048).decode("utf-8")
    print("Message from the server: {}".format(msg))

    # Here, you give the user the opportunity to go out
    Bye_bye = input("Write 'yes' if you want to exit: ")
    Bye_bye = Bye_bye.lower()
    if Bye_bye == 'yes':
        print("Bye bye.")
        run = False

    s.close()
