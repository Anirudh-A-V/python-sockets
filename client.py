import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.1.36"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!EXIT"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # create a socket object
client.connect(ADDR)                                              # connect to the server

print("Connected to server")

def send(msg):
    message = msg.encode(FORMAT)                                  # encode the message
    msg_length = len(message)                                     # get the length of the message
    send_length = str(msg_length).encode(FORMAT)                  # encode the length of the message
    send_length += b' ' * (HEADER - len(send_length))             # add spaces to the end of the message to make it 64 bytes long
    client.send(send_length)                                      # send the length of the message
    client.send(message)                                          # send the message
    
    print(client.recv(2048).decode(FORMAT))                       # receive the message from the server
    
while True:
    string = input(f"IP {socket.gethostbyname(socket.gethostname())} : ")
    if string == DISCONNECT_MESSAGE:
        break
    send(string)

send(DISCONNECT_MESSAGE)