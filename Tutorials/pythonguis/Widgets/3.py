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
    
    check = QCheckBox()
    check.setCheckState(Qt.CheckState.Checked)
    
    check.stateChanged.connect(self.ShowState_)
    
    mainLayout.addWidget(check)
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
  def ShowState_(self, state):
    print(state == Qt.CheckState.Checked.value)
    print(state)
    
if __name__=="__main__":
  app = QApplication()
  
  win = MainAppWin()
  win.show()
  
  app.exec()