from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QTabWidget, QLineEdit, QPushButton, QGridLayout
from PySide6.QtCore import Qt, QTimer
from PySide6 import QtCore
import time
import functools
import threading

class CountDownWindow(QWidget):
    
    timer_updated = QtCore.Signal(str)
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stoper')
        self.setGeometry(200, 200, 350, 200)
        self.arr = [0,0,0,0,0,0]
        self.indx = 5
        
        self.MainUI_()
        
        
    def MainUI_(self):
        TabWidget = QTabWidget(self)
        
        self.SelectTime = QWidget()
        Counter = QWidget()
        
        CounterLayout = QVBoxLayout()
        
        self.timerLabel = QLabel('00h 00m 00s')
        self.timer_updated.connect(self.SetTimeForStopper_) # connect signal to slot
        CounterLayout.addWidget(self.timerLabel)
        startTimerButton = QPushButton('Start Timer')
        startTimerButton.clicked.connect(lambda: self.TempFunc_())
        CounterLayout.addWidget(startTimerButton)
        
        Counter.setLayout(CounterLayout)
        
        self. SelectTimeUI_() #Creates Select Time Tab UI
        
        TabWidget.addTab(self.SelectTime,"Set Counter")
        TabWidget.addTab(Counter,"Counter")
        
    def TempFunc_(self):
        t1 = threading.Thread(target=self.StartTimer_)
        t1.start()
        QTimer.singleShot(0, t1.join) # join thread after starting
            
        
    def SelectTimeUI_(self):
        SelectTimeLayout = QGridLayout()
        
        self.TimeEdit = QLineEdit(f'00h 00m 00s')
        SelectTimeLayout.addWidget(self.TimeEdit, 0, 0)
        
        self.butRow = 0
        self.down = 1
        self.backIndx = 0
        
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
        sumbmitButton = QPushButton('Sumbmit')
        sumbmitButton.clicked.connect(self.SetTimeForStopper_())
        
        SelectTimeLayout.addWidget(sumbmitButton)
        
        self.SelectTime.setLayout(SelectTimeLayout)
        
        
    def UpDateTime_(self, num):
        if num=='Back':
            self.arr[self.backIndx] = 0
            self.TimeEdit.setText(f'{self.arr[5]}{self.arr[4]}h {self.arr[3]}{self.arr[2]}m {self.arr[1]}{self.arr[0]}s')
            self.backIndx-=1
            return 0
        self.backIndx = 5
        
        if num=='Trash':
            self.arr = [0,0,0,0,0,0]
            self.TimeEdit.setText(f'{self.arr[5]}{self.arr[4]}h {self.arr[3]}{self.arr[2]}m {self.arr[1]}{self.arr[0]}s')
            return 0
        
        if len(self.arr)<7:
            self.arr = self.arr[:-1]
            self.arr.insert(0,int(num))
        
        print(self.arr)
        
        self.TimeEdit.setText(f'{self.arr[5]}{self.arr[4]}h {self.arr[3]}{self.arr[2]}m {self.arr[1]}{self.arr[0]}s')
        self.indx+=1
        
    def SetTimeForStopper_(self):
        text = f'{self.arr[5]}{self.arr[4]}h {self.arr[3]}{self.arr[2]}m {self.arr[1]}{self.arr[0]}s'
        self.timer_updated.emit(text)
        
    def SetSecounds_(self, sec: int):
        secounds = str(sec-1)
        if len(secounds)==2:
            self.arr[1] = int(secounds[0])
            self.arr[0] = int(secounds[1])
        else:
            self.arr[1] = 0
            self.arr[0] = int(secounds[0])
            
        self.timerLabel.setText(f'1')
        self.SetTimeForStopper_()
        
    def SetMinutes_(self, min: int):
        minutes = str(min-1)
        if len(minutes)==2:
            self.arr[3] = int(minutes[0])
            self.arr[2] = int(minutes[1])
        else:
            self.arr[3] = 0
            self.arr[2] = int(minutes[0])
        
        self.SetSecounds_(60)
        
    def SetHours_(self, hour:int):
        hours = str(hour-1)
        if len(hours)==2:
            self.arr[5] = int(hours[0])
            self.arr[4] = int(hours[1])
        else:
            self.arr[5] = 0
            self.arr[4] = int(hours[0])
        
        self.SetMinutes_(59)
        
    def StartTimer_(self):
        print('start')
        
        while 1:
            hours = int(f'{self.arr[5]}{self.arr[4]}')
            minutes = int(f'{self.arr[3]}{self.arr[2]}')
            seconds = int(f'{self.arr[1]}{self.arr[0]}')
            
            print(f'Before: {hours, minutes, seconds}')
            
            if seconds > 0:
                self.SetSecounds_(seconds)
            else:
                if minutes > 0:
                    self.SetMinutes_(minutes)
                else:
                    if hours > 0:
                        self.SetHours_(hours)
                
            print(f'After: {hours, minutes, seconds}')
            self.timer_updated.emit(self.timerLabel.text()) # emit signal to update label
            time.sleep(1)
        
if __name__ == "__main__":
    app = QApplication()
    CounterAppWindow = CountDownWindow()
    CounterAppWindow.show()
    app.exec()
        
        