from re import X
import sys
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QMenu


class MainApp_(QWidget):
  def __init__(self):
    super().__init__()
    self.setMinimumSize(400, 300)
    
    self.setMouseTracking(True)
    self.label = QLabel("Click in this window")
    self.label.setFixedSize(200,50)
    #self.setCentralWidget(self.label)
    
  def mouseMoveEvent(self, event: QMouseEvent) -> None:
    self.mouse_pos = QPoint(event.x(), event.y())
    self.label.move(self.mouse_pos)
    #self.layout().addWidget(label)
    
    print(f"Mouse Moved at ({event.x()}, {event.y()})")
    
  def mousePressEvent(self, event: QMouseEvent) -> None:
    self.label.setText("Mouse Pressed")
    
  def mouseReleaseEvent(self, event: QMouseEvent) -> None:
    self.label.setText("Mouse Released")
    
  def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
    self.label.setText("Mouse Double Clicked")
  
  
if __name__=='__main__':
  app = QApplication(sys.argv)
  
  win = MainApp_()
  win.show()
  
  app.exec()