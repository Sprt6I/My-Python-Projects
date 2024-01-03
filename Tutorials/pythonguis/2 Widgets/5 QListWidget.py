import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QWidget,
    QVBoxLayout,
)

class MainAppWin_(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Some App?")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    
    listWidget = QListWidget()
    listWidget.addItems(["One","Two","Three"])
    
    listWidget.currentItemChanged.connect(self.IndexChanged_)
    listWidget.currentTextChanged.connect(self.TextChanged_)
    
    mainLayout.addWidget(listWidget)
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
  def IndexChanged_(self,indx):
    print(indx.text())
    
  def TextChanged_(self, text):
    print(text)
    
if __name__=="__main__":
  app = QApplication(sys.argv)
  
  win = MainAppWin_()
  win.show()
  
  app.exec()
  
  
    
    