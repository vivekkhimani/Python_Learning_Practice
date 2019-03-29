import abc,pygame,sys
from pygame.locals import *

class Drawable (metaclass = abc.ABCMeta):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        
    def getLoc (self):
        return (self.__x, self.__y)
    
    def setLoc (self,p):
        self.__x = p[0]
        self.__y = p[1]
        
    
    def draw (self,surface):
        pass
    
class House (Drawable):
    def __init__ (self, x=0, y=0, color = (0,0,0)):
        super().__init__(x,y)
        self.color = color
    def draw (self, surface):
        loc = self.getLoc()
        pygame.draw.rect(surface, self.color, [loc[0]-15, loc[1]-10, 30, 20])
        
pygame.init()
DISPLAYSURF = pygame.display.set_mode ((600,600))
drawables = []
drawables.append(House(100,100,(255,255,255)))
while True:
    DISPLAYSURF.fill((255,255,255))
    for drawable in drawables:
        drawable.draw(DISPLAYSURF)



