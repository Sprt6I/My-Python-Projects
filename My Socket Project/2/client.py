import socket
import threading

FORMAT = 'utf-8'
PORT = 9090
HEADER = 64
IP = '192.168.0.31'
SERVER_ADDR = (IP, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER_ADDR)


def send_(mess: str):
    messLen = len(mess.encode(FORMAT))
    sendLen = str(messLen).encode(FORMAT)
    sendLen += b' ' * (HEADER - len(sendLen))
    print(mess)
    client.send(sendLen)
    client.send(mess.encode(FORMAT))
    
def listen_():
    mess = client.recv(1024).decode(FORMAT)
    print(mess)
  
name = input('Input name: ')
send_(f'Name:{name}')
print(name)
    
while 1:
    mess = input("Input message: ")
    send_(mess)
    
    ServerMess = threading.Thread(target=listen_)
    ServerMess.start()
    
    print(mess)
    if mess=='quit':
        client.close()
        exit()