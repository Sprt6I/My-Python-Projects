from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QTabWidget, QLineEdit, QPushButton, QGridLayout
from PySide6.QtCore import Qt, QTimer
from PySide6 import QtCore
import time
import functools

class CountDownWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stopper')
        self.arr = [0,0,0,0,0,0]
        self.indx = 0
        
        self.UI_()
        
        
    def UI_(self):
        TabWidget = QTabWidget(self)
        
        SelectTime = QWidget()
        Counter = QWidget()
        
        SelectTimeLayout = QGridLayout()
        CounterLayout = QVBoxLayout()
        
        """ SETTING SELECT TIMER TAB """
        
        self.TimeEdit = QLineEdit(f'00h 00m 00s')
        SelectTimeLayout.addWidget(self.TimeEdit, 0, 0)
        
        self.butRow = 0
        self.down = 1
        
        namesArr = [1,2,3,4,5,6,7,8,9,'Trash',0,'Back']
        
        for i in namesArr:
            globals()[f'but{i}'] = QPushButton(str(i))
            eval(f'but{i}').clicked.connect(functools.partial(self.UpDateTime_, i))
            SelectTimeLayout.addWidget(eval(f'but{i}'), self.down, self.butRow)
            print(i)
            print(f'but{i}')
            print(eval(f'but{i}'))
            
            self.butRow+=1
            if self.butRow==3:
                self.butRow=0
                self.down+=1
        
        '''
        button1 = QPushButton('Trash')
        button1 = QPushButton('0')
        button1 = QPushButton('Back')
        '''
        
        SelectTime.setLayout(SelectTimeLayout)
        
        
        TabWidget.addTab(SelectTime,"Set Counter")
        TabWidget.addTab(Counter,"Counter")
        
    def UpDateTime_(self, num):
        if num=='Back':
            #self.arr[self.arr.index(0)+1] = 0
            self.TimeEdit.setText(f'{self.arr[5]}{self.arr[4]}h {self.arr[3]}{self.arr[2]}m {self.arr[1]}{self.arr[0]}s')
            return 0
        if len(self.arr)<7:
            self.arr = self.arr[:-1]
            self.arr.insert(0,int(num))
        
        print(self.arr)
        
        self.TimeEdit.setText(f'{self.arr[5]}{self.arr[4]}h {self.arr[3]}{self.arr[2]}m {self.arr[1]}{self.arr[0]}s')
        self.indx+=1
        
        
if __name__ == "__main__":
    app = QApplication()
    CounterAppWindow = CountDownWindow()
    CounterAppWindow.show()
    app.exec()
        
        