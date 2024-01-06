from email.policy import default


class Map__():
  def __init__(self, player):
    self.player = player
    
  def CreateMap_(self,heigth, width):
    self.map = []
    
    for i in range(heigth):
      self.map.append([str(i)*width])
      
    temp = ''.join(self.map[self.player.pos[0]])
    print(temp)
    print(str(self.player.pos[1]))
    
    temp = [val if indx!=self.player.pos[1] else 'P' for indx,val in enumerate(temp)]
    
    print(temp)
    self.map[self.player.pos[0]] = temp
    
  def ShowMap_(self):
    
    temp = ''.join(self.map[self.player.pos[0]])
    #print(temp)
    #print(str(self.player.pos[1]))
    
    temp = [val if indx!=self.player.pos[1] else 'P' for indx,val in enumerate(temp)]
    
    #print(temp)
    self.map[self.player.pos[0]] = temp
    
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
    
    


if __name__=="__main__":
  game = Game__()


