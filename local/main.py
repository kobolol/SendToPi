import socket
import colorama
from utils.data_sender import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Es Können nur Files gesendet werden, Ordner werden nicht gesendet!")
ip = input("Geben sie die Zu verbinden IP an: ")
port = int(input("Geben sie den Port an: "))
client.connect((ip, port))
send(client)
client.close()
print("Transfer Beendet, bitte Server auf Fehler checken")
