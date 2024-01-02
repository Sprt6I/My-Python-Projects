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

class MainAppWin(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Some App?")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    
    comboBox = QComboBox()
    comboBox.setEditable(True)
    comboBox.setInsertPolicy(QComboBox.InsertAtTop) #It's working
    comboBox.setMaxCount(10)
    comboBox.addItems(["One","Two","Three"])
    
    comboBox.currentIndexChanged.connect(self.IndxChanged_)
    
    comboBox.currentTextChanged.connect(self.TextChanged_)
    
    mainLayout.addWidget(comboBox)
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
  def IndxChanged_(self, indx):
    print(indx)
    
  def TextChanged_(self, text):
    print(text)
    

if __name__=="__main__":
  app = QApplication(sys.argv)
  
  win = MainAppWin()
  win.show()
  
  app.exec()