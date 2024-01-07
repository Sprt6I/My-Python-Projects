from mapa import Map__
from player import Player__
from items import *
from enemies import *

    
class Game__():
  def __init__(self):
    self.player = Player__()
    self.map = Map__(self.player) 
    
    self.map.CreateMap_(10,10, itemList=[Sword__('Weak Sword',5,2,2)], enemyList=[Zombie__(1,3)])
    self.map.ShowMap_()
    
    while True:
      self.player.Move_()
      self.map.ShowMap_()
    


if __name__=="__main__":
  game = Game__()


