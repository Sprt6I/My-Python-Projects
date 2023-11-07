from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

app = QApplication(sys.argv)
app.setStyleSheet(
    'QVBoxLayout {margin:0px;padding:0px;}'
    'QHBoxLayout {margin:0px; padding:0px;}'
    'QPushButton {height:55%;background-color: black;color:white;border:1px solid white;margin:0px;padding:0px;}'
)

class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color:black; color: white;margin:0;padding:0;")
        #self.setGeometry(900,500,180,180)
        self.setFixedSize(340,340)
        
        self.dragging = False
        self.symbol = ''
        self.num1 = ''
        self.num2 = ''
        
        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        #lay.setStretch(0, 0)

        
        self.Holder = QLineEdit()
        self.Holder.setStyleSheet("height:55%;margin:0px;padding:0px;font:20px;")
        self.Holder.setReadOnly(True)
        lay.addWidget(self.Holder)
        
        #Row 1
        layRow1 = QHBoxLayout()
        layRow1.setSpacing(0)
        layRow1.setContentsMargins(0, 0, 0, 0)
            
        but0 = QPushButton("7")
        but0.clicked.connect(lambda:self.Meine(but0.text()))
        layRow1.addWidget(but0)
        
        but1 = QPushButton("8")
        but1.clicked.connect(lambda:self.Meine(but1.text()))
        layRow1.addWidget(but1)
        
        but2 = QPushButton("9")
        but2.clicked.connect(lambda:self.Meine(but2.text()))
        layRow1.addWidget(but2)
        
        but3 = QPushButton("/")
        but3.clicked.connect(lambda:self.Meine(but3.text()))
        layRow1.addWidget(but3)

        lay.addLayout(layRow1, 0)
        
        
        
        #Row 2
        layRow2 = QHBoxLayout()
        layRow2.setSpacing(0)
        layRow2.setContentsMargins(0,0,0,0)
        
        but4 = QPushButton("4")
        but4.clicked.connect(lambda:self.Meine(but4.text()))
        layRow2.addWidget(but4)
        
        but5 = QPushButton("5")
        but5.clicked.connect(lambda:self.Meine(but5.text()))
        layRow2.addWidget(but5)
        
        but6 = QPushButton("6")
        but6.clicked.connect(lambda:self.Meine(but6.text()))
        layRow2.addWidget(but6)
        
        but7 = QPushButton("*")
        but7.clicked.connect(lambda:self.Meine(but7.text()))
        layRow2.addWidget(but7)
        
        lay.addLayout(layRow2, 0)
        
        
        
        #Row 3
        layRow3 = QHBoxLayout()
        layRow3.setSpacing(0)
        
        but8 = QPushButton("1")
        but8.clicked.connect(lambda:self.Meine(but8.text()))
        layRow3.addWidget(but8)
        
        but9 = QPushButton("2")
        but9.clicked.connect(lambda:self.Meine(but9.text()))
        layRow3.addWidget(but9)
        
        but10 = QPushButton("3")
        but10.clicked.connect(lambda:self.Meine(but10.text()))
        layRow3.addWidget(but10)
        
        but11 = QPushButton("+")
        but11.clicked.connect(lambda:self.Meine(but11.text()))
        layRow3.addWidget(but11)
        
        lay.addLayout(layRow3)
        
        
        
        #Row 4
        layRow4 = QHBoxLayout()
        layRow4.setSpacing(0)
        
        but12 = QPushButton("+/-")
        but12.clicked.connect(lambda:self.Meine('lsn'))
        layRow4.addWidget(but12)
        
        but13 = QPushButton("0")
        but13.clicked.connect(lambda:self.Meine(but13.text()))
        layRow4.addWidget(but13)
        
        but14 = QPushButton(".")
        but14.clicked.connect(lambda:self.Meine(but14.text()))
        layRow4.addWidget(but14)
        
        but15 = QPushButton("-")
        but15.clicked.connect(lambda:self.Meine(but15.text()))
        layRow4.addWidget(but15)
        
        lay.addLayout(layRow4)
        
        
        
        #Row 5
        layRow5 = QHBoxLayout()
        layRow5.setSpacing(0)
        
        but16 = QPushButton("C")
        but16.clicked.connect(lambda:self.Meine(but16.text()))
        layRow5.addWidget(but16)
        
        but17 = QPushButton("Back")
        but17.clicked.connect(lambda:self.Meine(but17.text()))
        layRow5.addWidget(but17)
        
        but18 = QPushButton("Round")
        but18.clicked.connect(lambda:self.Meine(but18.text()))
        layRow5.addWidget(but18)
        
        but19 = QPushButton("=")
        but19.clicked.connect(lambda:self.Meine(but19.text()))
        layRow5.addWidget(but19)
        
        lay.addLayout(layRow5)
        
        self.setLayout(lay)
        
    def ButTxt(self, data):
        print(data)
        
    def Meine(self, n):
        self.num1 = str(self.num1)
        self.num2 = str(self.num2)
        
        if n=="C": #Deletes Everything
            self.Del()
            return
        
        if n=="Back":#Delete 1 char
            self.Back()
            
        if n=='lsn': #Changes number symbol: num>0: num=-num else +num
            self.LSN()
            
        if n=='Round':
            self.MyRound()
            
            
        
        if n=="=" and self.symbol: #Equals
            self.num1 = float(self.num1) if self.num1!='' else 0
            self.num2 = float(self.num2) if self.num2!='' else 0
            if self.num2==0 and self.symbol=='/': #Shows Error Message if u want to devide by 0
                self.dev0()
                return 
            suma = round(eval(f"{self.num1}{self.symbol}{self.num2}"), 5)
            self.Holder.setText(f'{self.num1} {self.symbol} {self.num2} = {suma}')
            self.num1 = suma
            self.num2 = ''
            self.symbol = ''
            return
        
        if n in "+-/*": #Sets symbol
            self.symbol = n
        
        if self.symbol=='' and n in '1234567890.': #Sets 1 number
            self.num1+=n
            
        if self.symbol!='' and n in '1234567890.': #Sets 2 Number
                self.num2+=n
            
        self.Holder.setText(f'{self.num1} {self.symbol} {self.num2} = ') #Shows Calculations
        
    def dev0(self): #Devide By 0 Error Message
        message = QMessageBox()
        message.setWindowTitle("Bro...")
        message.setInformativeText("U can't devide by 0 :/")
        ret = message.exec()
        
    def Del(self): #Sets everything to ''
        self.num1 = ''
        self.num2 = ''
        self.symbol = ''
        self.Holder.setText(f'')
        return
    
    def LSN(self):
        if self.symbol=='':
            if (float(self.num1) if self.num1!='' else 0)>0:
                temp = [_ for _ in self.num1]
                temp.insert(0, '-')
                self.num1="".join(temp)
        else:
            if (float(self.num2) if self.num2!='' else 0)>0:
                temp = [_ for _ in self.num2]
                temp.insert(0, '-')
                self.num2="".join(temp)

    
    def Back(self):
        if self.symbol=='':
            if len(self.num1)>1:
                self.num1 = "".join([_ for _ in self.num1][:-1])
            else:
                self.num1=0
        else:
            if len(self.num2)>1:
                self.num2 = "".join([_ for _ in self.num1][:-1])
            else:
                self.num2=0
                
    def MyRound(self): #Rounds the number
        if self.symbol=='':
            self.num1= str(round(float(self.num1) if self.num1!='' else 0, 2))
        else:
            self.num2 = str(round(float(self.num2) if self.num2!='' else 0, 2))
                
        
        

window = Calc()
window.show()
app.exec()
        