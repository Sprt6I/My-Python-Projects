import sys

from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class MainAppWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Widgets App")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    
    widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]
    
    
    for i in widgets:
      #mainLayout.addWidget(QLabel(f'{i}'))
      mainLayout.addWidget(i())
      
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
if __name__ == "__main__":
  app = QApplication()
  
  win = MainAppWindow()
  win.show()
  
  app.exec()