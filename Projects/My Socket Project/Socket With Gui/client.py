from ast import List
import socket
import threading
import sys
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QLineEdit, QTextEdit, QPushButton
from PySide6.QtCore import QObject, Signal, Slot
from icecream import ic
from random import randrange

SERVER_ADDRESS = '192.168.0.31'
SERVER_PORT = 9090
FORMAT = 'utf-8'
SIZE = 1024

app = QApplication(sys.argv)
app.setStyleSheet(
    'QWidget{background-color:black; color:white;}'
    'QPushButton {background-color: black;color:white;border:1px solid white;}'
    'QLineEdit {background-color:black; color:white; border 1px solid white}'
    'QTextEdit {background-color:black; color:white; border:1px solid white}'
)


print('\n\nSend Message To Server: message')
print('Send Message To User: To:Name:message\n\n')

class Signaller(QObject):
   message_signal = Signal(str)

signaller = Signaller()

class clientApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QMess')
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((SERVER_ADDRESS, SERVER_PORT))
        
        signaller.message_signal.connect(self.update_message)
        
        #Sets Name
        self.name = input('Input Name: ')
        self.client.send(f'Name|{self.name}'.encode(FORMAT))
        
        self.UI_()
        
        getMess = threading.Thread(target=self.GetMess_, args=())
        getMess.start()
        
    def UI_(self):
        mainLayout = QVBoxLayout()
        
        toText = QLabel('Send Message')
        self.messageBox = QLineEdit('To|')
        sumbmitButton = QPushButton('Sumbmit')
        sumbmitButton.clicked.connect(self.Send_)
        self.incomingMessageBox = QTextEdit()
        self.incomingMessageBox.setReadOnly(True)
        
        mainLayout.addWidget(toText)
        mainLayout.addWidget(self.messageBox)
        mainLayout.addWidget(sumbmitButton)
        mainLayout.addWidget(self.incomingMessageBox)
        
        self.setLayout(mainLayout)
        
    def Send_(self):
        print('\n\n SEND MESS \n\n')
        text = self.messageBox.text()
        
        text = text.split('|')
        
        ic(text)
        
        encoder = self.EncodeMess(text[2])
        ic(encoder)
        
        text[2] = ''.join(encoder[0])
        key = encoder[1]
        start = key[0]
        add = key[1]
        
        text = '|'.join([i for i in text])
        ic(text)
        ic(key)
        
        
        self.client.send(f'{self.name}|{text}|{start}|{add}'.encode(FORMAT))

    def GetMess_(self):
        print('\n\n GET MESS \n\n')
        while 1:
            mess = self.client.recv(SIZE).decode(FORMAT)
            
            mess = mess.split('|')
            ic(mess)
            
            ic(mess[2])
            decoder = self.DecodeMess(mess[1], [mess[2], mess[3]]) 
            ic(decoder)
            
            mess = '|'.join(mess[:-2])+": "+ f'{decoder}'
            
            ic(mess)
            
            print(f'\n [MESSAGE] {mess}\n')
            signaller.message_signal.emit(mess)
        
    @Slot(str)
    def update_message(self, message):
        self.incomingMessageBox.setReadOnly(False)
        text = self.incomingMessageBox.toPlainText() + f'\n{message}'
        self.incomingMessageBox.setText(text)
        self.incomingMessageBox.setReadOnly(True)
        
    def EncodeMess(self, mess:str):
        KeyArray = []
        EncodedMess = ''
        add = randrange(300, 1200)
        
        for let in mess:
            start = randrange(0, 5)
            KeyArray.append(start)
            startNum = ''
            
            for i in range(start):
                startNum+=str(randrange(0,9))
            ic(startNum)
            
                           
            EncodedMess+=f'{startNum}{ord(let)+add}{randrange(0,9)}/' if let!=' ' else '!#!/'
        ic(EncodedMess)
        ic(KeyArray)
        return [''.join(EncodedMess[:-1]), [KeyArray, add]]
    
    def DecodeMess(self, EncodedMess, key):
        EncodedMess = EncodedMess[1:] #Everytime 0 elemet of mess is ' ' because  f'[MESSAGE] {address}: {mess}' (space between ':' and mess)
        EncodedMess = EncodedMess.split('/')
        
        ic(EncodedMess)
        minus = key[1]
        key = key[0]
        key = [int(i) for i in key[1:-1] if i not in ' ,']
        ic(key)
        
        for indx, num in enumerate(EncodedMess):
            ic(num[key[indx]:-1])
            EncodedMess[indx] = chr(int(num[key[indx]:-1]))
        ic(EncodedMess)
        
        return ''.join(EncodedMess)
        
if __name__=='__main__':
    appWindow = clientApp()
    appWindow.show()
    app.exec()