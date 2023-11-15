import socket
import threading
import sys
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QLineEdit, QTextEdit, QPushButton, QTabWidget
from PySide6.QtCore import QObject, Signal, Slot
from icecream import ic
from client import clientApp

SERVER_ADDRESS = '10.156.0.223'
SERVER_PORT = 9090
FORMAT = 'utf-8'
SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_ADDRESS, SERVER_PORT))


class RegisterLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.login = False
        self.setWindowTitle("Register/Login")
        
        self.UI_()
        
    def UI_(self):
        mainLayout = QVBoxLayout()
        self.tabs = QTabWidget(self)
        mainTab = QWidget()
        
        appName = QLabel('My MESS')
        mainLayout.addWidget(appName)
        
        userNameInput = QLineEdit("Input username: ")
        self.passwordInput = QLineEdit("Input password: ")
        mainLayout.addWidget(userNameInput)
        mainLayout.addWidget(self.passwordInput)
        
        LoginButton = QPushButton('Login')
        LoginButton.clicked.connect(lambda: self.Login_(userNameInput.text()))
        mainLayout.addWidget(LoginButton)
        
        
        mainTab.setLayout(mainLayout)
        
        self.tabs.addTab(mainTab, "Main Tab")
        self.RegisterTab_()
        
    def RegisterTab_(self):
        registerTab = QWidget()
        registerLayout = QVBoxLayout()
        
        registerUserNameInput = QLineEdit("Input username: ")
        self.registerPasswordInput = QLineEdit("Input password: ")
        registerLayout.addWidget(registerUserNameInput)
        registerLayout.addWidget(self.registerPasswordInput)
        
        registerButton = QPushButton('Register')
        registerButton.clicked.connect(lambda: self.Register_(registerUserNameInput.text()))
        registerLayout.addWidget(registerButton)
        
        registerTab.setLayout(registerLayout)
        self.tabs.addTab(registerTab, "Main Tab")
        
    def Login_(self, name: str):
        userName = name.split(':')[1]
        userName = userName[1:]
        ic(userName)
        
        client.send(f'Check|{userName}'.encode(FORMAT))
        getCheckLogin = threading.Thread(target=self.GetMess_, args=())
        getCheckLogin.start()
        
        print(client)
        
        if self.login:
            print('Login....')
            window = clientApp(client,userName)
            window.show() 
        
    def Register_(self, name: str):
        userName = name.split(':')[1]
        userName = userName[1:]
        ic(userName)
        
        
        client.send(f'Name|{userName}'.encode(FORMAT))
        print(client)
        
    def GetMess_(self):
        while 1:
            mess = client.recv(SIZE).decode(FORMAT)
            ic(mess)
            if mess:
                self.login = True
            else:
                self.login = False
                
        
        
    
print('a')
app = QApplication.instance()
if app is None:
   app = QApplication(sys.argv)
   print('b')
   
LoginRegWin = RegisterLoginWindow()
LoginRegWin.show()
app.exec()
print('c')
