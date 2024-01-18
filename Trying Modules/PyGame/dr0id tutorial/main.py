import pygame

class Game__():
  def __init__(self):
    pygame.init()
    
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    
    pygame.display.set_caption("My Game")
    
    self.screen = pygame.display.set_mode((240,180))
    
    self.screen.fill((20,90,80))
    
    self.Player_()
    
    
    
    self.Game_()
    
  def Player_(self):
    self.xpos = 50
    self.ypos = 50
    
    self.xStep = 2
    self.yStep = 2
    
    self.image = pygame.image.load("Trying Modules/PyGame/dr0id tutorial/player.png")
    self.image.set_colorkey((255,0,255))
    self.image.set_alpha(128)
    self.screen.blit(self.image, (self.xpos,self.ypos))
    
    pygame.display.flip()
    
  def Game_(self):
    while 1:
      for event in pygame.event.get():` -`
        if event.type==pygame.QUIT:
          return 0
        elif event.type==pygame.KEYDOWN:
          if event.key==pygame.K_w and self.ypos-self.yStep>0:
            self.screen.fill((20,90,80))
            self.ypos-=self.yStep
            self.screen.blit(self.image, (self.xpos,self.ypos))
        
        
        pygame.display.flip()
        
        
        
        
        
        
if __name__=="__main__":
  game = Game__()