from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QTabWidget, QLineEdit, QPushButton, QGridLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QRegion
import functools

app = QApplication()
app.setStyleSheet(
    "QTabWidget {background-color: transparent;}"
    'QTabWidget::pane {border: 1px solid white;}'  # Set the border color of QTabWidget
    'QTabBar::tab {background-color: black;color:white; border: 1px solid white; padding: 8px;}'  # Set text color and background color for tabs
    'QPushButton {color:white; background-color: rgba(255, 255, 255, 10%); border: 1px solid white;}'
    'QLabel {color:white; background-color:transparent}'
    'QLineEdit {color:white; background-color:transparent; border: 1px solid white;}'
)

class CountDownWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stoper')
        self.setGeometry(200, 200, 350, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.arr = [0,0,0,0,0,0]
        self.indx = 5
        
        self.MainUI_()
        
        
        
    def MainUI_(self):
        TabWidget = QTabWidget(self)
        
        
        self.SelectTime = QWidget()
        self.Counter = QWidget()

        self.CounterUI_() #Creates Counter Tab UI
        
        self.SelectTimeUI_() #Creates Set Counter Tab UI
        
        TabWidget.addTab(self.SelectTime,"Set Counter")
        TabWidget.addTab(self.Counter,"Counter")
        
        
        
    def ClockFunc_(self): #Update QLabel (text) In Stopper
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.StartTimer_)
        self.timer.start(1000)
            
            
            
    def CounterUI_(self): # Sets UI For 'Counter' Tab In App
        CounterLayout = QVBoxLayout()
        
        
        self.timerLabel = QLabel('00h 00m 00s')
        CounterLayout.addWidget(self.timerLabel)
        
        startTimerButton = QPushButton('Start Timer')
        startTimerButton.setMask(QRegion(0, 0, startTimerButton.width(), startTimerButton.height(), QRegion.Rectangle))
        startTimerButton.clicked.connect(lambda: self.ClockFunc_())
        CounterLayout.addWidget(startTimerButton)
        
        self.Counter.setLayout(CounterLayout)
        
        
        
    def SelectTimeUI_(self): # Sets UI For 'Set Counter' Tab In App
        SelectTimeLayout = QGridLayout()
        
        self.TimeEdit = QLineEdit(f'00h 00m 00s')
        SelectTimeLayout.addWidget(self.TimeEdit, 0, 0)
        
        sumbmitButton = QPushButton('Sumbmit')
        SelectTimeLayout.addWidget(sumbmitButton, 0, 1)
        
        self.butRow = 0
        self.down = 1
        self.backIndx = 0
        
        namesArr = [1,2,3,4,5,6,7,8,9,'Trash',0,'Back']
        
        for i in namesArr:
            globals()[f'but{i}'] = QPushButton(str(i))
            eval(f'but{i}').clicked.connect(functools.partial(self.UpDateTime_, i))
            SelectTimeLayout.addWidget(eval(f'but{i}'), self.down, self.butRow)
            #print(i)
            #print(f'but{i}')
            #print(eval(f'but{i}'))
            
            self.butRow+=1
            if self.butRow==3:
                self.butRow=0
                self.down+=1
        
        self.SelectTime.setLayout(SelectTimeLayout)
        
        
        
    def UpDateTime_(self, num): #Sets Time
        """ FUNCTION FOR "Set Counter" TAB """
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
        
        #print(self.arr)
        
        self.TimeEdit.setText(f'{self.arr[5]}{self.arr[4]}h {self.arr[3]}{self.arr[2]}m {self.arr[1]}{self.arr[0]}s')
        self.indx+=1
        
        
        
    def SetSecounds_(self, sec: int): #Calculate Secounds
        secounds = str(sec-1)
        if len(secounds)==2:
            self.arr[1] = int(secounds[0])
            self.arr[0] = int(secounds[1])
        else:
            self.arr[1] = 0
            self.arr[0] = int(secounds[0])
            
        self.timerLabel.setText(f'{self.arr[5]}{self.arr[4]}h {self.arr[3]}{self.arr[2]}m {self.arr[1]}{self.arr[0]}s')
        
        
        
    def SetMinutes_(self, min: int): #Calculate Minutes
        minutes = str(min-1)
        if len(minutes)==2:
            self.arr[3] = int(minutes[0])
            self.arr[2] = int(minutes[1])
        else:
            self.arr[3] = 0
            self.arr[2] = int(minutes[0])
        
        self.SetSecounds_(60)
        
        
        
    def SetHours_(self, hour:int): #Calculate Hours
        hours = str(hour-1)
        if len(hours)==2:
            self.arr[5] = int(hours[0])
            self.arr[4] = int(hours[1])
        else:
            self.arr[5] = 0
            self.arr[4] = int(hours[0])
        
        self.SetMinutes_(59)
        
        
        
    def StartTimer_(self):
        """ FUNCTION FOR "Counter" TAB (RUNS STOPER)"""
        hours = int(f'{self.arr[5]}{self.arr[4]}')
        minutes = int(f'{self.arr[3]}{self.arr[2]}')
        seconds = int(f'{self.arr[1]}{self.arr[0]}')
        if hours>60:
            hours = 60
        if minutes>60:
            minutes = 60
        if seconds>60:
            seconds = 60
        
        #print(f'Before: {hours, minutes, seconds}')
        
        if seconds > 0:
            self.SetSecounds_(seconds)
        else:
            if minutes > 0:
                self.SetMinutes_(minutes)
            else:
                if hours > 0:
                    self.SetHours_(hours)
            
        #print(f'After: {hours, minutes, seconds}')
        
        if hours+minutes+seconds<=0:
            print("END")
            exit()
        
        
        
if __name__ == "__main__":
    CounterAppWindow = CountDownWindow()
    CounterAppWindow.show()
    app.exec()
        
        