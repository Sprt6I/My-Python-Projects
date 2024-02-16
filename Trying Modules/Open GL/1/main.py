from OpenGL.GL import * #type: ignore
from OpenGL.GLUT import * #type: ignore
from OpenGL.GLU import * #type: ignore

window = 0
width, height = 500,400

def DrawRectangle_(x, y, width, height):
  glBegin(GL_QUADS)
  glVertex2f(x, y)
  glVertex2f(x+width, y)
  glVertex2f(x+width, y+height)
  glVertex2f(x, y+height)
  glEnd()

def Refresh2D_(width, height):
  glViewport(0,0, width, height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho(0.0,width,0.0,height,0.0,1.0)
  glMatrixMode (GL_MODELVIEW)
  glLoadIdentity()

def draw():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #type: ignore
  glLoadIdentity()
  Refresh2D_(width, height)
  
  glColor3f(0.0,0.0,1.0)
  DrawRectangle_(200,200,25,25)
  
  glutSwapBuffers()
  

glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH) #type: ignore
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("noobtuts.com")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop() 