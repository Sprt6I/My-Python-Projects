from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

app = QApplication(sys.argv)

class App(QWidget):  
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('To Do')
        
        self.layout = QGridLayout()
        self.row = 1
        
        AddTaskNameInput = QLineEdit()
        self.layout.addWidget(AddTaskNameInput,0,0)
        
        AddTaskBut = QPushButton('AddTask')
        AddTaskBut.clicked.connect(lambda: self.addTask123(AddTaskNameInput.text()))
        self.layout.addWidget(AddTaskBut,0,1)
        
        self.setLayout(self.layout)
        
    def addTask123(self,nameOfTask):
        DoneBut = QPushButton('Done !')
        mainBut = QPushButton(nameOfTask)
        self.layout.addWidget(DoneBut,self.row,0)
        self.layout.addWidget(mainBut,self.row,1)
        
        self.row+=1
        
    
        
window = App()
window.show()
app.exec()