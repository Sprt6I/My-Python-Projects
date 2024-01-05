from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys


class SecWin__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("sec App ?! :o")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    
    lab = QLabel("Idk")
    mainLayout.addWidget(lab)
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
    
    
    
    
class MainApp__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Main App")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    
    but = QPushButton("Pusho For Window")
    but.clicked.connect(self.NewWindow_)
    mainLayout.addWidget(but)
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
  def NewWindow_(self):
    self.win = SecWin__()
    self.win.show()
    

if __name__=="__main__":
  app = QApplication()
  
  mainWin = MainApp__()
  mainWin.show()
  
  app.exec()
    
    
    
    
    
    