import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # IP address of the local server
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!EXIT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object

server.bind(ADDR) # bind the socket to the address


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(64).decode(FORMAT) # receive the length of the message
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) # receive the message
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    
    conn.close() # close the connection
        

def start():
    server.listen() # start listening for connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # accept a connection
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # create a thread for each client
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") # print the number of active connections

print("[STARTING] server is starting...")
start()