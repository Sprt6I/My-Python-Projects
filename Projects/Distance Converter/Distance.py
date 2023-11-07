from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

app = QApplication(sys.argv)
app.setStyleSheet(
    'QLineEdit {height:40%; font:30px;}'
    'QComboBox {height:40%;border:1px solid white;font:20px;}'
    'QPushButton {height: 40%;border:1px solid white; font:20px;}'
    'QLabel {font:20px;}'
)

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Distance Corvertion")
        self.setStyleSheet('background-color:black;color:white')
        
        lay0 = QVBoxLayout()
        
        
        label = QLabel("Input Distance: ")
        lay0.addWidget(label)
            
        self.Input = QLineEdit() #Input
        lay0.addWidget(self.Input)
        
        label1 = QLabel("Convert From: ")
        lay0.addWidget(label1)
        self.comboBoxFrom = QComboBox() #Drop List | Convert From
        self.measureArr = ['km','m','dm','mm']
        self.comboBoxFrom.addItems(self.measureArr)

        lay0.addWidget(self.comboBoxFrom)
        

        
        label1 = QLabel("Convert To: ")
        lay0.addWidget(label1)
        self.comboBoxTo = QComboBox() #Drop List | Convert To
        self.comboBoxTo.addItems(self.measureArr)
        lay0.addWidget(self.comboBoxTo)
        
        
        button = QPushButton("Convert") #Button for changing
        button.clicked.connect(self.convert)
        lay0.addWidget(button)
        
        self.label2 = QLabel("Answer: ")
        lay0.addWidget(self.label2)
        
        
        
        self.setLayout(lay0)
        
    def convert(self):
        try: suma = float(self.Input.text()) #Checks if text is number if not shows error
        except:self.ErrorMessageWrongInput()
        
        FromIndx = self.measureArr.index(self.comboBoxFrom.currentText())
        ToIndx = self.measureArr.index(self.comboBoxTo.currentText())
        
        if FromIndx==ToIndx:
            self.label2.setText(f'Ans: {self.Input.text()}{self.comboBoxTo.currentText()}')
            return
        
        #suma = int(self.Input.text())
        arr = [1000,10,10]
        if FromIndx<ToIndx:
            for _ in range(1, (ToIndx-FromIndx)+1):
                suma*=arr[_-1]
            self.label2.setText(f'Ans: {suma}{self.comboBoxTo.currentText()}')
            return


        for _ in range(1, (FromIndx-ToIndx)+1):
            suma/=arr[_-1]
        self.label2.setText(f'Ans: {suma}{self.comboBoxTo.currentText()}')
        
        
        
        
    def ErrorMessageWrongInput(self):
        mess = QMessageBox(text="U can enter only numbers !")
        mess.setWindowTitle("Wrong Input !")
        mess.exec()
        
        

window = Main()
window.show()
app.exec()