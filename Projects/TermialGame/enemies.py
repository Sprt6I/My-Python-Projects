import random

class Zombie__():
  def __init__(self, x:int, y: int):
    self.name = 'Zombie'
    self.show = 'Z'
    self.x = x
    self.y = y
    
    self.health = random.randint(25, 67)
    self.attack = random.randint(8, 12)
    self.goRightSite = random.randint(40, 75)
    
  def MoveToPlayer_(self, player):
    moveChance = random.randint(0,100)
    
    if self.goRightSite>moveChance:
      if player.pos[1] > self.x: self.x+=1
      elif player.pos[1] < self.x: self.x-=1
      elif player.pos[0] > self.y: self.y+=1
      elif player.pos[0] < self.y: self.y-=1
    else:
      moveWay = random.randint(0,3)
      
      match moveWay:
        case 0: self.x+=1
        case 1: self.x-=1
        case 2: self.y+=1
        case 3: self.y-=1
        case _:
          raise ValueError(f"Wrong Value {moveWay}, range <0,3> !")
    
    
    
    
    
class Necromancer__():
  def __init__(self):
    self.name = "Necromancer"
    
    self.health = random.randint(30, 100)
    self.maxSummons = random.randint(2,5)
    
    
    
    