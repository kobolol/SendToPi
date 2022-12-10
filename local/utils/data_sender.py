import socket
import colorama
import os
from os import listdir
from os.path import isfile, join
import time

def send(client: socket):
    files = [f for f in listdir(os.getcwd() + "/send/") if isfile(join(os.getcwd() + "/send/", f))]
    if len(files) == 0:
        client.send(f"ERROR NO FILES".encode("utf-8"))
        time.sleep(1)
    else:
        client.send(f"GO".encode("utf-8"))
        time.sleep(1)
    x = 0
    for file in files:
        print(f"Send File {file}")
        client.send(file.encode("utf-8"))
        time.sleep(1)
        
        readfile = open(os.getcwd() + f"/send/{file}", "rb")
        content = readfile.read(10240)
        client.send(content)
        time.sleep(1)
        readfile.close()
        x += 1
        if x == len(files):
            client.send("Nein".encode("utf-8"))
            time.sleep(1)
        else:
            client.send("Ja".encode("utf-8"))
            time.sleep(1)
