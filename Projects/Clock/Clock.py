from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6 import QtCore
import time

class ClockWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Clock')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(200, 200, 700, 200)
        
        self.UI_()
        
    def UI_(self):
        self.MainLayout = QVBoxLayout(self)
        
        self.timeText = QLabel(self)
        self.timeText.setStyleSheet('color:white;font-size: 20px')
        self.MainLayout.addWidget(self.timeText)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.UpdateClock_)
        self.timer.start(1000)
        
        
    def UpdateClock_(self):
        current_time = time.localtime()
        self.timeText.setText(f'{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}')
        
    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        self.move(self.mapToGlobal(event.pos() - self.offset))

if __name__ == '__main__':
    app = QApplication([])
    appWindow = ClockWindow()
    appWindow.show()
    app.exec()
