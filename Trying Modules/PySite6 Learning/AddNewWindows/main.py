from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)
        self.another_window = None  # Store the reference to AnotherWindow instance

    def show_new_window(self, checked):
        if not self.another_window:
            self.another_window = AnotherWindow()  # Create an instance if it doesn't exist
        self.another_window.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()