from PySide6.QtWidgets import QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QMainWindow, QWidget, QHBoxLayout
import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
print(mydb)

# EVERY SERVER IS OWN DATABASE

'''

Database Server:
* Users:
* Chanells:


Database Users:
 *  Main:
  - Name
  - Password

'''

class Discord__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle('Discord')
    
    self.UI_()
    
  def UI_(self):
    self.mainWidget = QWidget()
    self.mainLayout = QHBoxLayout()
    
    self.serverList = QVBoxLayout()
    self.channelsList = QVBoxLayout()
    self.usersList = QVBoxLayout()
    
    