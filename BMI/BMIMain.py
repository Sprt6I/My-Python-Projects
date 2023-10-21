from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class BMI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        
        TabWidget = QTabWidget(self)

        
        
        ''' NORMAL VIEW '''
        NormalView = QWidget()
        
        lay = QVBoxLayout()
        
        EnterWeightLabel = QLabel("Input Weight (kg):")
        NormalWeightInput = QLineEdit()
        lay.addWidget(EnterWeightLabel)
        lay.addWidget(NormalWeightInput)
        
        EnterHeightLabel = QLabel("Input Height (m):")
        NormalHeightInput = QLineEdit()
        lay.addWidget(EnterHeightLabel)
        lay.addWidget(NormalHeightInput)
        
        ConvertButton = QPushButton("Calculate")
        ConvertButton.clicked.connect(lambda: self.CalculateBMI(NormalWeightInput.text(), NormalHeightInput.text(), 'Normal'))
        lay.addWidget(ConvertButton)
        
        self.AnswerMessage = QStatusBar()
        lay.addWidget(self.AnswerMessage)
        
        NormalView.setLayout(lay)
        
        
        ''' USA VIEW '''
        USAView = QWidget()
        lay1 = QVBoxLayout()
        EnterWeightLabel = QLabel("Input Weight (lbs):")
        USAWeightInput = QLineEdit()
        lay1.addWidget(EnterWeightLabel)
        lay1.addWidget(USAWeightInput)
        
        EnterHeightLabel = QLabel("Input Height (inch):")
        USAHeightInput = QLineEdit()
        lay1.addWidget(EnterHeightLabel)
        lay1.addWidget(USAHeightInput)
        
        ConvertButton = QPushButton("Calculate")
        ConvertButton.clicked.connect(lambda: self.CalculateBMI(USAWeightInput.text(), USAHeightInput.text(), 'USA'))
        lay1.addWidget(ConvertButton)
        
        self.AnswerMessage = QStatusBar()
        lay1.addWidget(self.AnswerMessage)
        
        USAView.setLayout(lay1)
        
        
        TabWidget.addTab(NormalView,"Normal View")
        TabWidget.addTab(USAView,"USA View")
        
        Mainlayout = QVBoxLayout()
        Mainlayout.addWidget(TabWidget)

        self.setLayout(Mainlayout)
    def CalculateBMI(self, weight: str , height: str, type:str) -> int:
        print('1')
        if weight == '' or not weight or len(weight)>5: return -1
        print('2')
        if height =='' or not height or len(height)>6: return -1
        print('3')

        for _ in weight:
            if _ not in '1234567890.':
                return -1
        print('4')
            
        for _ in height:
            if _ not in '1234567890.':
                return -1
            
        print('5')
        weight = float(weight)
        height = float(height)
        
        print(round((weight) / (height * height), 2))
        if type == "Normal": self.AnswerMessage.showMessage(str(round((weight) / (height * height), 2)))
        else: self.AnswerMessage.showMessage(str(round(((weight) / (height * height)*703), 2)))
        return 1

app = QApplication(sys.argv)
window = BMI()
window.show()
app.exec()