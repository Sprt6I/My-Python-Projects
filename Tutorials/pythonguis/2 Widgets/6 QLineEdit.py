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

class MainAppWin__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Some App?")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    
    self.lineEdit = QLineEdit()
    self.lineEdit.setInputMask('000.000.000.000;_')
    self.lineEdit.setMaxLength(10)
    self.lineEdit.setPlaceholderText("Enter yout text: ")
    
    #self.lineEdit.setReadOnly(True)
    
    self.lineEdit.returnPressed.connect(lambda: self.ReturnPressed_(self.lineEdit.text()))
    self.lineEdit.selectionChanged.connect(self.SelectionChanged_)
    self.lineEdit.textChanged.connect(self.TextChanged_)
    self.lineEdit.textEdited.connect(self.TextEdited_)
    
    mainLayout.addWidget(self.lineEdit)
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
  def ReturnPressed_(self, text):
    print(f"LineEdit Pressed! {text}")
    #self.lineEdit.setText("Boom !")
    
  def SelectionChanged_(self):
    print("Selection Changed !")
    print(self.lineEdit.selectedText())
    
  def TextChanged_(self, text):
    print(f"Text Changed: {text}")
    
  def TextEdited_(self,text):
    print(f"Text Edited: {text}")
    
    
if __name__=="__main__":
  app = QApplication(sys.argv)
  
  win = MainAppWin__()
  win.show()
  
  app.exec()