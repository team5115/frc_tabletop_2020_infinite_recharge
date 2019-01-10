import pygame
import player
import copy
from colors import *

from pygame.math import Vector2



 
#####################################################################
class Cargo_ship(pygame.sprite.Sprite):

    def __init__(self, x, y,color=GREEN):

        # Call the parent's constructor
        super(Cargo_ship,self).__init__()

        self.verbosity=0

        width=40.5+21.75+21.75*2
        height=21.75*3
   

        
        self.image = pygame.Surface((width,height), pygame.SRCALPHA)
        self.image.fill(color)


        self.image_original=self.image
        self.rect_original=self.image_original.get_rect()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
