from email.policy import default


class Map__():
  def __init__(self, player):
    self.player = player
    
    self.backPlayerPos = [player.pos[0], player.pos[1]]
    
  def CreateMap_(self,heigth, width):
    self.map = []
    
    for i in range(heigth):
      self.map.append(['.'*width])
      
    temp = ''.join(self.map[self.player.pos[0]])
    
    temp = [val if indx!=self.player.pos[1] else 'P' for indx,val in enumerate(temp)]
    
    self.map[self.player.pos[0]] = temp
    
  def ShowMap_(self):
    
    ''' Removing Last Player Position '''
    temp = self.map[self.backPlayerPos[0]]
    temp = [val if indx!=self.backPlayerPos[1] else '.' for indx, val in enumerate(temp)]
    self.map[self.backPlayerPos[0]] = temp
    
    ''' Moving Player On Map '''
    temp = ''.join(self.map[self.player.pos[1]])
    
    temp = ['.' if indx!=self.player.pos[0] else 'P' for indx,val in enumerate(temp)]
    self.map[self.player.pos[1]] = temp
    
    
    ''' Saving Player Last Pos '''
    self.backPlayerPos[0] = self.map.index(temp)
    self.backPlayerPos[1] = self.player.pos[0]
    
    for i in self.map:
      s = ''
      for a in i:
        s+=a
      print(s)
        
class Player__():
  def __init__(self):
    self.pos = [5,5]
    
  def Move_(self):
    direction = input("Move: (wsad): ")
    
    match direction:
      case 'w': self.pos[1]-=1
      case 's': self.pos[1]+=1
      case 'a': self.pos[0]-=1
      case 'd': self.pos[0]+=1
      case _: self.Move_()
    
    
class Game__():
  def __init__(self):
    self.player = Player__()
    self.map = Map__(self.player) 
    
    self.map.CreateMap_(10,10)
    self.map.ShowMap_
    
    while True:
      self.player.Move_()
      self.map.ShowMap_()
    


if __name__=="__main__":
  game = Game__()


