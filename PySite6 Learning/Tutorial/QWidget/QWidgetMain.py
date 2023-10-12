import sys
from PySide6.QtWidgets import *
from RockWidget import RocWid

app = QApplication(sys.argv)
window = RocWid()
window.show()
app.exec()