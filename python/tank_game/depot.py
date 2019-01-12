import pygame
import copy
from colors import *
from units import *

from pygame.math import Vector2



 
#####################################################################
class Depot(pygame.sprite.Sprite):

    def __init__(self, x, y,color=YELLOW,flip_x=False, flip_y=False):

        # Call the parent's constructor
        super(Depot,self).__init__()

        self.verbosity=0

        width=3*ft_+7*in_+5.0/8.0*in_
        height=1*ft_+9*in_+3.0/4.0*in_
        
        width=int(width)
        height=int(height)

        if True:
            picture = pygame.image.load('./data/depot.png')
            #picture= pygame.transform.rotate(picture,angle)
            self.image=pygame.transform.scale(picture, (width,height))
        else:        
            self.image = pygame.Surface((width,height), pygame.SRCALPHA)
            self.image.fill(color)


        self.image_original=self.image
        self.rect_original=self.image_original.get_rect()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        if (flip_y==True):
            self.rect.y=y-height

        if (flip_x==True):
            self.rect.x=x-width
