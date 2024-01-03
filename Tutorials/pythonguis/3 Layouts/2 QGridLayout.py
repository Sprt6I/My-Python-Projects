import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PySide6.QtGui import QPalette, QColor

class Color__(QWidget):
  def __init__(self, color):
    super(Color__, self).__init__()
    self.setAutoFillBackground(True)
    
    palette = self.palette()
    palette.setColor(QPalette.Window, QColor(color)) # type: ignore
    self.setPalette(palette)

class MainApp__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("My App?!")
    
    self.UI_()
    
  def UI_(self):
    widget = QWidget()
    layout = QGridLayout()
    
    layout.setContentsMargins(0,0,0,0)
    layout.setSpacing(0)
    
    layout.addWidget(Color__('red'), 0, 0)
    layout.addWidget(Color__('green'), 1, 0)
    layout.addWidget(Color__('blue'), 1, 1)
    layout.addWidget(Color__('purple'), 2, 1)
    
    widget.setLayout(layout)
    
    self.setCentralWidget(widget)
    
if __name__=="__main__":
  app = QApplication()
  
  win = MainApp__()
  win.show()
  
  app.exec()
