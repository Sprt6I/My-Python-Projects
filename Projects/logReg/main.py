import mysql.connector
from PySide6.QtWidgets import QLabel, QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
import sys



#cursor.execute('DROP TABLE users;')
#cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, login VARCHAR(30), password VARCHAR(50));")

class ShadowLineEdit(QLineEdit): #Special QLabel with "Shadow text"
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
    
    
    appName = QLabel("Some App") #App Name
    self.mainLayout.addWidget(appName)

    loginInp = ShadowLineEdit() #Login Input
    loginInp.setPlaceholderText("Login")
    self.mainLayout.addWidget(loginInp)
    
    passwordInp = ShadowLineEdit() #Password Input
    passwordInp.setPlaceholderText("Password")
    self.mainLayout.addWidget(passwordInp)
    
    self.warningLabel = QLabel() #Warning Label
    self.mainLayout.addWidget(self.warningLabel)
    
    sumbmitButton = QPushButton("Login") #Sumbmit Button
    sumbmitButton.clicked.connect(lambda: self.Login_(loginInp.text(), passwordInp.text()))
    self.mainLayout.addWidget(sumbmitButton)
    
    noAccountButton = QPushButton("I don\'t have an account") #Register Button
    noAccountButton.clicked.connect(self.openRegisterWindow_)
    self.mainLayout.addWidget(noAccountButton)
    
    
    self.setLayout(self.mainLayout)
    
    
    
  def Login_(self, login: str, password: str) -> int:
    db = mysql.connector.connect( #Connect With Database
      host = 'localhost',
      user = 'root',
      password = 'root',
      database="logReg"
    )
    cursor = db.cursor()
    
    cursor.execute(f'SELECT login, password from users WHERE login="{login}";') #Select All Users With Login Provided Earlier (In "loginInp") To Check If User Exists
    
    try: #Checks If user exists
      usr = cursor.fetchall()[0] #Gets 1 Element (If User Exists, Element Exists, Else It's Error)
      print(usr)
    except:  #If It's Error Shows User Message And Stops Further Code
      self.warningLabel.setText(f"User {login}, not found :/")
      return 0
    
    
    if usr[1]==password: #Checks If Provided Password (in "passwordInp") Is Equal To Password From Query (line 75)
      self.warningLabel.setText(f"Logging into {login}")
      db.close()
      return 1
    else:
      self.warningLabel.setText("Wrong Password!")
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
    
    
    appName = QLabel("Some App") #App Name
    self.mainLayout.addWidget(appName)
    
    loginInp = ShadowLineEdit() #Login Inpput
    loginInp.setPlaceholderText("Login")
    self.mainLayout.addWidget(loginInp)
    
    passwordInp = ShadowLineEdit() #Password Input
    passwordInp.setPlaceholderText("Password")
    self.mainLayout.addWidget(passwordInp)
    
    self.warningLabel = QLabel() #Warning Label
    self.mainLayout.addWidget(self.warningLabel)
    
    sumbmitButton = QPushButton("Sumbmit") #Sumbmit Button
    sumbmitButton.clicked.connect(lambda: self.addUser_(loginInp.text(), passwordInp.text()))
    self.mainLayout.addWidget(sumbmitButton)
    
    
    self.setLayout(self.mainLayout)
    
    
    
  def addUser_(self, login: str, password:str) -> int:
    if len(login)<3: 
      self.warningLabel.setText('Login can\'t be shorter than 3')
      return 0
    
    if len(password)<4:
      self.warningLabel.setText('Password can\'t be shoter than 4')
      return 0
    
    db = mysql.connector.connect( #Connects With Databse
      host = 'localhost',
      user = 'root',
      password = 'root',
      database="logReg"
    )
    cursor = db.cursor()
    
    cursor.execute(f'SELECT * FROM users WHERE login="{login}";') 
    
    try: #Checks If user Exists (If Yes, Prints: User Exists And Stops Further Code)
      usr = cursor.fetchall()[0] #Gets 1 Element (If User Exists, Element Exists, Else It's Error)
      print(usr)
      self.warningLabel.setText("This User already exists :/")
      db.close()
      return 0
    except: pass
    
    cursor.execute(f'INSERT INTO users (login, password) VALUES ("{login}", "{password}")') #Adds User To Databse
    
    db.commit() #Commits Changes Into Databse
    
    print(f'User {login}, {password} Added')
    db.close() #Closes Connection With Databse
    
    return 1
    


if __name__=="__main__":
  app = QApplication()
  window = LoginWindow_()
  window.show()
  app.exec()
  
"""!!! IT'S ONLY FOR TEST !!!"""
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