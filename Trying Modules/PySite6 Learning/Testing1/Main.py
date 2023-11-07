from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class MyPyQt:
    def MyLabel(text, Styl, font=QFont("Arial", 14)):
        label = QLabel(text)
        if Styl:
            label.setStyleSheet(Styl)
        #if geometry:
        #    label.setGeometry(geometry)
        label.setFont(font)
        return label

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My PySide6 App") #Gives Window Name
        Width = 500
        Height = 700
        self.resize(Width, Height) #Sets Size Of Window
        '''
        Main = QFrame(self) #New Main Window
        Main.setFrameShape(QFrame.StyledPanel)
        Main.setFrameShadow(QFrame.Raised)
        Main.setStyleSheet("background-color:black;border-radius: 50px;text-align: center; color:white") #Sets stylesheet to window
        self.setWindowFlag(Qt.FramelessWindowHint) #Makes Window Frameless
        self.setAttribute(Qt.WA_TranslucentBackground) #Makes Window's background transparent
        '''
        lay1 = QGridLayout(self)
        #self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:black;border-radius: 50px;text-align: center; color:white") #Sets stylesheet to window
        #self.setAttribute(Qt.WA_TranslucentBackground) #Makes Window's background transparent
        
        
        
        label = QLabel("Ubank", self)
        label.setFont(QFont("Arial", 40))
        label.setStyleSheet("text-align: center;  background-color: transparent;")
        lay1.addWidget(label, 0, 2)
        #label.setGeometry(Width/2-int(label.text().__sizeof__()*1.6), 10,label.text().__sizeof__()*int(25/2), 45)
        
        label1 = QLabel("Welcome User", self)
        label1.setFont(QFont("Arial", 35))
        label1.setStyleSheet("text-align: center;  background-color: transparent;")
        lay1.addWidget(label1, 1, 2)
        
        
        self.setLayout(lay1)
        #label1.setGeometry(Width/2-int(label.text().__sizeof__()*2.5), 60,label1.text().__sizeof__()*int(25/2), 50)
        '''
        but = QPushButton("Login", Main)
        but.setGeometry(Width/2-int(but.text().__sizeof__()*4.2), Height/3, 200, 30)
        but.setStyleSheet("background-color:transparent; color:white;border:1px solid white; border-radius: 15px;")
        but.clicked.connect(self.exit_but)
        
        but = QPushButton("Register", Main)
        but.setGeometry(Width/2-int(but.text().__sizeof__()/6), Height/3, 200, 30)
        but.setStyleSheet("background-color:transparent; color:white;border:1px solid white; border-radius: 15px;")
        but.clicked.connect(self.exit_but)
        
        
        
        but = QPushButton("Exit", Main)
        but.setGeometry(Width/2-int(but.text().__sizeof__()*1.8), Height-40, 200, 30)
        but.setStyleSheet("background-color:transparent; color:white;border:1px solid white; border-radius: 15px;")
        but.clicked.connect(self.exit_but)
        '''
        
        
        #self.setCentralWidget(Main) #Sets Main as Main Window or something
        
    def exit_but(self):
        QApplication.quit()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

