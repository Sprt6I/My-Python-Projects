import mysql.connector
from PySide6.QtWidgets import QLabel, QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
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
  
  
  
class RegisterWindow_(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Register Window")
    
    self.UI_()
    
  def UI_(self):
    self.mainLayout = QVBoxLayout()
    
    appName = QLabel("Some App")
    self.mainLayout.addWidget(appName)
    
    shadow_line_edit = ShadowLineEdit()
    shadow_line_edit.setPlaceholderText("Name")
    self.mainLayout.addWidget(shadow_line_edit)
    
    
    self.setLayout(self.mainLayout)
    



if __name__=="__main__":
  app = QApplication()
  window = RegisterWindow_()
  window.show()
  app.exec()