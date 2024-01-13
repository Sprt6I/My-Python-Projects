from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel, QMainWindow, QHBoxLayout
from PySide6.QtCore import Signal
import psutil
import GPUtil
import time
import threading

print('\nPROCESSOR')
print(psutil.cpu_count())
print(psutil.cpu_freq())
print(psutil.cpu_percent())

print('\nHARD DRIVE')
print()

print('\nRAM')
print(psutil.virtual_memory().total)
print(psutil.virtual_memory().available)
print(psutil.virtual_memory().used)
print(psutil.virtual_memory().percent)


print('\nGpu')
gpus = GPUtil.getGPUs()

for gpu in gpus:
   print(gpu.name)

'''print('\nFANS')
arr = psutil.sensors_fans()
for fan in psutil.sensors_fans():
  print(fan, arr[fan][0].current) #Name, usage'''
  
  
class RescourceMonitor__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Rescource Monitor")
    
    self.UI_()
    
  def UI_(self):
    mainWidget = QWidget()
    self.mainLayout = QHBoxLayout()
    
    self.SetCpu_()
    
    self.SetRam_()
    
    self.SetDisk()
    
    mainWidget.setLayout(self.mainLayout)
    
    self.setCentralWidget(mainWidget)
    
    
  def SetCpu_(self):
    cpuLayout = QVBoxLayout()
    cputLabel = QLabel("CPU:")
    cpuLayout.addWidget(cputLabel)
    
    cpuCountLabel = QLabel(f'{psutil.cpu_count()}')
    cpuLayout.addWidget(cpuCountLabel)
    
    self.cpuProcent = QLabel(f'{psutil.cpu_percent()}')
    cpuLayout.addWidget(self.cpuProcent)
    
    self.cpuFrequencyMax = QLabel(f'{psutil.cpu_freq().max}')
    cpuLayout.addWidget(self.cpuFrequencyMax)
    
    self.cpuFrequencyMin = QLabel(f'{psutil.cpu_freq().min}')
    cpuLayout.addWidget(self.cpuFrequencyMin)
    
    threading.Thread(target=self.UpDateCpu_, daemon=True).start()
    
    self.mainLayout.addLayout(cpuLayout)
    
  
  def UpDateCpu_(self):
    while 1:
      self.cpuProcent.setText(f'{psutil.cpu_percent()}%')
      self.cpuFrequencyMax.setText(f'{psutil.cpu_freq().max}')
      self.cpuFrequencyMin.setText(f'{psutil.cpu_freq().min}')
      time.sleep(0.3) 
  
  def SetRam_(self):
    ramLayout = QVBoxLayout()
    
    ramLabel = QLabel('RAM:')
    ramLayout.addWidget(ramLabel)
    
    ramTotal = QLabel(f'{psutil.virtual_memory().total // 1024 //1024//1024} GB')
    ramLayout.addWidget(ramTotal)
    
    self.ramPrecent = QLabel(f'{psutil.virtual_memory().percent}%')
    ramLayout.addWidget(self.ramPrecent)
    
    self.ramAviable = QLabel(f'{psutil.virtual_memory().available //1024 //1024//1024} GB')
    ramLayout.addWidget(self.ramAviable)
    
    self.ramUsed = QLabel(f'{psutil.virtual_memory().used //1024 //1024//1024} GB')
    ramLayout.addWidget(self.ramUsed)
    
    threading.Thread(target=self.UpdateRam_, daemon=True).start()
    
    self.mainLayout.addLayout(ramLayout)
    
  def UpdateRam_(self):
    while 1:
      self.ramPrecent.setText(f'{psutil.virtual_memory().percent}%')
      self.ramAviable.setText(f'{psutil.virtual_memory().available //1024 //1024//1024} GB')
      self.ramUsed.setText(f'{psutil.virtual_memory().used //1024 //1024//1024} GB')
      time.sleep(0.3)
      
  def SetDisk(self):
    diskLayout = QVBoxLayout()
    
    diskLabel = QLabel("DISK:")
    diskLayout.addWidget(diskLabel)
    
    
    
    for disk in psutil.disk_partitions():
      diskProcentage = QLabel(f'{disk.device[:-1]}' + ' | ' + f'{psutil.disk_usage(disk.device).free //1024//1024//1024} GB' + ' | ' + f'{psutil.disk_usage(disk.device).percent}%')
      diskLayout.addWidget(diskProcentage)
    
    
    self.mainLayout.addLayout(diskLayout)
    
    
    
if __name__=="__main__":
  app = QApplication()
  
  win = RescourceMonitor__()
  win.show()
  
  app.exec()
