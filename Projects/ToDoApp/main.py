from PySide6.QtWidgets import QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
import sys


class MainAppWindow(QWidget):
    
    __slots__ = ["layout", "row", "tasksNames", 'taskWin']
    
    def __init__(self): #Sets Up All Variables And 'Configurate' Layout
        super().__init__()
        
        self.setWindowTitle('To Do')
        self.setStyleSheet('background-color:black;color:white;font-size: 16pt;')
        self.layout = QGridLayout()
        
        self.layout.setContentsMargins(0, 0, 0, 0) #Sets margin to 0 and strech button to task name in 1/4
        self.layout.setColumnStretch(0, 4)
        self.layout.setColumnStretch(1, 1)
        
        self.row = 1 #Number Of Row To Add Task
        self.tasksNames = [] #Names Of Task Added
        
        self.AddUI_()
        
    def AddUI_(self): #Adds UI For App
        
        AddTaskNameInput = QLineEdit() #Input For Task Name
        AddTaskNameInput.setFixedHeight(50)
        AddTaskNameInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout.addWidget(AddTaskNameInput,0,0)
        
        AddTaskBut = QPushButton('AddTask') #Button To Add Tasks
        AddTaskBut.setFixedHeight(50)
        AddTaskBut.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        AddTaskBut.clicked.connect(lambda: self.addTask_(AddTaskNameInput.text()))
        self.layout.addWidget(AddTaskBut,0,1)
        
        self.setLayout(self.layout)
        
    def addTask_(self,nameOfTask: str) -> int:
        """Adds Task

        Args:
            nameOfTask (str): Name Of Task To Add

        Returns:
            int: 0 if everyhing is correct else -1
        """
        if not nameOfTask: return -1 #Task must have name
        if len(nameOfTask)>50: return -1 #Tasks name can't be longer than 50 char
        if nameOfTask in self.tasksNames: return -1 #No Task With Same Name
        
        DoneBut = QPushButton('Done !') #Button For Deleting Task
        DoneBut.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        DoneBut.clicked.connect(lambda: self.DeleteTask_(DoneBut, mainBut, nameOfTask))
        
        taskWin = TaskWindow(nameOfTask)  #Create window for task
            
        mainBut = QPushButton(nameOfTask) #Button With Task Name (When clicked shows window with space to add description)
        mainBut.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainBut.clicked.connect(lambda: taskWin.show())
        
        self.layout.addWidget(DoneBut, self.row, 1)
        self.layout.addWidget(mainBut,self.row, 0)
        
        self.row+=1
        self.tasksNames.append(nameOfTask) #Adds Task Name To List
        
        return 0
        
    def DeleteTask_(self,DoneBut,taskButton, nameOfTask:str):
        """Deletes task

        Args:
            DoneBut (_type_): Button With "Done !" Description
            mainBut (_type_): Button With Task Name
        """
        DoneBut.deleteLater()
        taskButton.deleteLater()
        
        self.tasksNames.remove(nameOfTask) #Removes Task Name To List
        
        
class TaskWindow(QWidget): #Window Containig Space For Task Description Showing When Task Button Clickedv
    
    __slots__ = ["layout"]
    
    def __init__(self, taskName: str):
        super().__init__()
        self.setWindowTitle(taskName)
        self.setStyleSheet('background-color:black; color:white')
        
        self.layout = QVBoxLayout()
        
        self.setUI_()
        
    def setUI_(self):
        DescriptionForTask = QTextEdit()
        DescriptionForTask.setStyleSheet('border: 1px solid white')
        self.layout.addWidget(DescriptionForTask)
        
        self.setLayout(self.layout)
   
        
if __name__ == "__main__":   
    app = QApplication(sys.argv)

    app.setStyleSheet (
        'QLineEdit {border: 1px solid white; color:white; background-color:black}'
        'QPushButton {border: 1px solid white; color:white; background-color:black;}'
    ) 
        
    TaskApp = MainAppWindow()
    TaskApp.show()
    app.exec()