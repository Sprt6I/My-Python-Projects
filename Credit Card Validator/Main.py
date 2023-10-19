from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import QtGui
import sys


class Val(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Credit Card Validator")

        lay = QGridLayout()

        self.textEdit = QLineEdit()
        lay.addWidget(self.textEdit)

        but = QPushButton("Validate")
        but.clicked.connect(lambda: self.Validate(self.textEdit.text()))
        lay.addWidget(but)

        self.setLayout(lay)

    def Validate(self, number):
        if len(number)>50:return -1 #Check Len
        for _ in number: #Check If Number (Spaces are ok too)
            if _ not in '1234567890 ':
                return -1
         
        number = [_ for _ in number if _!=' ']   #Delete Space
        EverySecNum = []
        i = 1
        for _ in number[::-1]: #Takes every secound num from number
            if i%2==0:
                EverySecNum.append(_)
            i+=1
        EverySecNum = ''.join([str(int(_)*2) for _ in EverySecNum])
        EverySecNum = [_ for _ in EverySecNum]
        print(number)
        print(EverySecNum)
        EverySecNumSum = sum([int(_) for _ in EverySecNum])
        print(EverySecNumSum)
        
        EverySecNumOdd = []
        i = 1
        for _ in number[::-1]: #Takes every secound num from number
            if i%2==0 and int(_)%2!=0:
                EverySecNumOdd.append(_)
            i+=1
        print(EverySecNumOdd)
        EverySecNumOddSum = sum([int(_) for _ in EverySecNumOdd])
        print(EverySecNumOddSum + EverySecNumSum)
            
            

        
        
            
        
        
app = QApplication(sys.argv)
window = Val()
window.show()
app.exec()
