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
        self.setStyleSheet('color:white; background-color:black;')
        self.Player = 0
        
        #Array For Storing How Match Goes (Changes Nums to X/O When Button Clicked)
        self.arr = [[0,1,2],
                    [3,4,5],
                    [6,7,8]]
        
        #Create Font That Can Resize
        font = QFont()
        font.setPointSize(20)
        
        #Create Layout
        lay = QGridLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        
        
        ''' SET UP BUTTONS'''
        #1. Create Button
        #2. Set Expanding Policy so it resizes
        #3. Set font (so it can resize too)
        #4. Connect Function to button
        #5. Add Button
        
        but1 = QPushButton(text=None)       #1
        but1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)    #2
        but1.setFont(font)      #3
        but1.clicked.connect(lambda: self.Clic(but1, 0, 0))     #4
        lay.addWidget(but1, 0,0) #5
        
        but2 = QPushButton()
        but2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but2.setFont(font)
        but2.clicked.connect(lambda: self.Clic(but2, 0, 1))
        lay.addWidget(but2, 0,1)
        
        but3 = QPushButton()
        but3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but3.setFont(font)
        but3.clicked.connect(lambda: self.Clic(but3, 0, 2))
        lay.addWidget(but3, 0,2)
        
        but4 = QPushButton()
        but4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but4.setFont(font)
        but4.clicked.connect(lambda: self.Clic(but4, 1, 0))
        lay.addWidget(but4, 1,0)
        
        but5 = QPushButton()
        but5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but5.setFont(font)
        but5.clicked.connect(lambda: self.Clic(but5, 1, 1))
        lay.addWidget(but5, 1,1)
        
        but6 = QPushButton()
        but6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but6.setFont(font)
        but6.clicked.connect(lambda: self.Clic(but6, 1, 2))
        lay.addWidget(but6, 1,2)
        
        but7 = QPushButton()
        but7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but7.setFont(font)
        but7.clicked.connect(lambda: self.Clic(but7, 2, 0))
        lay.addWidget(but7, 2,0)
        
        but8 = QPushButton()
        but8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but8.setFont(font)
        but8.clicked.connect(lambda: self.Clic(but8, 2,1))
        lay.addWidget(but8, 2,1)
        
        but9 = QPushButton()
        but9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        but9.setFont(font)
        but9.clicked.connect(lambda: self.Clic(but9, 2, 2))
        lay.addWidget(but9, 2,2)

        self.setLayout(lay)
        
    def Clic(self, data,Row, indx): #Fucntion Called When Button Clicked
        if self.Player%2!=0 and data.text() == '': #Checks if variable self.Player%2 not equall to zero if so its player 2 move else it's player's 1
            data.setText('X') #Changes Button Text
            self.arr[Row][indx] = 'X' #Changes Array
            self.Check() #Checks If Someone Wins
            self.Player+=1
            
        elif self.Player%2==0 and data.text() == '':
            data.setText('O') #Changes Button Text
            self.arr[Row][indx] = 'O' #Changes Array
            self.Check() #Checks If Someone Wins
            self.Player+=1
        
    def Check(self):
        VerticalCheck0 = ''
        VerticalCheck1 = ''
        VerticalCheck2 = ''
        
        HorizontalCheck0 = ''
        
        for _ in self.arr: #Checks Vertical lines
           VerticalCheck0 +=str(_[0]) #Line 1
           VerticalCheck1 +=str(_[1]) #2
           VerticalCheck2 += str(_[2])#3
           
        #Checks Horizontal Lines
        HorizontalCheck0 = ''.join([str(_) for _ in self.arr[0]]) #Line 1
        HorizontalCheck1 = ''.join([str(_) for _ in self.arr[1]]) #2
        HorizontalCheck2 = ''.join([str(_) for _ in self.arr[2]]) #3

        if VerticalCheck0=='XXX' or VerticalCheck1=='XXX' or VerticalCheck2=='XXX' or HorizontalCheck0=='XXX' or HorizontalCheck1=='XXX' or HorizontalCheck2=='XXX' or (VerticalCheck0[2]=='X' and VerticalCheck1[1]=='X' and VerticalCheck2[0]=='X') or (VerticalCheck0[0]=='X' and VerticalCheck1[1]=='X' and VerticalCheck2[2]=='X'):
            self.EndMess("Player 1 (X) Wins !!!")
 
        elif VerticalCheck0=='OOO' or VerticalCheck1=='OOO' or VerticalCheck2=='OOO'  or HorizontalCheck0=='OOO' or HorizontalCheck1=='OOO' or HorizontalCheck2=='OOO' or (VerticalCheck0[2]=='O' and VerticalCheck1[1]=='O' and VerticalCheck2[0]=='O') or (VerticalCheck0[0]=='O' and VerticalCheck1[1]=='O' and VerticalCheck2[2]=='O'):
            self.EndMess("Player 2 (O) Wins !!!")
            
    def EndMess(self, txt): #Shows End Game Message
        mess = QMessageBox(text=txt)
        mess.setStyleSheet('color:white; background-color:black;')
        mess.setWindowTitle = "Game Ends!"
        mess.exec()
        app.quit()
            
        

window = Tic()
window.show()
app.exec()