import sys

from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor, QFont 
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)


class MainAppWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle('Some App')
    
    
    
    self.UI_()
  
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    imagesLayout = QHBoxLayout()
    
    '''label = QLabel("hampter")
    font = label.font()
    font.setPointSize(30)
    label.setFont(font)
    label.setAlignment(
      Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
    )'''
    
    label2 = QLabel()
    label2.setScaledContents(True)
    label2.setPixmap(QPixmap('/home/deleted/Documents/hampter.jpg'))
    imagesLayout.addWidget(label2)
    
    
    
    dampterImg = QPixmap('/home/deleted/Documents/dampter.jpg')
    label3 = QLabel()
    label3.setScaledContents(True)
    label3.setPixmap(dampterImg)
    
    
    painter = QPainter(dampterImg)
    
    pen = QPen()
    pen.setWidth(1)
    pen.setColor(QColor("black"))
    painter.setPen(pen)

    font = QFont()
    #font.setFamily("Times")
    font.setPointSize(50)
    painter.setFont(font)
    #QRect(),  | 
    painter.drawText(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignLeft,Qt.AlignmentFlag.AlignBottom, "Dampter")
    
    painter.end()
    
    label3.setPixmap(dampterImg)
    
    
    imagesLayout.addWidget(label3)
    mainLayout.addLayout(imagesLayout)
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  
  win = MainAppWindow()
  win.show()
  
  app.exec()