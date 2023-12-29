import pytube as yt
from PySide6.QtWidgets import QLabel, QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QHBoxLayout, QComboBox
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt

PATH = "/home/deleted/Videos/"

link = "https://www.youtube.com/watch?v=QsR8zBh6EdE"

ytVid = yt.YouTube(link)

"""for stream in ytVid.streams:
  if stream.resolution:
    print(stream.resolution)"""
    
    
class ShadowLineEdit(QLineEdit): #Special QLabel with "Shadow text"
   def __init__(self, *args, **kwargs):
       super(ShadowLineEdit, self).__init__(*args, **kwargs)

   def paintEvent(self, event):
       painter = QPainter(self)
       painter.setPen(Qt.gray)
       painter.drawText(self.rect(), Qt.AlignCenter, self.placeholderText())
       super(ShadowLineEdit, self).paintEvent(event)
       
       
       
    
class YtDownloader(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Yt Downloader")
    
    
    self.UI_()

  def UI_(self):
    mainLayout = QVBoxLayout()
    
    appName = QLabel("Yt Downloader")
    mainLayout.addWidget(appName)
    
    pathToVideo = ShadowLineEdit()
    pathToVideo.setPlaceholderText("PATH TO VIDEO: https://www.youtube.com/watch?v=QsR8zBh6EdE")
    mainLayout.addWidget(pathToVideo)
    
    pathToSave = ShadowLineEdit()
    pathToSave.setPlaceholderText("PATH TO SAVE: /home/deleted/Desktop")
    mainLayout.addWidget(pathToSave)
    
    self.warningLabel = QLabel()
    self.warningLabel.setStyleSheet("color: red;")
    mainLayout.addWidget(self.warningLabel)
    
    qualities = QComboBox()
    
    arr= []
    for stream in ytVid.streams:
      if stream.resolution and stream.resolution not in arr:
        arr.append(stream.resolution)
    
    arr.sort()
    
    arr = arr[::-1]
    
    for i in arr:
      qualities.addItem(i)
        
    mainLayout.addWidget(qualities)
    
    sumbmitButton = QPushButton("Download")
    sumbmitButton.clicked.connect(lambda: self.Download(pathToVideo.text(), pathToSave.text(), qualities.currentText()))
    mainLayout.addWidget(sumbmitButton)
      
    
    self.setLayout(mainLayout)
    
  def Download(self, pathToVid: str, pathToSave: str, quality:str) -> int:
    if not pathToVid:
      self.warningLabel.setText("No Video Path !")
      return 0
    if not pathToSave:
      self.warningLabel.setText("No Path To Save Video !")
      return 0
    if not quality:
      self.warningLabel.setText("No Quality Choosen !")
    
    print(pathToVid)
    print(pathToSave)
    print(quality)
    
    try:
      ytVid.streams.filter(res=quality).first().download(pathToSave)
      return 1
    except:
      self.warningLabel.setText("Some Error Occurred :/")
      return 0
      
    
    
if __name__ == "__main__":
  app = QApplication()
  appWindow = YtDownloader()
  appWindow.show()
  app.exec()
#ytVid.streams.filter(res="720p").first().download(PATH)