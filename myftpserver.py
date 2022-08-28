
from base64 import decode
import socket
import threading
from tracemalloc import start
import os

PORT = 5000
SERVER = '192.168.1.121'
HEADER = 64
discoMessage = "DISCONNECT"
server_address = (SERVER, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
#Χειρισμός του πελάτη για διάφορες απαιτήσεις απο την πλευρά του
def clientHandle(c,addr):
    print(f"New connection {addr} detected")
    connected = True
    while connected:
        messageLength = c.recv(HEADER).decode()
        if messageLength:
            messageLength = int(messageLength)
            message = c.recv(messageLength).decode()
            if "list1" in message:
                c.send("---".join( os.listdir()).encode())
            elif ("mkdir" in message):
                os.makedirs(message.split()[1])
            elif "put" in message:
                filename = message.split()[1]
                message = message.split()
                message.pop(0)
                message.pop(0)
                message = " ".join(message)
                try:
                    f = open(filename,"w")
                    f.write(message)  
                    f.close()
                except:
                    c.send("Could not open file!".encode()) 
            elif 'get' in message:
                filename = message.split()[1]
                try:
                    f = open(filename,"r")
                    c.send(f.read().encode())
                    f.close()
                except:
                    c.send("Exception! Could not open file!".encode())
            elif "cd" in message:
                os.chdir(message.split()[1])
                

            elif (message == discoMessage or message == "bye"):
                connected = False
                
            print(f"[{addr}] {message}")
            
    c.close() 
       
#Η συνάρτηση που ξεκινά των server
def startServer():
    sock.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        c,addr = sock.accept()
        thread = threading.Thread(target=clientHandle,args=(c,addr)) #Δημιουργία thread και κλήση της συνάρτησης για χειρισμό του πελάτη.
        thread.start()
        print(f"Active connections {threading.active_count() -1 }") #Τυπώνει τα ενεργά threads






print("Starting server.....")
startServer()