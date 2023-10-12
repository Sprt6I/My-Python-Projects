import sys
from PySide6.QtWidgets import *

class IDK(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        lay1 = QGridLayout()


        #lay1.addWidget(QPushButton("Button at (0, 0)"), 0, 0)
        #lay1.addWidget(QPushButton("Button at (0, 1)"), 0, 1)
        #lay1.addWidget(QPushButton("Button Spans two Cols"), 1, 0, 1, 2)
        
        
        label = QLabel("Full Name: ")
        lay1.addWidget(label, 0, 0)
        
        self.lineEdit = QLineEdit()
        self.lineEdit.textChanged.connect(self.txtChanged)
        lay1.addWidget(self.lineEdit,0, 1, 1, 2)
        
        but1 = QPushButton("Grab Data")
        but1.clicked.connect(self.grabDat)
        lay1.addWidget(but1,1, 0, 1, 3)
        
        self.message = QLabel("")
        lay1.addWidget(self.message, 2, 0, 1,2)
        
        
        self.setLayout(lay1)
        
    def grabDat(self):
        print(f"FullName: {self.lineEdit.text()}")
        self.message.setText(self.lineEdit.text())
        
    def txtChanged(self):
        self.message.setText(self.lineEdit.text())

app = QApplication(sys.argv)
window = IDK()
window.show()
app.exec()