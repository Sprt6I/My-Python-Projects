import sys
from PySide6.QtWidgets import QApplication,QMessageBox, QLabel,QDialog,QDialogButtonBox,QMainWindow, QWidget, QPushButton, QVBoxLayout


class MyApp__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("My App?")
    
    self.UI_()
    
  def UI_(self):
    widget = QWidget()
    layout = QVBoxLayout()
    
    button = QPushButton("Press Me")
    button.clicked.connect(self.ButtonClicked_)
    
    layout.addWidget(button)
    
    widget.setLayout(layout)
    
    self.setCentralWidget(widget)
    
  def ButtonClicked_(self, s):
    print("click", s)
    
    
    messBox = QMessageBox.question(self, "Question dialog", "The longer message")
    #messBox.setWindowTitle("Idk")
    #messBox.setText("Something Happend And U Can\'t Do Anything About It hehe")
    #button = messBox.exec()
    
    '''if button ==QMessageBox.Ok: #type: ignore
      print('Nice')
    elif button==QMessageBox.Cancel: #type: ignore
      print('f u')'''
      
    '''
    QMessageBox.NoIcon	The message box does not have an icon.
    QMessageBox.Question	The message is asking a question.
    QMessageBox.Information	The message is informational only.
    QMessageBox.Warning	The message is warning.
    QMessageBox.Critical	The message indicates a critical problem.
    '''
      
    '''
    QMessageBox.Ok
    QMessageBox.Open
    QMessageBox.Save
    QMessageBox.Cancel
    QMessageBox.Close
    QMessageBox.Discard
    QMessageBox.Apply
    QMessageBox.Reset
    QMessageBox.RestoreDefaults
    QMessageBox.Help
    QMessageBox.SaveAll
    QMessageBox.Yes
    QMessageBox.YesToAll
    QMessageBox.No
    QMessageBox.NoToAll
    QMessageBox.Abort
    QMessageBox.Retry
    QMessageBox.Ignore
    QMessageBox.NoButton
    '''
      
    #dialog = CustomDialog__(self)
    #dialog.setWindowTitle("hmmm?")
    #dialog.exec()
    
    
class CustomDialog__(QDialog):
  def __init__(self, parent = None, name="Some Window", text="Something Happend, Is That Ok?"):
    super().__init__(parent)
    
    self.text = text
    
    self.setWindowTitle(name)
    
    self.UI_()
    
  def UI_(self):
    self.layout = QVBoxLayout() #type: ignore
    
    mess = QLabel(self.text)
  
  
    QBtn = QDialogButtonBox.Yes | QDialogButtonBox.No #type: ignore
    
    '''
    QDialogButtonBox.Ok
    QDialogButtonBox.Open
    QDialogButtonBox.Save
    QDialogButtonBox.Cancel
    QDialogButtonBox.Close
    QDialogButtonBox.Discard
    QDialogButtonBox.Apply
    QDialogButtonBox.Reset
    QDialogButtonBox.RestoreDefaults
    QDialogButtonBox.Help
    QDialogButtonBox.SaveAll
    QDialogButtonBox.Yes
    QDialogButtonBox.YesToAll
    QDialogButtonBox.No
    QDialogButtonBox.Abort
    QDialogButtonBox.Retry
    QDialogButtonBox.Ignore
    QDialogButtonBox.NoButton
    '''
    
    
    self.buttonBox = QDialogButtonBox(QBtn)
    self.buttonBox.accepted.connect(self.Accept_)
    self.buttonBox.rejected.connect(self.Reject_)
    
    self.layout.addWidget(mess)
    self.layout.addWidget(self.buttonBox)
    
    self.setLayout(self.layout)
    
  def Accept_(self):
    print('Accepted :)')
    
  def Reject_(self):
    print('f*ck u bro >:(')
    
    
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  
  win = MyApp__()
  win.show()
  
  app.exec()
    