class Player__():
  def __init__(self):
    self.pos = [5,5]
    
    self.health = 100
    self.attack = 15
    self.manna = 5
    
  def Move_(self):
    direction = input("Move: (wsad): ")
    
    match direction:
      case 'w': self.pos[1]-=1
      case 's': self.pos[1]+=1
      case 'a': self.pos[0]-=1
      case 'd': self.pos[0]+=1
      case _: self.Move_()
      
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