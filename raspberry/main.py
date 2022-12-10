import socket
import colorama
from utils.data_handler import *

# Setzen der host Adresse + Port difinition
HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
#server initialisieren und binden
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
#server starten (listen)
server.listen()
#init the client list


def main():
    print(f"Verbinden Können sie sich auf ihrem PC unter der {HOST}:{PORT} | Alle gesendeten Dateien befinden sich im recv ordner!")
    
    while True:
        client, addr = server.accept()
        print(f"Connect to {addr}")
        handle(client)
        client.close()

if __name__ == "__main__":
    main()
