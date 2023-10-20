from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class BMI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        
        lay = QVBoxLayout()
        
        EnterWeightLabel = QLabel("Input Weight:")
        WeightInput = QLineEdit()
        lay.addWidget(EnterWeightLabel)
        lay.addWidget(WeightInput)
        
        EnterHeightLabel = QLabel("Input Height (m):")
        HeightInput = QLineEdit()
        lay.addWidget(EnterHeightLabel)
        lay.addWidget(HeightInput)
        
        ConvertButton = QPushButton("Calculate")
        ConvertButton.clicked.connect(lambda: self.CalculateBMI(WeightInput.text(), HeightInput.text()))
        lay.addWidget(ConvertButton)
        
        self.AnswerMessage = QStatusBar()
        lay.addWidget(self.AnswerMessage)
        
        self.setLayout(lay)
    def CalculateBMI(self, weight: str , height: str) -> int:
        if weight == '' or not weight or len(weight)>5: return -1
        if height =='' or not height or len(height)>6: return -1

        for _ in weight:
            if _ not in '1234567890.':
                return -1
            
        for _ in height:
            if _ not in '1234567890.':
                return -1
            
        weight = float(weight)
        height = float(height)
        
        print(round((weight) / (height * height), 2))
        self.AnswerMessage.showMessage(str(round((weight) / (height * height), 2)))
        return 1

app = QApplication(sys.argv)
window = BMI()
window.show()
app.exec()