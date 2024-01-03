import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QMenu, QVBoxLayout, QLabel

class AppMainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('hehe')
    self.setMinimumSize(200,400)
    
    self.UI_()
    
  def UI_(self):
    mainLayout = QVBoxLayout()
    
    self.label = QLabel("Some Text")
    mainLayout.addWidget(self.label)
    
    self.setLayout(mainLayout)
    
  def contextMenuEvent(self, event):
   context = QMenu(self)

   action1 = QAction("<3", self)
   action2 = QAction("hehe", self)
   action3 = QAction("123", self)

   context.addAction(action1)
   context.addAction(action2)
   context.addAction(action3)

   action1.triggered.connect(lambda: self.ChangeText(action1.text()))
   action2.triggered.connect(lambda: self.ChangeText('hehe'))
   action3.triggered.connect(lambda: self.ChangeText('123'))
   
   context.exec(event.globalPos())
    
  def ChangeText(self,text: str):
    self.label.setText(text)
    
if __name__=="__main__":
  app = QApplication()
  
  win = AppMainWin()
  win.show()
  
  app.exec()