import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode ((400, 300))
MYSURF = pygame.display.set_mode((500,800))
pygame.display.set_caption ('Hello World')
pygame.draw.line(DISPLAYSURF, (255,255,255), (0,0), (50,50))
pygame.draw.rect(DISPLAYSURF, (255,255,255), (0,0,25,25))
pygame.draw.rect(MYSURF, (255,255,255), (25,25,100,100))
pygame.draw.circle(MYSURF, (255,255,255), (150,150), 70)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()