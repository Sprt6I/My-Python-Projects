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

class MyApp__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("My App?")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    
    dial = QDial()
    dial.setRange(0, 360)
    dial.setSingleStep(1)
    
    dial.valueChanged.connect(self.ValueChanged_)
    dial.sliderMoved.connect(self.DialPosition_)
    dial.sliderPressed.connect(self.DialPressed_)
    dial.sliderReleased.connect(self.DialReleased_)

    mainLayout.addWidget(dial)
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
  def ValueChanged_(self, val):
    print(val)
    
  def DialPosition_(self, pos):
    print(f"Position: {pos}")

  def DialPressed_(self):
    print("Dial Pressed !")
    
  def DialReleased_(self):
    print("Dial Released !")    
    
    
if __name__=="__main__":
  app = QApplication(sys.argv)
  
  win = MyApp__()
  win.show()
  
  app.exec()