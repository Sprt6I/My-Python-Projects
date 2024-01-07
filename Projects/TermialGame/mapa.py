import time
class Map__():
  def __init__(self, player):
    self.player = player
    
    self.backPlayerPos = [player.pos[0], player.pos[1]]
    
    self.itemList = []
    self.enemyList = []
    self.backEnemyPos = []
    
  def CreateMap_(self,heigth, width, itemList = [],enemyList = []):
    self.map = []
    self.itemList = itemList
    self.enemyList = enemyList
    
    spec = 0
    for a in range(heigth):
      s = ''
      for b in range(width):
        if a==self.player.pos[0] and b==self.player.pos[1]: #Sets Player On Map
          s+='P'
          continue
        for item in itemList: #Sets Items On Map
          if a==item.x and b==item.y:
            s+='?'
            spec+=1 #For Every Item It Skips One '.'
            
        for enemy in enemyList:
          if a==enemy.x and b==enemy.y:
            self.backEnemyPos.append([enemy.x, enemy.y, '.'])
            s+=enemy.show
            spec+=1
            
        if spec>0: #Here It Skips '.'
          spec-=1
          continue
        
        s+='.'
      self.map.append(s)
      
    
  def ShowMap_(self):
    print('\033c', end='')
    ''' Checks If Player Take Item (Same Position) '''
    for indx, item in enumerate(self.itemList):
      if item.x == self.player.pos[0] and item.y == self.player.pos[1]:
        temp = self.map[item.y]
        print(f"You Found {item.name}, {item.stat[0].upper()+item.stat[1:]}: {self.player.attack} -> {self.player.attack+item.add}")
        self.player.AddAtributes_(item.stat, item.add)
        
        temp = [val if indx!=item.x else '.' for indx, val in enumerate(temp)]
        
        self.map[item.y] = temp
        #print(self.player.PlayerStats_())
        
        self.itemList.pop(indx)
        
    self.RemoveLasPos_()
    
    self.MoveEnemies_()
    

    self.MovePlayer_()
    
    for i in self.map:
      s = ''
      for a in i:
        s+=a
      print(s)
      
  def RemoveLasPos_(self):
    ''' Checks If Player Is At The Same Place As Enemy '''
    for indx, enemy in enumerate(self.enemyList):
      if enemy.x == self.player.pos[1] and enemy.y == self.player.pos[0]:
        print(f"Fight {enemy.name} Vs Player !!!")
        self.Fight_(indx, enemy)
        
    
    ''' Removing Last Player Position '''
    temp = self.map[self.backPlayerPos[0]]
    temp = [val if indx!=self.backPlayerPos[1] else '.' for indx, val in enumerate(temp)]
    self.map[self.backPlayerPos[0]] = temp      
      
  def MoveEnemies_(self):
    ''' Moves Enemies '''
    for indx, enemyPos in enumerate(self.backEnemyPos):
      temp = self.map[enemyPos[0]]
      
      temp = [val if indxx!=enemyPos[1] else enemyPos[2] for indxx, val in enumerate(temp)]
      
      self.map[enemyPos[0]] = temp
      
    
    for enemy in self.enemyList:
      enemy.MoveToPlayer_(self.player)
      
      temp = ''.join(self.map[enemy.x])
      
      placeVal = temp[enemy.y]
      
      temp = [val if indx!=enemy.y else enemy.show for indx, val in enumerate(temp)]
      
      self.map[enemy.x] = temp
      
      self.backEnemyPos.append([enemy.x, enemy.y, placeVal])
    
      
  def MovePlayer_(self):
    ''' Moving Player On Map '''
    temp = ''.join(self.map[self.player.pos[1]])
    
    temp = [val if indx!=self.player.pos[0] else 'P' for indx,val in enumerate(temp)]
    self.map[self.player.pos[1]] = temp
    
    
    ''' Saving Player Last Pos '''
    self.backPlayerPos[0] = self.map.index(temp)
    self.backPlayerPos[1] = self.player.pos[0]
      
  def Fight_(self, indx, enemy):
    while enemy.health>0 and self.player.health>0:
          print(f'Enemy: {enemy.health}, Player: {self.player.health}')
          enemy.health-=self.player.attack
          self.player.health -= enemy.attack
          
          if self.player.health<=0:
            print('You died :/')
            exit()
          elif enemy.health<=0:
            print(f'You killed {enemy.name} !')
            self.enemyList.pop(indx)
            
          
          time.sleep(0.4)
  