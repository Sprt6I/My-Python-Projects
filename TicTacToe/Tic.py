from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import QtGui
import sys


app = QApplication(sys.argv)
app.setStyleSheet (
    'QGridLayout {margin:0;padding:0}'
    'QPushButton {background-color: black;color:white;border:1px solid white;margin:0px;padding:0px;}'
)

class Tic(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TicTacToe")
        self.Player = 0
        
        self.arr = [[0,1,2],
                    [3,4,5],
                    [6,7,8]]
        
        lay = QGridLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        
        but1 = QPushButton(text=None)
        but1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but1.clicked.connect(lambda: self.Clic(but1, 0, 0))
        lay.addWidget(but1, 0,0)
        
        but2 = QPushButton()
        but2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but2.clicked.connect(lambda: self.Clic(but2, 0, 1))
        lay.addWidget(but2, 0,1)
        
        but3 = QPushButton()
        but3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but3.clicked.connect(lambda: self.Clic(but3, 0, 2))
        lay.addWidget(but3, 0,2)
        
        but4 = QPushButton()
        but4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but4.clicked.connect(lambda: self.Clic(but4, 1, 0))
        lay.addWidget(but4, 1,0)
        
        but5 = QPushButton()
        but5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but5.clicked.connect(lambda: self.Clic(but5, 1, 1))
        lay.addWidget(but5, 1,1)
        
        but6 = QPushButton()
        but6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but6.clicked.connect(lambda: self.Clic(but6, 1, 2))
        lay.addWidget(but6, 1,2)
        
        but7 = QPushButton()
        but7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but7.clicked.connect(lambda: self.Clic(but7, 2, 0))
        lay.addWidget(but7, 2,0)
        
        but8 = QPushButton()
        but8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but8.clicked.connect(lambda: self.Clic(but8, 2,1))
        lay.addWidget(but8, 2,1)
        
        but9 = QPushButton()
        but9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but9.clicked.connect(lambda: self.Clic(but9, 2, 2))
        lay.addWidget(but9, 2,2)

        self.setLayout(lay)
        
    def Clic(self, data,Row, indx):
        if self.Player%2!=0 and data.text() == '':
            data.setText('X')
            self.arr[Row][indx] = 'X'
        elif self.Player%2==0 and data.text() == '':
            data.setText('O')
            self.arr[Row][indx] = 'O'
        self.Player+=1
        print(self.arr)
        
    def Check(self):
        pass
        

window = Tic()
window.show()
app.exec()