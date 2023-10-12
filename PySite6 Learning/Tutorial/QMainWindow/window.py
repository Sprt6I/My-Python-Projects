import sys
from PySide6.QtWidgets import *

class MainWin(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom Main Window")

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        quitAct = fileMenu.addAction("Quit")
        quitAct.triggered.connect(self.quitApp)
        
    def quitApp(self):
        self.app.quit()
        