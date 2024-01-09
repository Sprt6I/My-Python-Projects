from PySide6.QtWidgets import QSizePolicy,QMainWindow, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
import sys
import os

class FolderManager__(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("File Explorer")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    self.mainLayout = QVBoxLayout()
    
    self.mainLayout.setSpacing(0)
    
    self.CreateButtons_()
      
    mainWidget.setLayout(self.mainLayout)
    
    self.setCentralWidget(mainWidget)
    
    
  def CreateButtons_(self):  
    arr = os.listdir(os.getcwd())
    print(arr)
    
    for i in arr:
      but = QPushButton(f"{i}")
      #but.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) #type:ignore
      but.clicked.connect(lambda: self.ChangeLoc_(i))
      self.mainLayout.addWidget(but)
    
    self.update()
    #return os.listdir(os.getcwd())
  
  
  def ChangeLoc_(self, where: str):
    for i in range(self.mainLayout.count()):
        child = self.mainLayout.itemAt(i).widget()
        if child:
            child.deleteLater()
            
    os.chdir(where)
            
    self.mainLayout.setSpacing(0)
    self.adjustSize()
            
    self.CreateButtons_()
  
  
  
if __name__=="__main__":
  app = QApplication(sys.argv)
  
  win = FolderManager__()
  win.show()
  
  app.exec()