# Server that analyzes DNA sequences
import socket
from SeqFromP1 import Seq
import io

# Configure the Server's IP and PORT
PORT = 2000
IP = "192.168.1.38"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")

        lines = io.StringIO(msg)
        seq = lines.readline().replace("\n", "").upper()

        messg = ""
        if seq == "":
            messg = "ALIVE"
        else:
            for letter in seq:
                if letter != "A" and letter != "C" and letter != "T" and letter != "G":
                    messg = "ERROR"
                    break
                else:
                    messg = "OK"

        list_lines = lines.readlines()
        output = ""
        msg_sent = messg + '\n'
        seq = Seq(seq)
        if messg == "OK":
            for line in list_lines:
                line = line.replace("\n", "")
                if line == "len":
                    output = seq.len()
                    output = str(output)
                elif line == "complement":
                    output = seq.complement()
                    output = output.strbase
                elif line == "reverse":
                    output = seq.reverse()
                    output = output.strbase
                elif line == "countA":
                    output = seq.count('A')
                    output = str(output)
                elif line == "countT":
                    output = seq.count('T')
                    output = str(output)
                elif line == "countC":
                    output = seq.count('C')
                    output = str(output)
                elif line == "countG":
                    output = seq.count('G')
                    output = str(output)
                elif line == "percA":
                    output = seq.perc('A')
                    output = str(output)
                elif line == "percT":
                    output = seq.perc('T')
                    output = str(output)
                elif line == "percC":
                    output = seq.perc('C')
                    output = str(output)
                elif line == "percG":
                    output = seq.perc('G')
                    output = str(output)
                else:
                    output = "ERROR"
                msg_sent += output + '\n'

        print("Message from client: {}".format(msg))

        # Send the message
        send_bytes = str.encode(msg_sent)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
