from PySide6.QtWidgets import QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QCheckBox
import sys

class MainWindowApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        
        self.layout = QGridLayout()
        
        self.AddUI_()
        
        self.setLayout(self.layout)
        
    def AddUI_(self):
        PasswordShow = QLineEdit()
        self.layout.addWidget(PasswordShow,0,0)
        
        GenerateButton = QPushButton("Generate Password")
        GenerateButton.clicked.connect(self.Generate_)
        self.layout.addWidget(GenerateButton,0,1)
        
        
        
        self.lowerCaseLettersCheck = QCheckBox("LowerCase Characters")
        self.layout.addWidget(self.lowerCaseLettersCheck,1,0)
        
        self.upperCaseLettersCheck = QCheckBox("UpperCase Characters")
        self.layout.addWidget(self.upperCaseLettersCheck,1,1)
        
        self.NumsCheck = QCheckBox("Nums")
        self.layout.addWidget(self.NumsCheck,1,2)
        
        self.SpecialCharCheck = QCheckBox("Special Characters")
        self.layout.addWidget(self.SpecialCharCheck,1,3)
        
        self.PasswordLength = QLineEdit("Length Of Password")
        self.layout.addWidget(self.PasswordLength,1,4)
        
    def Generate_(self):
        print(self.lowerCaseLettersCheck.isChecked())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    appWindow = MainWindowApp()
    appWindow.show()
    app.exec()
        