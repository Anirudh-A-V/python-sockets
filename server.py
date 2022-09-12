import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())                          # IP address of the local server
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!EXIT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                   # create a socket object
server.bind(ADDR)                                                            # bind the socket to the address

c_message = ""
c_addr = ""

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    global c_message
    global c_addr
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)                        # receive the length of the message
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)                       # receive the message
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            if c_message == "":
                pass
            else:
                c_message = f"[{c_addr}] {c_message}"
                conn.send(c_message.encode(FORMAT))                          # send the message to the client
                c_message = ""
                c_addr = ""
            
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
            c_message = msg
            c_addr = addr
    
    conn.close()                                                             # close the connection
        

def start():
    server.listen()                                                          # start listening for connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # accept a connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))   # create a thread for each client
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")        # print the number of active connections

print("[STARTING] server is starting...")
start()