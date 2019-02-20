import termcolor
import socket

PORT = 3000
IP = "10.0.32.54"
MAX_OPEN_REQUEST = 5


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    termcolor.cprint("Message from the client: {}".format(msg), 'green')

    # Sending the message back to the client
    # because it is an echo server
    cs.send(str.encode(msg))


# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Process the client request
    print("Attending client: {}".format(address))

    process_client(clientsocket)

    # Close the socket
    clientsocket.close()
