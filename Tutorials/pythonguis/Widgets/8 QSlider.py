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

class MainApp__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("My App?")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    
    slider = QSlider(Qt.Orientation.Horizontal)
    
    slider.setMinimum(0)
    slider.setMaximum(100)
    
    slider.setSingleStep(1)
    
    slider.valueChanged.connect(self.ValueChanged_)
    slider.sliderMoved.connect(self.SliderPosition_)
    slider.sliderPressed.connect(self.SliderPressed_)
    slider.sliderReleased.connect(self.SliderReleased_)
    
    mainLayout.addWidget(slider)
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
  def ValueChanged_(self, value):
    print(value)
    
  def SliderPosition_(self, position):
    print(position)
    
  def SliderPressed_(self):
    print("Slider Pressed !")
    
  def SliderReleased_(self):
    print("Released")
    
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  
  win = MainApp__()
  win.show()
  
  app.exec()