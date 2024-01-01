import sys
import os
import requests

'''Checks Pip'''
x = os.system('pip --version') #Checks if pip is installed
  
if x!=0: #0==installed else some other number
  '''Install Pip'''
  url = 'https://bootstrap.pypa.io/get-pip.py'
  response = requests.get(url)
  with open('get-pip.py', 'wb') as f:
      f.write(response.content)
      
  os.system('py get-pip.py')
  os.system('python get-pip.py')
  os.system('python3 get-pip.py')


'''Check All Librares'''
try:
  import psutil
  import signal
  from random import choice
  from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel
except:
  os.system('pip install psutil')
  os.system('pip install signal')
  os.system('pip install random')
  os.system('pip install PySide6')
  import psutil
  import signal
  from random import choice
  from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel


'''App'''
class App_(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Hello User")
    
    self.arr = ['a','b','c','d','e','error','f','g'] #Window Names
    
    self.UI_()
    
  def UI_(self):
    self.mainLayout = QVBoxLayout()
    
    self.button = QPushButton("hehe")
    self.button.clicked.connect(self.ChangeWindowName)
    self.mainLayout.addWidget(self.button)
    
    self.label = QLabel("error")
    
    self.setLayout(self.mainLayout)
    
    
  def ChangeWindowName(self):
    val = choice(self.arr)
    self.setWindowTitle(val)
    
    if val=="error":
      self.button.deleteLater()
      self.mainLayout.addWidget(self.label)
      self.TerminateProcess_()
      
  
  def TerminateProcess_(self):
   arr = ['steam', 'brave', 'opera', 'chrome', 'edge', 'microsoft-store', 'firefox', 'powershell', 'cmd', 'safari']
   for proc in psutil.process_iter(['pid', 'name']):
      print(proc.pid, proc.name)
      if proc.info['name'] in arr:
        os.kill(proc.info['pid'], signal.SIGTERM)
      
      
if __name__ == "__main__":
  app = QApplication(sys.argv)
  
  window = App_()
  window.show()
  
  app.exec()