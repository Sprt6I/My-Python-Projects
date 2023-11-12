import socket
import threading

SERVER_ADDRESS = '192.168.0.31'
SERVER_PORT = 9090
FORMAT = 'utf-8'
SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_ADDRESS, SERVER_PORT))

def Send_():
    mess = input('\n>> ')
    client.send(mess.encode(FORMAT))
    
def GetMess_():
    mess = client.recv(SIZE).decode(FORMAT)
    print(f'\n [MESSAGE] {mess}\n')

#Sets Name
name = input('Input Name: ')
client.send(f'Name:{name}'.encode(FORMAT))


print('\n\nSend Message To Server: message')
print('Send Message To User: To:Name:message\n\n')

while 1:
    sender = threading.Thread(target=Send_, args=())
    sender.start()
    
    getMess = threading.Thread(target=GetMess_, args=())
    getMess.start()