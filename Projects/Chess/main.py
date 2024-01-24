from PySide6.QtWidgets import QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QMainWindow, QWidget, QHBoxLayout
from PySide6.QtGui import QFont

class Chess__(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        
        self.UI_()
        
    def UI_(self):
        mainWidget = QWidget()
        mainLayout = QGridLayout()
        
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        
        row = 0
        nigg = []
        whites = []
        
        for a in range(8):
            indx = 0
            for b in range(8):
                but = QPushButton()
                color = "color: black;"
                
                if row>=6:
                    if row==6:
                        but = Pionek__('white')
                    color = "color: white;" 
                    whites.append(but)
                elif row<=2: 
                    if row==2:
                        but = Pionek__('black')
                    nigg.append(but)
                
                
                if row%2==0:
                    if indx%2!=0:
                        temp = 'QPushButton {background-color: grey;}'
                    else:
                        temp = 'QPushButton {background-color: green;}'
                    but.setStyleSheet(temp[:-1]+color+temp[-1])
                else:
                    if indx%2!=0:but.setStyleSheet('QPushButton {background-color: green;}')
                    else:but.setStyleSheet('QPushButton {background-color: grey;}')
                
                if row==2 or row==6:
                    but.setText('i')

                mainLayout.addWidget(but, row, indx)
                indx+=1
            row+=1
            
        print(nigg)
        print(whites)
            
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
            
        #self.Game_()
        
    #def Game_():
        #while 1:
        #    while 1:
                
            
            
class Pionek__(QPushButton):
    def __init__(self, color):
        super().__init__()
        self.color = color
         
if __name__=="__main__":
    app = QApplication()
    
    win = Chess__()
    win.show()
    
    app.exec()
                
            
            
            