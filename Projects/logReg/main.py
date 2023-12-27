import mysql.connector
from PySide6.QtWidgets import QLabel, QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
from abc import ABC, abstractmethod, ABCMeta
import sys

db = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = 'root',
  database="logReg"
)

cursor = db.cursor()

#cursor.execute('DROP TABLE users;')
#cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, login VARCHAR(30), password VARCHAR(50));")


'''cursor.execute("SHOW TABLES;")

for i in cursor:
  print(i)'''
  
class ShadowLineEdit(QLineEdit):
   def __init__(self, *args, **kwargs):
       super(ShadowLineEdit, self).__init__(*args, **kwargs)

   def paintEvent(self, event):
       painter = QPainter(self)
       painter.setPen(Qt.gray)
       painter.drawText(self.rect(), Qt.AlignCenter, self.placeholderText())
       super(ShadowLineEdit, self).paintEvent(event)
  
  
class LoginWindow_(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Login Window")
    
    self.UI_()
    
  def UI_(self):
    self.regWin = RegisterWindow_()

    self.mainLayout = QVBoxLayout()
    
    appName = QLabel("Some App")
    self.mainLayout.addWidget(appName)

    
    shadow_line_edit = ShadowLineEdit()
    shadow_line_edit.setPlaceholderText("Login")
    self.mainLayout.addWidget(shadow_line_edit)
    
    shadow_line_edit = ShadowLineEdit()
    shadow_line_edit.setPlaceholderText("Password")
    self.mainLayout.addWidget(shadow_line_edit)
    
    sumbmitButton = QPushButton("Login")
    self.mainLayout.addWidget(sumbmitButton)
    
    noAccountButton = QPushButton("I don\'t have an account")
    noAccountButton.clicked.connect(self.openRegisterWindow_)
    self.mainLayout.addWidget(noAccountButton)
    
    self.setLayout(self.mainLayout)
    
  def openRegisterWindow_(self):
    self.regWin.show()
    


class RegisterWindow_(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Register Window")
    
    self.UI_()
    
  def UI_(self):
    self.mainLayout = QVBoxLayout()
    
    appName = QLabel("Some App")
    self.mainLayout.addWidget(appName)
    
    loginInp = ShadowLineEdit()
    loginInp.setPlaceholderText("Login")
    self.mainLayout.addWidget(loginInp)
    
    passwordInp = ShadowLineEdit()
    passwordInp.setPlaceholderText("Password")
    self.mainLayout.addWidget(passwordInp)
    
    sumbmitButton = QPushButton("Sumbmit")
    self.mainLayout.addWidget(sumbmitButton)
    
    self.setLayout(self.mainLayout)
    
    


if __name__=="__main__":
  app = QApplication()
  window = LoginWindow_()
  window.show()
  app.exec()