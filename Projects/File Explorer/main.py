from PySide6.QtWidgets import QSizePolicy,QMainWindow, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QScrollArea
from PySide6.QtCore import Qt
import sys
import os
from functools import partial

class FolderManager__(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("File Explorer")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    self.mainLayout = QVBoxLayout()
    self.itemsWidget = QWidget()
    self.itemsLayout = QVBoxLayout()
    self.scroll = QScrollArea() #type: ignore
    
    
    self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) #type: ignore
    self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #type: ignore
    self.scroll.setWidgetResizable(True)
    
    
    self.Directories = QLineEdit(os.getcwd())
    self.Directories.returnPressed.connect(lambda: self.ChangedDirectory_(self.Directories.text()))
    self.mainLayout.addWidget(self.Directories)
    
    
    self.CreateButtons_()
    self.itemsWidget.setLayout(self.itemsLayout)
    self.scroll.setWidget(self.itemsWidget)
    
    
    self.mainLayout.addWidget(self.scroll)
    
    
    mainWidget.setLayout(self.mainLayout)
    self.setCentralWidget(mainWidget)
    
    
    
  def CreateButtons_(self):  
    arr = os.listdir(os.getcwd())
    print(arr)
    
    for i in arr:
      but = QPushButton(i, self)
      #but.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) #type:ignore
      but.clicked.connect(partial(self.ChangeLoc_, i))
      self.itemsLayout.addWidget(but)
    
    #self.update()
    #return os.listdir(os.getcwd())
  
  
  def ChangeLoc_(self, where: str):
    print(where)
    for i in range(self.itemsLayout.count()):
        child = self.itemsLayout.itemAt(i).widget()
        if child:
            child.deleteLater()
            
    os.chdir(where)
            
    self.itemsLayout.setSpacing(0)
    #self.adjustSize()
            
    self.CreateButtons_()
    self.Directories.setText(os.getcwd())
    
  def ChangedDirectory_(self, text):
    self.ChangeLoc_(text)
    #print(f"LineEdit Pressed! {text}")
  
  
  
if __name__=="__main__":
  app = QApplication(sys.argv)
  
  win = FolderManager__()
  win.show()
  
  app.exec()