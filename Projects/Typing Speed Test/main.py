import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "/usr/local/lib/python3.10/dist-packages/PySide6/Qt/plugins"
from PySide6.QtWidgets import QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QLabel
from PySide6.QtCore import QTimer, Qt
import sys
from random import choice, randrange
import time


app = QApplication(sys.argv)

class SpeedTestWindowClass(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Speed Test")
    self.setGeometry(200,200,400,400)
  
    
    
    self.UI_()
    
  def UI_(self):
    mainLayout = QVBoxLayout()
    
    
    self.TimerScript_()
    
    self.timeText = QLabel(str(self.time))
    self.timeText.setAlignment(Qt.AlignCenter)
    mainLayout.addWidget(self.timeText)
    
    self.inp = QTextEdit()
    self.inp.setOverwriteMode(True)
    mainLayout.addWidget(self.inp)
    
    self.MakeTest_()
    
    self.setLayout(mainLayout)
    
  def TimerScript_(self):
    self.time = 0
    
    self.timer = QTimer(self)
    self.timer.timeout.connect(self.TimeUpdate_)
    self.timer.start(1000)
    
  def MakeTest_(self):
    arr = ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry.', 'Lorem', 'Ipsum', 'has', 'been', 'the', "industry's", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s,', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book.', 'It', 'has', 'survived', 'not', 'only', 'five', 'centuries,', 'but', 'also', 'the', 'leap', 'into', 'electronic', 'typesetting,', 'remaining', 'essentially', 'unchanged.', 'It', 'was', 'popularised', 'in', 'the', '1960s', 'with', 'the', 'release', 'of', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages,', 'and', 'more', 'recently', 'with', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'versions', 'of', 'Lorem', 'Ipsum.']
    
    testArr = []
    
    for i in range(50):
      testArr.append(arr[randrange(0, len(arr)-1)])
      
    print(testArr)
    self.inp.setText(' '.join(testArr))
    
  def TimeUpdate_(self):
    self.time+=1
    self.timeText.setText(str(self.time))
    
      
    
    
    
    
    
    
if __name__=="__main__":
  win = SpeedTestWindowClass()
  win.show()
  app.exec()
    
    
    
    
    