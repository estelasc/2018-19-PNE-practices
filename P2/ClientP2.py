from SeqP1 import Seq
import socket

Port = 5015
IP = "212.128.253.69"

chain = input("Please, enter a valid DNA sequence: ")
orig_seq = Seq(chain)
seq2 = orig_seq.reverse()
seq3 = seq2.complement()
print(orig_seq.strbase)
run = True
while run:

    # First of all, we create the socket for communication with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Now, we connect to the server
    s.connect((IP, Port))

    chain = input("Please, enter a valid DNA sequence: ")
    orig_seq = Seq(chain)
    seq2 = orig_seq.reverse()
    seq3 = seq2.complement()



    s.send(str.encode("The original sequence is: {}, the reverse of the original sequence is: {}, and the complement of"
                      " the reverse sequence is: {}".format(chain, seq2, seq3)))

    msg = s.recv(2048).decode("utf-8")
    print("Message from the server: {}".format(msg))

    # Here, you give the user the opportunity to go out
    Bye_bye = input("Write 'yes' if you want to exit: ")
    Bye_bye = Bye_bye.lower()
    if Bye_bye == 'yes':
        print("Bye bye.")
        run = False

    s.close()
