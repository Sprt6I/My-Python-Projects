import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainAppWin(QMainWindow):
  def __init__(self):
    super().__init__()
    self.label = QLabel("Click In This Window")
    self.setCentralWidget(self.label)
    
  def mousePressEvent(self, event: QMouseEvent) -> None:
    if event.button()== Qt.MouseButton.LeftButton:
      self.label.setText("Mouse Left Button Was Prssed")
    elif event.button()==Qt.MouseButton.MiddleButton:
      self.label.setText("Mouse Middle Button Was Pressed")
    elif event.button()== Qt.MouseButton.RightButton:
      self.label.setText("Mouse Right Button Was Pressed")
    
  def mouseReleaseEvent(self, event: QMouseEvent) -> None:
    if event.button()== Qt.MouseButton.LeftButton:
      self.label.setText("Mouse Left Button Was Released")
    elif event.button()==Qt.MouseButton.MiddleButton:
      self.label.setText("Mouse Middle Button Was Released")
    elif event.button()== Qt.MouseButton.RightButton:
      self.label.setText("Mouse Right Button Was Released")
      
  def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
    if event.button()== Qt.MouseButton.LeftButton:
      self.label.setText("Mouse Left Button Was DoubleClicked")
    elif event.button()==Qt.MouseButton.MiddleButton:
      self.label.setText("Mouse Middle Button Was DoubleClicked")
    elif event.button()== Qt.MouseButton.RightButton:
      self.label.setText("Mouse Right Button Was DoubleClicked")
      
      
if __name__ == "__main__":
  app = QApplication()
  
  win = MainAppWin()
  win.show()
  
  app.exec()