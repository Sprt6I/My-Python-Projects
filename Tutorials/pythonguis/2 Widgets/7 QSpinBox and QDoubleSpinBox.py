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
    
    self.setWindowTitle("Some App?")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    
    spinBox = QDoubleSpinBox()
    spinBox.lineEdit().setReadOnly(True)
    
    spinBox.setMinimum(-10)
    spinBox.setMaximum(3.5)
    spinBox.setRange(-10, 3.5)
    
    spinBox.setPrefix('$')
    spinBox.setSuffix("c")
    spinBox.setSingleStep(3)
    spinBox.valueChanged.connect(self.ValueChanged_)
    spinBox.textChanged.connect(self.ValueChangedStr_)
    
    mainLayout.addWidget(spinBox)
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
  def ValueChanged_(self, value):
    print(value)
    
  def ValueChangedStr_(self, strVal):
    print(strVal)
    
    
if __name__=="__main__":
  app = QApplication(sys.argv)
  
  win = MyApp__()
  win.show()
  
  app.exec()