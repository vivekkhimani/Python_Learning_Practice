import pygame,sys
from pygame.locals import *

pygame.init()
new_surface = pygame.display.set_mode((600,600))

imgSurface = pygame.image.load(Knot_Class.jpg)
new_surface.blit(imgSurface,(0,0))

