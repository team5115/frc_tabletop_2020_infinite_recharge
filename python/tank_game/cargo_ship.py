import pygame
import copy
from colors import *
from units import *

from pygame.math import Vector2



 
#####################################################################
class Cargo_ship(pygame.sprite.Sprite):

    def __init__(self, x, y,color=GREEN,angle=180):

        # Call the parent's constructor
        super(Cargo_ship,self).__init__()

        self.verbosity=0

        width=95.88*in_*2
        height=45.50*in_

        width=int(width)
        height=int(height)

        if True:
            picture = pygame.image.load('./data/cargo.png')
            picture= pygame.transform.rotate(picture,angle)
            self.image=pygame.transform.scale(picture, (width,height))
        else:        
            self.image = pygame.Surface((width,height), pygame.SRCALPHA)
            self.image.fill(color)


        self.image_original=self.image
        self.rect_original=self.image_original.get_rect()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        
