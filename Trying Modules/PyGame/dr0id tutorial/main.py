import pygame

class Game__():
  def __init__(self):
    pygame.init()
    
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    
    pygame.display.set_caption("My Game")
    
    screen = pygame.display.set_mode((240,180))
    
    screen.fill((20,90,80))
    
    
    image = pygame.image.load("Trying Modules/PyGame/dr0id tutorial/player.png")
    image.set_colorkey((255,0,255))
    image.set_alpha(128)
    screen.blit(image, (26,26))
    
    pygame.display.flip()
    
    
    self.Game_()
    
  def Game_(self):
    while 1:
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          return 0
        
        
        
        
if __name__=="__main__":
  game = Game__()