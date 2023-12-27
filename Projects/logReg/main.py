import mysql.connector
from PySide6.QtWidgets import QLabel, QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
from abc import ABC, abstractmethod, ABCMeta
import sys



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

    
    loginInp = ShadowLineEdit()
    loginInp.setPlaceholderText("Login")
    self.mainLayout.addWidget(loginInp)
    
    passwordInp = ShadowLineEdit()
    passwordInp.setPlaceholderText("Password")
    self.mainLayout.addWidget(passwordInp)
    
    sumbmitButton = QPushButton("Login")
    sumbmitButton.clicked.connect(lambda: self.Login_(loginInp.text(), passwordInp.text()))
    self.mainLayout.addWidget(sumbmitButton)
    
    noAccountButton = QPushButton("I don\'t have an account")
    noAccountButton.clicked.connect(self.openRegisterWindow_)
    self.mainLayout.addWidget(noAccountButton)
    
    self.setLayout(self.mainLayout)
    
  def Login_(self, login: str, password: str) -> int:
    db = mysql.connector.connect(
      host = 'localhost',
      user = 'root',
      password = 'root',
      database="logReg"
    )
    cursor = db.cursor()#buffered=True
    
    cursor.execute(f'SELECT login, password from users WHERE login="{login}";')
    
    try:
      usr = cursor.fetchall()[0]
      print(usr)
    except: 
      print(f"User {login}, not found :/")
      return 0
    
    
    if usr[1]==password:
      print(f"Logging into {login}")
      db.close()
      return 1
    else:
      print("Wrong Password!")
      db.close()
      return 1
    
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
    sumbmitButton.clicked.connect(lambda: self.addUser_(loginInp.text(), passwordInp.text()))
    self.mainLayout.addWidget(sumbmitButton)
    
    self.setLayout(self.mainLayout)
    
  def addUser_(self, login: str, password:str) -> int:
    if len(login)<3: 
      print('Login can\'t be shorter than 3')
      return 0
    
    if len(password)<4:
      print('Password can\'t be shoter than 4')
      return 0
    
    db = mysql.connector.connect(
      host = 'localhost',
      user = 'root',
      password = 'root',
      database="logReg"
    )
    cursor = db.cursor()
    
    cursor.execute(f'SELECT * FROM users WHERE login="{login}";') 
    
    print(cursor.fetchall())
    if cursor.fetchall():
      print("This User already exists :/")
      db.close()
      return 0
    
    cursor.execute(f'INSERT INTO users (login, password) VALUES ("{login}", "{password}")')
    
    db.commit()
    
    print(f'User {login}, {password} Added')
    db.close()
    
    return 1
    


if __name__=="__main__":
  app = QApplication()
  window = LoginWindow_()
  window.show()
  app.exec()
  
  
db = mysql.connector.connect(
      host = 'localhost',
      user = 'root',
      password = 'root',
      database="logReg"
)
cursor = db.cursor()

cursor.execute('SELECT * FROM users')

for i in cursor:
  print(i)