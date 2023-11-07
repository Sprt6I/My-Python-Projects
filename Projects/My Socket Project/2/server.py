import socket
import threading

FORMAT = 'utf-8'
PORT = 9090
HEADER = 64
IP = '192.168.0.31'
SERVER_ADDR = (IP, PORT)
print(IP)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDR)

print(f'Server Started On: {SERVER_ADDR}')

clientNames = []

def handleClient_(conn, address):
    
    while 1:
        messLen = conn.recv(HEADER).decode(FORMAT)
        if not messLen: return -1
        messLen = int(messLen)
        mess = conn.recv(messLen).decode(FORMAT)
        print(mess)
        if mess=='quit':
            conn.close()
        elif 'Name:' in mess:
            mess = mess.split(':')
            clientNames.append(mess[1])
            print(f'List Of Users: {clientNames}')
        else:
            print('\n Sending mess to someone')
            mess = mess.split('/')
            print(f'message: {mess}')
            print(f'List Of Users: {clientNames}')
            for name in clientNames:
                if name==mess[0]:
                    print(f'Sending: {mess[1]}, To {name}')
                    conn.send(mess[1].encode(FORMAT))

def start_():
    server.listen()
    while 1:
        conn, address = server.accept()
        print(f'{address} conected')
        
        handleClientThread = threading.Thread(target=handleClient_, args=(conn, address))
        handleClientThread.start()
        
        print(f'Active Connections: {threading.active_count() - 1}')
        
        
        
start_()