import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
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
    super(MainApp__, self).__init__()
    
    self.setWindowTitle("Some App ?!")
    
    self.UI_()
    
  def UI_(self):
    widget = QWidget()
    layout1 = QHBoxLayout()
    layout2 = QVBoxLayout()
    layout3 = QVBoxLayout()
    
    layout1.setContentsMargins(0,0,0,0)
    layout1.setSpacing(0)

    layout2.addWidget(Color__('red'))
    layout2.addWidget(Color__('yellow'))
    layout2.addWidget(Color__('purple'))

    layout1.addLayout( layout2 )

    layout1.addWidget(Color__('green'))

    layout3.addWidget(Color__('red'))
    layout3.addWidget(Color__('purple'))

    layout1.addLayout( layout3 )
    layout1.addLayout(layout2)

    widget = QWidget()
    widget.setLayout(layout1)
    self.setCentralWidget(widget)
    
    
    #widget.setLayout(layoutMain)
    
    #self.setCentralWidget(widget)

    
if __name__=="__main__":
  app = QApplication(sys.argv)
  
  win = MainApp__()
  win.show()
  
  app.exec()