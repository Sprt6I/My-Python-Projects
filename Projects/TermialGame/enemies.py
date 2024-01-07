import random

class Zombie__():
  def __init__(self, x:int, y: int):
    self.name = 'Zombie'
    self.show = 'Z'
    self.x = x
    self.y = y
    
    self.health = random.randint(25, 67)
    self.attack = random.randint(8, 12)
    
  def MoveToPlayer_(self, player):
    if player.pos[1] > self.x: self.x+=1
    elif player.pos[1] < self.x: self.x-=1
    #elif player.pos[0] < self.y: self.y-=1
    #elif player.pos[1] > self.y: self.y+=1
    
    
    
    
    
class Necromancer__():
  def __init__(self):
    self.name = "Necromancer"
    
    self.health = random.randint(30, 100)
    self.maxSummons = random.randint(2,5)
    
    
    
    