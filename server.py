import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())         # IP address of the local server
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!EXIT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket object

server.bind(ADDR)                                           # bind the socket to the address


def handle_client(conn, addr):
    pass

def start():
    pass

print("[STARTING] server is starting...")
start()