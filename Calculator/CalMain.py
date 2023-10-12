from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys


class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        
        self.c = 0
        self.but = ''
        self.suma1 = ''
        self.suma2 = ''
        self.x = ''
        
        lay = QVBoxLayout()
        
        self.Holder = QLineEdit()
        lay.addWidget(self.Holder)
        
        #Row 1
        layRow1 = QHBoxLayout()
            
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

        lay.addLayout(layRow1)
        
        
        
        #Row 2
        layRow2 = QHBoxLayout()
        
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
        
        lay.addLayout(layRow2)
        
        
        
        #Row 3
        layRow3 = QHBoxLayout()
        
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
        
        but16 = QPushButton("C")
        but16.clicked.connect(lambda:self.Meine(but16.text()))
        layRow5.addWidget(but16)
        
        but17 = QPushButton("Back")
        but17.clicked.connect(lambda:self.Meine(but17.text()))
        layRow5.addWidget(but17)
        
        but18 = QPushButton("=")
        but18.clicked.connect(lambda:self.Meine(but18.text()))
        layRow5.addWidget(but18)
        
        lay.addLayout(layRow5)
        
        self.setLayout(lay)
        
    def ButTxt(self, data):
        print(data)
        
    def Meine(self, n):
        self.suma1 = str(self.suma1)
        self.suma2 = str(self.suma2)
        
        if n=="C":
            self.c = 0
            self.suma1 = ''
            self.suma2 = ''
            self.but = ''
            self.Holder.setText(f'')
            return
        
        if n=="=" and self.but:
            if len(self.suma2)>0:
                self.suma2 = float(self.suma2)
            else:
                self.suma2=0
                if self.suma2==0 and self.but=='/':
                    self.dev0()
                    return
            print(round(eval(f'{self.suma1}{self.but}{self.suma2}'), 5))
            suma = round(eval(f"{self.suma1}{self.but}{self.suma2}"), 5)
            self.Holder.setText(f'{self.suma1} {self.but} {self.suma2} = {suma}')
            self.suma1 = suma
            self.suma2 = ''
            self.but = ''
            return
        
        if n in "+-/*":
            self.c = 1
            self.but = n
            self.suma1 = float(self.suma1)
        
        if self.c==0 and n not in "+-/*=":
            if n=="Back":
                if len(self.suma1)>1:
                    self.suma1 = "".join([_ for _ in self.suma1].pop())
                else:
                    self.suma1=0
            elif n =='lsn':
                if int(self.suma1)>0:
                    temp = [_ for _ in self.suma1]
                    temp.insert(0, '-')
                    self.suma1="".join(temp)
                    print(temp)
                else:
                    temp = [_ for _ in self.suma1]
                    temp.pop(0)
                    self.suma1="".join(temp)
                    print(temp)
            else:
                self.suma1+=n
            
        if self.c==1 and n not in "+-/*=":
            if self.but=='/' and n=='0':
                self.dev0()
                return
                
            if n=="Back":
                if len(self.suma2)>1:
                    self.suma2 = "".join([_ for _ in self.suma2].pop())
                else:
                    self.suma2=0
            elif n =='lsn':
                if int(self.suma2)>0:
                    temp = [_ for _ in self.suma2]
                    temp.insert(0, '-')
                    self.suma2="".join(temp)
                    print(temp)
                else:
                    temp = [_ for _ in self.suma2]
                    temp.pop(0)
                    self.suma2="".join(temp)
                    print(temp)
            else:
                self.suma2+=n
            
        self.x = f'{self.suma1} {self.but} {self.suma2} = '
        self.Holder.setText(self.x)
        
    def dev0(self):
        message = QMessageBox()
        message.setWindowTitle("Bro...")
        message.setInformativeText("U can't devide by 0 :/")
        ret = message.exec()
        
        
app = QApplication(sys.argv)
window = Calc()
window.show()
app.exec()
        