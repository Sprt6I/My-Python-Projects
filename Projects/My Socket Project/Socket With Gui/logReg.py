import socket
import threading
import sys
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QLineEdit, QTextEdit, QPushButton, QTabWidget
from PySide6.QtCore import QObject, Signal, Slot
from icecream import ic

class RegisterLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register/Login")
        
        self.UI_()
        
    def UI_(self):
        mainLayout = QVBoxLayout()
        self.tabs = QTabWidget(self)
        mainTab = QWidget()
        
        appName = QLabel('My MESS')
        mainLayout.addWidget(appName)
        
        self.userNameInput = QLineEdit("Input username: ")
        self.passwordInput = QLineEdit("Input password: ")
        
        sumbmitButton = QPushButton('Login')
        mainLayout.addWidget(sumbmitButton)
        
        self.RegisterTab_()
        
        self.tabs.addTab(mainTab, "Main Tab")
        
    def RegisterTab_(self):
        registerTab = QWidget()
        registerLayout = QVBoxLayout()
        
        self.registerUserNameInput = QLineEdit("Input username: ")
        self.registerPasswordInput = QLineEdit("Input password: ")
        
        registerButton = QPushButton('Register')
        registerLayout.addWidget(registerButton)
        
        self.tabs.addTab(registerTab, "Main Tab")
        