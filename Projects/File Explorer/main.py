from PySide6.QtWidgets import QSizePolicy,QMainWindow, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QScrollArea, QLabel, QHBoxLayout, QSpacerItem
from PySide6.QtCore import Qt
import sys
import os
from functools import partial

class FolderManager__(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("File Explorer")
    self.setGeometry(100, 100, 600, 400)
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    self.mainLayout = QVBoxLayout()
    self.itemsWidget = QWidget()
    self.itemsLayout = QVBoxLayout()
    self.scroll = QScrollArea() #type: ignore
  
    self.itemsLayout.setSpacing(0)
    self.itemsLayout.setContentsMargins(0, 0, 0, 0)
    
    self.mainLayout.setSpacing(0)
    self.mainLayout.setContentsMargins(0, 0, 0, 0)
    
    
    self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) #type: ignore
    self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #type: ignore
    self.scroll.setWidgetResizable(True)
    
    
    self.Directories = QLineEdit(os.getcwd())
    self.Directories.returnPressed.connect(lambda: self.ChangedDirectory_(self.Directories.text()))
    self.mainLayout.addWidget(self.Directories)
    
    
    self.CreateButtons_()
    self.itemsLayout.addStretch()
    self.itemsWidget.setLayout(self.itemsLayout)
    self.scroll.setWidget(self.itemsWidget)
    
    
    self.mainLayout.addWidget(self.scroll)
    
    
    self.dataLabel = QLineEdit(f'{len(os.listdir(os.getcwd()))} items, {self.CalculateDiskFreeSpace_(os.getcwd())} GB')
    self.dataLabel.setAlignment(Qt.AlignCenter) #type: ignore
    self.mainLayout.addWidget(self.dataLabel)
    
    
    mainWidget.setLayout(self.mainLayout)
    self.setCentralWidget(mainWidget)
    
    
    
  def CreateButtons_(self):  
    Currentdir = os.getcwd()
    arr = os.listdir(Currentdir)
    print(arr)
    
    for indx, val in enumerate(arr):
      lay = QHBoxLayout()
      but = QPushButton(val, self)
      but.clicked.connect(partial(self.ChangeLoc_, val))
      but.setMinimumWidth(240)
      lay.addWidget(but)
      
      lay.addItem(QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Preferred)) #type:ignore
      
      _, ext = os.path.splitext(Currentdir+val)
      fileType = QLabel(ext[1:] if ext else "Folder")
      fileType.setMinimumWidth(160)
      lay.addWidget(fileType)
      
      fileSize = QLabel(f"{round(os.path.getsize(Currentdir +'/'+ val)/1024, 2)} MB" if (ext and ext!='.git' and ext!='.vscode') else f'{len(os.listdir(Currentdir+"/"+val))} items')
      lay.addWidget(fileSize)
      
      
      self.itemsLayout.addLayout(lay)
    
    #self.itemsLayout.setSpacing(10)
    self.itemsLayout.update()
    self.update()
  
  
  def ChangeLoc_(self, where: str):
    while self.itemsLayout.count():
       child = self.itemsLayout.takeAt(0).layout()
       if child is not None:
           for i in reversed(range(child.count())):
               w = child.itemAt(i).widget()
               if w is not None:
                  w.deleteLater()
            
    os.chdir(where)
            
    #self.itemsLayout.setSpacing(10)
    #self.adjustSize()
            
    self.CreateButtons_()
    
    self.dataLabel.setText(f'{len(os.listdir(os.getcwd()))} items, {self.CalculateDiskFreeSpace_(os.getcwd())} GB')
    
    self.itemsLayout.addStretch()
    self.Directories.setText(os.getcwd())
    
  def ChangedDirectory_(self, text):
    self.ChangeLoc_(text)
    #print(f"LineEdit Pressed! {text}")
    
  def CalculateDiskFreeSpace_(self, path: str) -> float:
    st = os.statvfs(path)

    freeSpace = bytes_avail = st.f_bavail * st.f_frsize

    freeSpaceGB = freeSpace /1024 /1024 / 1024
    #print(freeSpace)
    #print(freeSpaceGB)
    return round(freeSpaceGB, 2)
  
  
  
if __name__=="__main__":
  app = QApplication(sys.argv)
  
  win = FolderManager__()
  win.show()
  
  app.exec()