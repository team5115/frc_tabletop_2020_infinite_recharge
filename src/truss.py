import pygame
import copy
from colors import *
from units import *

from pygame.math import Vector2



 
#####################################################################
class Truss(pygame.sprite.Sprite):

    def __init__(self, r,angle=22.5,color=GREEN):

        # Call the parent's constructor
        super(Truss,self).__init__()

        self.verbosity=0
        x=r.x
        y=r.y
        use_png=False
        width=12*in_
        height=12*in_

        width=int(width)
        height=int(height)

        if use_png:
            picture = pygame.image.load('./resources/truss.png')
            picture=pygame.transform.scale(picture, (width,height))
            picture= pygame.transform.rotate(picture,angle)
            self.image=picture
        else:
            picture=pygame.Surface((width,height), pygame.SRCALPHA)
            picture.fill(color)
            picture= pygame.transform.rotate(picture,angle)
            self.image = picture


        
        self.image_original=self.image
        self.rect_original=self.image_original.get_rect()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y


