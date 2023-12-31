from PySide6.QtWidgets import QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QLabel
from PySide6.QtCore import Qt
from random import choice
import sys
import subprocess
import os
import psutil
import signal

def terminate_process(process_name):
   for proc in psutil.process_iter(['pid', 'name']):
       if proc.info['name'] == process_name:
           os.kill(proc.info['pid'], signal.SIGTERM)



class App_(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Hello User")
    
    self.arr = ['a','b','c','d','e','error','f','g']
    
    self.UI_()
    
  def UI_(self):
    self.mainLayout = QVBoxLayout()
    
    self.button = QPushButton("hehe")
    self.button.clicked.connect(self.Yep_)
    self.mainLayout.addWidget(self.button)
    
    self.label = QLabel("error")
    #mainLayout.addWidget(self.label)
    
    self.setLayout(self.mainLayout)
    
    
  def Yep_(self):
    val = choice(self.arr)
    self.setWindowTitle(val)
    
    if val=="error":
      self.button.deleteLater()
      self.mainLayout.addWidget(self.label)
      terminate_process('brave')
      
      
if __name__ == "__main__":
  app = QApplication(sys.argv)
  
  window = App_()
  window.show()
  
  app.exec()