import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        
        button = QPushButton("Press Me !", self)
        button.setCheckable(True)
        button.clicked.connect(self.button_click)
        
        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(25)
        slider.valueChanged.connect(self.sliderResponse)
        
    def button_click(self, data):
        if data:
            print("Button Checked")
        else:
            print("Button UnChecked")
            
    def sliderResponse(self, data):
        print(f"Value: {data}")
        
app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()