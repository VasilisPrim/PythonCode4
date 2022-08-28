from http import client
import socket
from webbrowser import get

from myftpserver import HEADER

PORT = 5000
SERVER = '192.168.1.121'
HEADER = 64
server_address = (SERVER, PORT)
discoMessage = "DISCONNECT"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
#Πρωτόκολλο για να στέλνεις εκτός απο το μήνυμα και πληροφορίες για το μήκος του.
def msgProtocol(message):
    my_message = message.encode()
    messageLength = len(my_message)
    send_length = str(messageLength).encode()
    send_length = send_length + b' '*(HEADER - len(send_length))
    sock.send(send_length)
    sock.send(my_message)
#Η συνάρτηση για να στέλνει ο πελάτης μηνύματα στον εξυπηρετητή με κατάλληλους ελέγχους για τα put και get
def send(message):
    if "put" in message:
        filename = message.split()[1]
        try:
            f = open(filename,"r")
            message = message +" " + f.read()
            msgProtocol(message) #Κλήση του πρωτοκόλλου για αποστολή μηνυμάτων.
            f.close()
        except:
            print("Could not find file!")
        print(sock.recv(4096).decode())
    elif 'get' in message:
        msgProtocol(message)
        f = open(message.split()[1],"w")
        receivedData = sock.recv(4096).decode()
        if receivedData.startswith("Exception"):
            print("Could not open file!")
        else:    
            f.write(receivedData)
            f.close()
    else:
        msgProtocol(message)    
        print( sock.recv(4096).decode())
    
     
     #Υποθέτω ότι το αρχείο που θα σταλεί είναι σχετικά μικρό.Αλλιώς πρέπει να γραφτεί ξανά ο κώδικας της msgProtocol
    
msg = input("Give a command: ")
send(msg)
