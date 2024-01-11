from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel, QMainWindow 
import psutil

print('\nPROCESSOR')
print(psutil.cpu_count())
print(psutil.cpu_freq())
print(psutil.cpu_percent())

print('\nHARD DRIVE')
print(psutil.disk_usage('/').percent)

print('\nRAM')
print(psutil.virtual_memory().total)
print(psutil.virtual_memory().available)
print(psutil.virtual_memory().used)
print(psutil.virtual_memory().percent)

print('\nFANS')
arr = psutil.sensors_fans()
for fan in psutil.sensors_fans():
  print(fan, arr[fan][0].current) #Name, usage
  
  
class RescourceMonitor__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Rescource Monitor")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    
    cpuLayout = QVBoxLayout()
    
    
    cputLabel = QLabel("CPU:")
    cpuLayout.addWidget(cputLabel)
    
    cpuCountLabel = QLabel(f'{psutil.cpu_count()}')
    cpuLayout.addWidget(cpuCountLabel)
    
    cpuFrequencyMax = QLabel(f'{psutil.cpu_freq().max}')
    cpuLayout.addWidget(cpuFrequencyMax)
    
    cpuFrequencyMin = QLabel(f'{psutil.cpu_freq().min}')
    cpuLayout.addWidget(cpuFrequencyMin)
    
    
    mainLayout.addLayout(cpuLayout)
    
    
    mainWidget.setLayout(mainLayout)
    
    self.setCentralWidget(mainWidget)
    
    
    
    
if __name__=="__main__":
  app = QApplication()
  
  win = RescourceMonitor__()
  win.show()
  
  app.exec()
