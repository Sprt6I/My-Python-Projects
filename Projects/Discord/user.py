from PySide6.QtWidgets import QSizePolicy, QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QMainWindow, QWidget, QHBoxLayout
import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
print(mydb)

'''create servers database with servers with channels, users like discord SQL (Yep chat gpt)

idk....

CREATE TABLE Servers (
   ServerId INT PRIMARY KEY,
   ServerName VARCHAR(255) NOT NULL
);

CREATE TABLE Channels (
   ChannelId INT PRIMARY KEY,
   ChannelName VARCHAR(255) NOT NULL,
   ServerId INT,
   FOREIGN KEY (ServerId) REFERENCES Servers(ServerId)
);

CREATE TABLE Users (
   UserId INT PRIMARY KEY,
   Username VARCHAR(255) NOT NULL,
   PasswordHash VARCHAR(255) NOT NULL
);

CREATE TABLE UserChannels (
   UserId INT,
   ChannelId INT,
   PRIMARY KEY (UserId, ChannelId),
   FOREIGN KEY (UserId) REFERENCES Users(UserId),
   FOREIGN KEY (ChannelId) REFERENCES Channels(ChannelId)
);


'''
class Discord__(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle('Discord')
    
    self.UI_()
    
  def UI_(self):
    self.mainWidget = QWidget()
    self.mainLayout = QHBoxLayout()
    
    self.serverList = QVBoxLayout()
    self.channelsList = QVBoxLayout()
    self.usersList = QVBoxLayout()
    
    