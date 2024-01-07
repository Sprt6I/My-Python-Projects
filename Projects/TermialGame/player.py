class Player__():
  def __init__(self):
    self.pos = [5,5]
    
    self.health = 100
    self.attack = 15
    self.manna = 5
    
  def Move_(self, mapHight:int, mapWidth:int):
    direction = input("Move: (wsad): ")

    match direction:
      case 'w': 
        if self.pos[1]-1 >= 0:
          self.pos[1]-=1
        else:
          self.Move_(mapHight, mapWidth)
          
      case 's': 
        if self.pos[1]+1 < mapHight:
          self.pos[1]+=1
        else:
          self.Move_(mapHight, mapWidth)
          
      case 'a': 
        if self.pos[0]-1 >= 0:
          self.pos[0]-=1
        else:
          self.Move_(mapHight, mapWidth)
          
      case 'd': 
        if self.pos[0]+1 < mapWidth:
          self.pos[0]+=1
        else:
          self.Move_(mapHight, mapWidth)
          
      case _: self.Move_(mapHight, mapWidth)
    
      
  def AddAtributes_(self, stat, value):
    if stat=='health':
      self.health+=value
    elif stat=='attack':
      self.attack+=value
    elif stat == "manna":
      self.manna+=value
    else:
      raise ValueError(f"Wrong argument {stat}, must be: (health, attack, manna)")
    
  def PlayerStats_(self):
    print(f"health: {self.health}\nattack: {self.attack}\nmanna: {self.manna}")