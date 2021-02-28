import socket
import threading
import time
import json

PORT = 11023
HOST = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

sitename = input("Enter an IP or domain name.. ")
threads = input("Enter a thread count for the clients.. ")

def userhandling(conn,addr):
    if sitename:
        metadata = {
            "META" : {
                "sitename" : sitename,
                "action" : "start",
                "threads" : threads
            } 
        }
        conn.send(bytes(json.dumps(metadata), 'utf-8'))
    else:
        print("INVALID SITENAME, ADDRESS, OR URL")

s.listen(10)

while True:
    conn, addr = s.accept()
    userthread = threading.Thread(target=userhandling, args=(conn, addr))
    userthread.start()