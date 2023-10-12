import sys
from PySide6.QtWidgets import *

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me !")
        
        self.setCentralWidget(button)
        
app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()