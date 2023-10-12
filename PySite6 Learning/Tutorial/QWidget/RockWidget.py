import sys
from PySide6.QtWidgets import *

class RocWid(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        lay0 = QVBoxLayout()
        
        label = QLabel("Hehehe")
        lay0.addWidget(label)
        
        lay1 = QGridLayout()
        
        but1 = QPushButton("Button1")
        lay1.addWidget(but1, 1,1)
        
        but2 = QPushButton("Button2")
        lay1.addWidget(but2, 1,2)
        
        but2 = QPushButton("Button3")
        lay1.addWidget(but2, 5, 0)
        
        but2 = QPushButton("Button4")
        lay1.addWidget(but2, 3, 2)
        
        
        
        lay0.addLayout(lay1)
        
        self.setLayout(lay0)
