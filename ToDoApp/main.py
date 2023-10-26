from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

app = QApplication(sys.argv)

app.setStyleSheet (
    'QLineEdit {border: 1px solid white; color:white; background-color:black}'
    'QPushButton {border: 1px solid white; color:white; background-color:black;}'
)

class App(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('To Do')
        self.setStyleSheet('background-color:black;color:white;font-size: 16pt;')
        self.layout = QGridLayout()
        
        self.row = 1 #Number Of Row To Add Task
        self.tasksNames = [] #Names Of Task Added
        self.taskWin = None
        self.TaskWindowsArr = []
        font = QFont()
        
        
        font.setPointSize(20)
        
        self.setFont(font)
        
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.layout.setColumnStretch(0, 4)
        self.layout.setColumnStretch(1, 1)
        
        
        
        AddTaskNameInput = QLineEdit()
        AddTaskNameInput.setFont(font)
        AddTaskNameInput.setFixedHeight(50)
        AddTaskNameInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout.addWidget(AddTaskNameInput,0,0)
        
        AddTaskBut = QPushButton('AddTask')
        AddTaskBut.setFixedHeight(50)
        AddTaskBut.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        AddTaskBut.clicked.connect(lambda: self.addTask(AddTaskNameInput.text()))
        self.layout.addWidget(AddTaskBut,0,1)
        
        self.text = 2
        
        self.setLayout(self.layout)
        
    def addTask(self,nameOfTask: str) -> int:
        """Adds Task

        Args:
            nameOfTask (str): Name Of Task To Add

        Returns:
            int: 0 if everyhing is correct else -1
        """
        if  nameOfTask=='' or not nameOfTask: return -1 #Task must have name
        if len(nameOfTask)>50: return -1 #Tasks name can't be longer than 50 char
        if nameOfTask in self.tasksNames: return -1 #No Task With Same Name
        
        DoneBut = QPushButton('Done !')
        DoneBut.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        DoneBut.clicked.connect(lambda: self.DeleteTask(DoneBut, mainBut, nameOfTask))
        
        taskWin = TaskWindow(nameOfTask)  #Create window for task
            
        mainBut = QPushButton(nameOfTask)
        mainBut.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainBut.clicked.connect(lambda: taskWin.show())
        
        self.layout.addWidget(DoneBut, self.row, 1)
        self.layout.addWidget(mainBut,self.row, 0)
        
        self.row+=1
        self.tasksNames.append(nameOfTask) #Adds Task Name To List
        
        #self.adjustSize() #Resizes Window
        return 0
        
    def DeleteTask(self,DoneBut,taskButton, nameOfTask:str):
        """Deletes task

        Args:
            DoneBut (_type_): Button With "Done !" Description
            mainBut (_type_): Button With Task Name
        """
        DoneBut.deleteLater()
        taskButton.deleteLater()
        
        self.tasksNames.remove(nameOfTask) #Removes Task Name To List
        
        #self.adjustSize() #Resizes Window
        
        
class TaskWindow(QWidget):
    def __init__(self, taskName: str):
        super().__init__()
        self.setWindowTitle(taskName)
        self.setStyleSheet('background-color:black; color:white')
        
        layout = QVBoxLayout()
        
        textHolder = QTextEdit()
        textHolder.setStyleSheet('border: 1px solid white')
        layout.addWidget(textHolder)
        
        self.setLayout(layout)
        
        
window = App()
window.show()
app.exec()