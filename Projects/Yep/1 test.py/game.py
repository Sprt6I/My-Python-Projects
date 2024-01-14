import pygame as pg
from OpenGL.GL import *

class App__():
    def __init__(self):
        self.MaxFps = 60
        
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        
        glClearColor(0.1,0.5,0.2,1)
        
        self.MainLoop_()
        
    def MainLoop_(self):
        while 1:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    return 0
                
            
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()
            
            self.clock.tick(self.MaxFps)
            
    def Quit_(self):
        pg.quit()
        
        
if __name__=="__main__":
    app = App__()