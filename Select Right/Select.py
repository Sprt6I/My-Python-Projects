from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import random
import time

app = QApplication(sys.argv)


class Select(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select")
        arr = ['capital', 'a', 'is', 'with', 'phrase', 'an', 'which', 'and', 'wish,', 'expresses', 'command,', 'appropriate', 'performance', 'punctuation,', 'the', 'that', 'characteristic', 'distinguished', 'pauses', 'stress,', 'syntactic', 'phrases', 'letter', 'exclamation,', 'word,', 'concludes', 'pitch,', 'speaking', 'end', 'clause,', 'writing', 'or', 'usually', 'assertion,', 'action,', 'begins', 'in', 'by', 'forming', 'of', 'group', 'clauses', 'unit', 'patterns', 'question,']
        
        RandomArr = [random.choice(arr) for _ in arr]
        self.target = random.choice(RandomArr) #Target to select
        RandomArr = ' '.join(RandomArr)
        
        self.start_time = time.perf_counter() #Takes starting time
        
        
        
        lay0 = QVBoxLayout()
        
        targetlabel = QLabel(f'Target: {self.target}') #Text with target to select
        lay0.addWidget(targetlabel)
        
        self.textHolder = QTextEdit() #Pleace where text is shown
        self.textHolder.selectionChanged.connect(self.SelChanged)
        self.textHolder.setText(RandomArr)
        lay0.addWidget(self.textHolder)
        
        self.setLayout(lay0)
        
        
    def SelChanged(self): #If selected word changes:
        if self.textHolder.textCursor().selectedText()==self.target: #checks if selected word == target word
            end_time = time.perf_counter() #Takes time on the end of game
            
            message = QMessageBox() #Shows message
            message.setWindowTitle("You Won !!!")
            message.setInformativeText(f"It Took You: {round(end_time - self.start_time, 2)}s") #Shows how long it took u
            message.exec()
            app.quit()
        
        

window = Select()
window.show()
app.exec()
        