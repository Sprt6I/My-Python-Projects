import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout
from PySide6.QtGui import QPalette, QColor
from PySide6.QtGui import QMouseEvent




class Color__(QWidget):
  def __init__(self, color):
    super(Color__, self).__init__()
    self.setAutoFillBackground(True)
    
    palette = self.palette()
    palette.setColor(QPalette.Window, QColor(color)) # type: ignore
    self.setPalette(palette)
    
    



class MyApp__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("My App?")
    
    self.indx = 0
    
    self.UI_()
  
  def UI_(self):
    widget = QWidget()
    self.layout = QStackedLayout() #type: ignore
    
    self.layout.addWidget(Color__('red'))
    self.layout.addWidget(Color__('green'))
    self.layout.addWidget(Color__('blue'))
    self.layout.addWidget(Color__('yellow'))
    
    self.layout.setCurrentIndex(self.indx)
    
    widget.setLayout(self.layout)
    
    self.setCentralWidget(widget)
    
  def mousePressEvent(self, event: QMouseEvent) -> None:
    self.indx+=1
    if self.indx>=4: self.indx=0
    self.layout.setCurrentIndex(self.indx)
    
if __name__=="__main__":
  app = QApplication()
  
  win = MyApp__()
  win.show()
  
  app.exec()