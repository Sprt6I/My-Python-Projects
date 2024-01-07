class Map__():
  def __init__(self, player):
    self.player = player
    
    self.backPlayerPos = [player.pos[0], player.pos[1]]
    
    self.itemList = []
    
  def CreateMap_(self,heigth, width, itemList = [],enemyList = []):
    self.map = []
    self.itemList = itemList
    
    spec = 0
    for a in range(heigth):
      s = ''
      for b in range(width):
        if a==self.player.pos[0] and b==self.player.pos[1]:
          s+='P'
          continue
        for item in itemList:
          if a==item.x and b==item.y:
            s+='?'
            spec+=1
        if spec>0:
          spec-=1
          continue
        s+='.'
      self.map.append(s)
      
    
  def ShowMap_(self):
    
    ''' Checks If Player Take Item (Same Position) '''
    for item in self.itemList:
      if item.x == self.player.pos[0] and item.y == self.player.pos[1]:
        print(self.player.PlayerStats_())
        print(item.name)
        self.player.AddAtributes_("attack", item.stat)
        print(self.player.PlayerStats_())
    
    ''' Removing Last Player Position '''
    temp = self.map[self.backPlayerPos[0]]
    temp = [val if indx!=self.backPlayerPos[1] else '.' for indx, val in enumerate(temp)]
    self.map[self.backPlayerPos[0]] = temp
    
    ''' Moving Player On Map '''
    temp = ''.join(self.map[self.player.pos[1]])
    
    temp = [val if indx!=self.player.pos[0] else 'P' for indx,val in enumerate(temp)]
    self.map[self.player.pos[1]] = temp
    
    
    ''' Saving Player Last Pos '''
    self.backPlayerPos[0] = self.map.index(temp)
    self.backPlayerPos[1] = self.player.pos[0]
    
    for i in self.map:
      s = ''
      for a in i:
        s+=a
      print(s)