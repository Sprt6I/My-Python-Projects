import socket
import threading
import sys
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QLineEdit, QTextEdit, QPushButton
from PySide6.QtCore import QObject, Signal, Slot

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
        self.client.send(f'Name:{self.name}'.encode(FORMAT))
        
        self.UI_()
        
        getMess = threading.Thread(target=self.GetMess_, args=())
        getMess.start()
        
    def UI_(self):
        mainLayout = QVBoxLayout()
        
        toText = QLabel('Send Message')
        self.messageBox = QLineEdit('To:')
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
        text = self.messageBox.text()
        self.client.send(f'{self.name}:{text}'.encode(FORMAT))
    
    def GetMess_(self):
        while 1:
            mess = self.client.recv(SIZE).decode(FORMAT)
            print(f'\n [MESSAGE] {mess}\n')
            signaller.message_signal.emit(mess)
        
    @Slot(str)
    def update_message(self, message):
        self.incomingMessageBox.setReadOnly(False)
        text = self.incomingMessageBox.toPlainText() + f'\n{message}'
        self.incomingMessageBox.setText(text)
        self.incomingMessageBox.setReadOnly(True)
        
if __name__=='__main__':
    appWindow = clientApp()
    appWindow.show()
    app.exec()