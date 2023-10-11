from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import *
import sys

class MyPyQt:
    def MyLabel(text, Styl, font=QFont("Arial", 14)):
        label = QLabel(text)
        if Styl:
            label.setStyleSheet(Styl)
        #if geometry:
        #    label.setGeometry(geometry)
        label.setFont(font)
        return label

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My PySide6 App") #Gives Window Name
        Width = 500
        Height = 700
        self.resize(Width, Height) #Sets Size Of Window
        
        Main = QFrame(self) #New Main Window
        Main.setFrameShape(QFrame.StyledPanel)
        Main.setFrameShadow(QFrame.Raised)
        Main.setStyleSheet("border-radius: 50px; background-color: lightblue;text-align: center;") #Sets stylesheet to window
        self.setWindowFlag(Qt.FramelessWindowHint) #Makes Window Frameless
        self.setAttribute(Qt.WA_TranslucentBackground) #Makes Window's background transparent
        
        TitleFont = QFont("Arial", 25)
        '''
        t = "Hello, PySide6!"
        Main.label = QLabel(t, Main)
        Main.label.setFont(TitleFont)
        Main.label.setStyleSheet("text-align: center;  background-color: transparent;")
        Main.label.setGeometry(Width/2-int(len(t)*8), 50,len(t)*25, 30)
        '''
        
        Main.label = MyPyQt.MyLabel("Hello, PySite6!", "background-color: transparent;", font=TitleFont)
        
        Main.but = QPushButton("Click me !", self)
        Main.but.setGeometry(Width/2-int(Main.but.width()/2), 100, 200, 30)
        Main.but.clicked.connect(self.on_button_click)
        
        
        
        self.setCentralWidget(Main) #Sets Main as Main Window or something
        
    def on_button_click(self):
        print("Button clicked!")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

