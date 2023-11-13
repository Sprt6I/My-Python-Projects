import socket
import threading
import time
from icecream import ic

SERVER_ADDRESS = '192.168.0.31'
SERVER_PORT = 9090
FORMAT = 'utf-8'
SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_ADDRESS, SERVER_PORT))

clients = {}

def handleClient_(conn, address):
    while 1:
        mess = conn.recv(SIZE).decode(FORMAT)
        print(mess)
        if 'Name|' in mess:
            mess = mess.split('|')
            clients[mess[1]] = conn
            continue
        
        if 'To|' in mess:
            mess = mess.split('|')
            
            for name, addr in clients.items():
                if name==mess[2]:
                    sendtime = time.localtime()
                    hours = sendtime.tm_hour
                    minutes = sendtime.tm_min
                    secounds = sendtime.tm_sec
                    if len(str(hours))<2: hours = f'0{hours}'
                    if len(str(minutes))<2: minutes = f'0{minutes}'
                    if len(str(secounds))<2: secounds = f'0{secounds}'
                    ic(mess)
                    addr.send(f'[{hours}:{minutes}:{secounds}] {mess[0]}| {mess[3]}|{mess[4]}|{mess[5]}'.encode(FORMAT))
            
            continue
        
        print(f'[MESSAGE] {address}| {mess}')

server.listen()

print(f'[START] Server Started: {SERVER_ADDRESS}:{SERVER_PORT}')

while 1:
    conn, address = server.accept()
    print(f'[CONNECTION] {address} connected')
    
    clientHandler = threading.Thread(target=handleClient_, args=(conn, address,))
    clientHandler.start()






