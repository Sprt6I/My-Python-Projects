import socket
import threading

HOST = '192.168.1.16'
PORT = 9090
ENCODER = 'utf-8'
BYTE_SIZE = 1024

def reciveMess_(clientConn):
    while True:
        mess = clientConn.recv(BYTE_SIZE).decode(ENCODER)
        print(mess)

client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

receive_thread = threading.Thread(target=reciveMess_, args=(client,))
receive_thread.start()

clientName = input("Input Name: ")
client.send(f'Name:{clientName}'.encode(ENCODER))

while True:
    ToSpecify = input('To: ')
    message = input('')
    client.send(f'{ToSpecify}:{message}'.encode(ENCODER))
    
    if message=='quit': 
        client.close()
        break
    
    