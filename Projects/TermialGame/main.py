from mapa import Map__
from player import Player__
from items import *
from enemies import *

    
class Game__():
  def __init__(self):
    self.player = Player__()
    self.map = Map__(self.player) 
    
    mapHight = 10
    mapWidth = 10
    
    self.map.CreateMap_(mapHight,mapWidth, itemList=[Sword__('Weak Sword',"attack",5,2,2)], enemyList=[Zombie__(1,3)])
    self.map.ShowMap_()
    
    while True:
      self.player.Move_(mapHight, mapWidth)
    
      self.map.ShowMap_()
    


if __name__=="__main__":
  game = Game__()


