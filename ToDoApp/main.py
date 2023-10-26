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
        AddTaskBut.clicked.connect(lambda: self.addTask(AddTaskNameInput.text()))
        self.layout.addWidget(AddTaskBut,0,1)
        
        self.text = 2
        
        self.setLayout(self.layout)
        
    def addTask(self,nameOfTask):
        self.TaskLayout = QHBoxLayout()
        DoneBut = QPushButton('Done !')
        mainBut = QPushButton(nameOfTask)
        DoneBut.clicked.connect(lambda: self.DeleteTask(DoneBut, mainBut))
        
        self.layout.addWidget(DoneBut, self.row, 1)
        self.layout.addWidget(mainBut,self.row, 0)
        
        self.row+=1
        self.adjustSize()
        
    def DeleteTask(self,DoneBut,mainBut):
        DoneBut.deleteLater()
        mainBut.deleteLater()
        
        self.adjustSize()
        
window = App()
window.show()
app.exec()