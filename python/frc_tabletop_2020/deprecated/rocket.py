import pygame
import copy
from colors import *
from units import *

from pygame.math import Vector2



 
#####################################################################
class Rocket(pygame.sprite.Sprite):

    def __init__(self, x, y,color=GREEN,flip_y=False):

        # Call the parent's constructor
        super(Rocket,self).__init__()

        self.verbosity=0

        width=48*in_
        height=24.8*in_

        width=int(width)
        height=int(height)

        if True:
            if (color==RED):
                picture = pygame.image.load('./data/red_rocket.png')
            else:
                picture = pygame.image.load('./data/blue_rocket.png')
                
            if not (flip_y):
                angle=180
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
        self.rect.y = y

        if (flip_y==True):
            self.rect.y=y-height

