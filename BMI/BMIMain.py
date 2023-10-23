from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

app = QApplication(sys.argv)

app.setStyleSheet(
    'QMainWindow {background-color:black;}'
    'QPushButton {border: 1px solid white; color: white; background-color:black;}'
    'QLineEdit {border: 1px solid white; color:white;}'
    'QStatusBar {border: 1px solid white; color:white;}'
    'QTabWidget::pane {border: 1px solid white;}'  # Set the border color of QTabWidget
    'QTabBar::tab {background-color: black; color: white; border: 1px solid white; padding: 8px;}'  # Set text color and background color for tabs
    'QWidget {background-color:black; color:white;}'
    'QVBoxLayout {background-color:black; color:white;}'
)
class BMI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setStyleSheet('background-color:black;color:white;')
        
        TabWidget = QTabWidget(self)

        
        
        ''' NORMAL VIEW '''
        NormalView = QWidget()
        
        lay = QVBoxLayout()
        
        EnterWeightLabel = QLabel("Input Weight (kg):")
        NormalWeightInput = QLineEdit()
        NormalWeightInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lay.addWidget(EnterWeightLabel)
        lay.addWidget(NormalWeightInput)
        
        EnterHeightLabel = QLabel("Input Height (m):")
        NormalHeightInput = QLineEdit()
        NormalHeightInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lay.addWidget(EnterHeightLabel)
        lay.addWidget(NormalHeightInput)
        
        ConvertButton = QPushButton("Calculate")
        ConvertButton.clicked.connect(lambda: self.CalculateBMI(NormalWeightInput.text(), NormalHeightInput.text(), 'Normal'))
        ConvertButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lay.addWidget(ConvertButton)
        
        self.NormalAnswerMessage = QStatusBar()
        self.NormalAnswerMessage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lay.addWidget(self.NormalAnswerMessage)
        
        NormalView.setLayout(lay)
        
        
        ''' USA VIEW '''
        USAView = QWidget()
        lay1 = QVBoxLayout()
        EnterWeightLabel = QLabel("Input Weight (lbs):")
        USAWeightInput = QLineEdit()
        USAWeightInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lay1.addWidget(EnterWeightLabel)
        lay1.addWidget(USAWeightInput)
        
        EnterHeightLabel = QLabel("Input Height (inch):")
        USAHeightInput = QLineEdit()
        USAHeightInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lay1.addWidget(EnterHeightLabel)
        lay1.addWidget(USAHeightInput)
        
        ConvertButton = QPushButton("Calculate")
        ConvertButton.clicked.connect(lambda: self.CalculateBMI(USAWeightInput.text(), USAHeightInput.text(), 'USA'))
        ConvertButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lay1.addWidget(ConvertButton)
        
        self.USAAnswerMessage = QStatusBar()
        self.USAAnswerMessage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lay1.addWidget(self.USAAnswerMessage)
        
        USAView.setLayout(lay1)
        
        
        TabWidget.addTab(NormalView,"Normal View")
        TabWidget.addTab(USAView,"USA View")
        
        Mainlayout = QVBoxLayout()
        Mainlayout.addWidget(TabWidget)

        self.setLayout(Mainlayout)
    def CalculateBMI(self, weight: str , height: str, type:str) -> int:
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
        

        if type == "Normal": self.NormalAnswerMessage.showMessage(str(round((weight) / (height * height), 2)))
        else: self.USAAnswerMessage.showMessage(str(round(((weight) / (height * height)*703), 2)))
        


window = BMI()
window.show()
app.exec()