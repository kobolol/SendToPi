import socket
import colorama
import time
import os

def handle(client: socket.socket):
    start_cmd = client.recv(1024).decode("utf-8")
    print(start_cmd)
    if start_cmd == "GO":
        print("Starting Data Transfer")
        weiter = True
        while weiter:
            filename = client.recv(1024).decode("utf-8")
            filecontent = client.recv(10240)
            if os.path.exists(os.getcwd() + "/recv/" + filename):
                os.remove(os.getcwd() + "/recv/" + filename)
                print(f"{filename} exist, we delete the old file and write the new file!")

            file = open(os.getcwd() + "/recv/" + filename, "xb")
            file.write(filecontent)
            file.close()
            print(f"write file {filename}")
            existnextfile = client.recv(1024).decode("utf-8")
            if existnextfile == "Nein":
                weiter = False
        print("File Transfer End!")
    
    else:
        print("error!")
