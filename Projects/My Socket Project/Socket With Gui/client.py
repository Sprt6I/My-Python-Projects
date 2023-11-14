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
        
        #Connects With Server
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
        text = self.messageBox.text() #Gets Message
        
        text = text.split('|') #Splits it using '|'
        ic(text)
        
        MessageToSend = text[2]
        
        
        encoder = self.EncodeMess(MessageToSend)
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
        while 1:
            mess = self.client.recv(SIZE).decode(FORMAT)
            
            if mess:
                print('\n\n GET MESS \n\n')
            
            mess = mess.split('|')
            FromMessage = mess[0]
            Message = mess[1]
            KeyToMess = mess[2]
            AddToMess = mess[3]
            
            ic(mess)
            ic(AddToMess)
            
            ic(KeyToMess)
            decoder = self.DecodeMess(Message, KeyToMess, AddToMess) 
            ic(decoder)
            
            mess = '|'.join(mess[:-3])+": "+ f'{decoder}'
            
            ic(mess)
            
            print(f'\n [MESSAGE] {mess}\n')
            signaller.message_signal.emit(mess)
        
    @Slot(str)
    def update_message(self, message): #Add Messages We Get On The Screen
        self.incomingMessageBox.setReadOnly(False)
        text = self.incomingMessageBox.toPlainText() + f'\n{message}'
        self.incomingMessageBox.setText(text)
        self.incomingMessageBox.setReadOnly(True)
        
    def EncodeMess(self, mess:str):
        print('\n ENCODING MESS \n')
        KeyArray = [] #Array With Key
        EncodedMess = ''
        adds = []
        
        
        for let in mess:
            start = randrange(0, 5)
            startNum = ''
            KeyArray.append(start)
            for i in range(start): #Every Number Has Random Numers At Start (start = randrange(0,5)) In Range 0-9
                startNum+=str(randrange(0,9))
            ic(startNum)
            
            add = randrange(300, 1200)
            adds.append(str(add))
            
            EncodedMess+=f'{startNum}{ord(let)+add}{randrange(0,9)}/' if let!=' ' else f'{startNum}{ord(" ")+add}{randrange(0,9)}/'
            
            
        ic(EncodedMess)
        ic(KeyArray)
        
        '''
        for word in EncodedMess.split('/'):
            for indx, let in enumerate(word):
                ic(f'{let}{word[indx+1]}')
                ic(int(f'{let}{word[indx+1]}'))
                ic(x:=chr(int(f'{let}{word[indx+1]}')))
                ic(ord(x))
        ''' 
            
        #ic(EncodedMess)
        
        return [''.join(EncodedMess[:-1]), [KeyArray, adds]] #Return Array[0] = Message, Array[1] = Key
    
    def DecodeMess(self, EncodedMess, key, adds):
        print('\n DECODING MESS \n')
        EncodedMess = EncodedMess[1:] #Everytime 0 elemet of mess is ' ' because  f'[MESSAGE] {address}: {mess}' (space between ':' and mess)
        EncodedMess = EncodedMess.split('/')
        ic(EncodedMess)
        ic(key)
        
        start = key
        start = [int(i) for i in start[1:-1] if i not in ' ,'] #Key is string so we convert it to array
        ic(start)
        
        add = []
        s = ''
        for let in adds[1:-1]:
            if let not in ", '" and let!='':
                s+=let
            else:
                if s:
                    add.append(int(s))
                s = ''
                
        ic(add)
                
        
        DecodedMessage = ''
        
        
        for indx, num in enumerate(EncodedMess):
            ic(num[start[indx]:-1])
            
            letter = int(num[start[indx]:-1])
            letter -=add[indx]
            ic(letter)
            DecodedMessage += chr(letter)
        ic(DecodedMessage)
        
        return ''.join(DecodedMessage)
        
if __name__=='__main__':
    appWindow = clientApp()
    appWindow.show()
    app.exec()