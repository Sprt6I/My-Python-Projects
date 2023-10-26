import sys
from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *

class ItemWidget(QWidget):
    def __init__(self, id_str="", parent=None):
        super(ItemWidget, self).__init__(parent)
        self.id_str = id_str
        self._generateUI()
    def _generateUI(self):
        main_layout = QGridLayout()
        self.setLayout(main_layout)
        title = QLabel("title" + self.id_str)
        main_layout.addWidget(title, 0, 0, 1, 3)
        close_button = QPushButton("-")
        close_button.setFixedWidth(30)
        close_button.clicked.connect(self._close_widget) # add to close the widget
        main_layout.addWidget(close_button, 0, 3, 1, 1)
        spinbox = QSpinBox()
        main_layout.addWidget(spinbox, 1, 0, 1, 4)
    def _close_widget(self):
        self.deleteLater() # main function to close widget

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.id_num = 1
        self._generateUI()
    def _generateUI(self):
        main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)
        item = ItemWidget(str(self.id_num))
        self.main_layout.addWidget(item)
        add_button = QPushButton("+")
        add_button.clicked.connect(self._addItem)
        self.main_layout.addWidget(add_button)
    def _addItem(self):
        self.id_num += 1
        item = ItemWidget(str(self.id_num))
        self.main_layout.insertWidget(self.main_layout.count()-1, item)
    def _deletedItem(self, item):
        self.id_num -= 1
        #for i in range(3):
        #   QApplication.processEvents()
        #self.adjustSize()

def launch():
    app = QApplication(sys.argv)
    widget = MyMainWindow()
    widget.show()
    app.exec_()

launch()