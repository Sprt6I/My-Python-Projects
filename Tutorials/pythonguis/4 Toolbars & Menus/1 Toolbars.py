import sys
from PySide6.QtWidgets import (
  QMainWindow, QApplication,
  QLabel, QToolBar, QStatusBar,
  QWidget, QVBoxLayout
)
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import Qt

class MyApp__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Some App")
    
    self.UI_()
    
  def UI_(self):
    widget = QWidget()
    layout = QVBoxLayout()
    
    """TOOL BAR """
    toolBar = QToolBar("Main ToolBar")
    toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon) #type: ignore
    self.addToolBar(toolBar)
    
    toolBarSave = QAction(QIcon("/home/deleted/Documents/hampter.jpg"),"Save", self)
    toolBarSave.setStatusTip("Save Work")
    toolBarSave.triggered.connect(self.ToolBarSave)
    toolBar.addAction(toolBarSave)
    
    toolBar.addSeparator()
    
    toolBarEdit = QAction(QIcon("/home/deleted/Documents/hampter.jpg"),"Edit", self)
    toolBarEdit.setStatusTip("Edit Work")
    toolBarEdit.triggered.connect(self.ToolBarSave)
    toolBarEdit.setShortcut(QKeySequence("Ctrl+p")) #Shortcut For Button
    toolBar.addAction(toolBarEdit)
    
    """ WIDGETS """
    label = QLabel("Idk")
    label.setAlignment(Qt.AlignCenter) #type: ignore
    
    self.setStatusBar(QStatusBar(self))
    
    layout.addWidget(label)
    
    
    """ Menu Bar """
    
    menu = self.menuBar() #Makes Menus Show
    
    fileMenu = menu.addMenu('&File') #Adds Menu eg: "File", "Edit"
    fileMenu1 = menu.addMenu('&Edit')
    
    fileMenu.addMenu(fileMenu1) #"Creates" Sub Menu 'Edit' In 'File' Menu
    
    fileMenu.addAction(toolBarSave) #Add Action To "File" Menu
    fileMenu.addSeparator()
    fileMenu.addAction(toolBarEdit)
    
    widget.setLayout(layout)
    
    
    self.setCentralWidget(widget)
    
  def ToolBarSave(self, s):
    print("Save", s)
    
    
if __name__ == "__main__":
  app = QApplication()
  
  win = MyApp__()
  win.show()
  
  app.exec()