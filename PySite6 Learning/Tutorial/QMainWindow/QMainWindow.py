import sys
from PySide6.QtWidgets import *
from window import MainWin


app = QApplication(sys.argv)
window = MainWin(app)
window.show()
app.exec()