from PySide6.QtWidgets import QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QMainWindow, QWidget, QHBoxLayout

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
        for a in range(8):
            indx = 0
            for b in range(8):
                if row==1 or row==6:
                    mainLayout.addWidget(QPushButton('i'), row, indx)
                    indx+=1
                    continue
                mainLayout.addWidget(QPushButton(), row, indx)
                indx+=1
            row+=1
            
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
            
            
            
if __name__=="__main__":
    app = QApplication()
    
    win = Chess__()
    win.show()
    
    app.exec()
                
            
            
            