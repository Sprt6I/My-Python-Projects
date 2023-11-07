from PySide6.QtWidgets import QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QCheckBox, QLabel
import sys
import random
sys.path.append('C:/Users/User/Documents/GitHub/Python')
from HelpClasses import Lists

class MainWindowApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.setStyleSheet('background-color:black;color:white;')
        
        self.layout = QGridLayout()
        self.layout.setColumnStretch(0, 4)
        self.layout.setColumnStretch(1, 2)
        
        self.AddUI_()
        
        self.setLayout(self.layout)
        
    def AddUI_(self):
        self.PasswordShow = QLineEdit()
        self.PasswordShow.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.PasswordShow,0,0)
        
        GenerateButton = QPushButton("Generate Password")
        GenerateButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        GenerateButton.clicked.connect(self.Generate_)
        self.layout.addWidget(GenerateButton,0,1)
        
        
        
        self.lowerCaseLettersCheck = QCheckBox("LowerCase Characters")
        self.lowerCaseLettersCheck.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.lowerCaseLettersCheck,1,0)
        
        self.upperCaseLettersCheck = QCheckBox("UpperCase Characters")
        self.upperCaseLettersCheck.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.upperCaseLettersCheck,1,1)
        
        self.NumsCheck = QCheckBox("Nums")
        self.NumsCheck.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.NumsCheck,2,0)
        
        self.SpecialCharCheck = QCheckBox("Special Characters")
        self.SpecialCharCheck.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.SpecialCharCheck,2,1)
        
        PassLengthText = QLabel('<- Password Length')
        self.layout.addWidget(PassLengthText, 3,1)
        
        self.PasswordLength = QLineEdit()
        self.PasswordLength.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.PasswordLength,3, 0)
        
    def Generate_(self) -> int:
        if not self.PasswordLength.text(): return -1
        if len(self.PasswordLength.text()) > 2: return -1
        if int(self.PasswordLength.text()) > 60: return -1
        if not self.lowerCaseLettersCheck.isChecked() and not self.upperCaseLettersCheck.isChecked() and not self.NumsCheck.isChecked() and not self.SpecialCharCheck.isChecked(): return -1
        
        for _ in self.PasswordLength.text():
            if _ not in '1234567890':
                return -1
        
        arr = [self.lowerCaseLettersCheck.isChecked(), self.upperCaseLettersCheck.isChecked(), self.NumsCheck.isChecked(),self.SpecialCharCheck.isChecked()]
         
        s = ''
        for _ in range(int(self.PasswordLength.text())):
            toAdd = random.randrange(0,sum([1 for _ in arr if _==True])) #Rancom number <0, number of checked checkboxes>
            
            if arr[0]: #If first checkbox is checked
                if toAdd==0: #If rand number == 0
                    s+=random.choice(Lists.lowerCaseChar)
            else: #If not add 1 so next statement can be done
                toAdd+=1
                
            if arr[1]:
                if toAdd==1:
                    s+=random.choice(Lists.upperCaseChar)
            else:
                toAdd+=1
                
            if arr[2]:
                if toAdd==2:
                    s+=random.choice(Lists.numberList)
            else:
                toAdd+=1
                
            if arr[3]:
                if toAdd==3:
                    s+=random.choice(Lists.specialCHarList)
            else:
                toAdd+=1

        
        self.PasswordShow.setText(s)
        return 1
        
        

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.setStyleSheet(
        'QPushButton {border: 1px solid white; color: white;background-color:black;}'
        'QLineEdit {border: 1px solid white; color: white;background-color:black;}'
    )
    
    appWindow = MainWindowApp()
    appWindow.show()
    app.exec()
        