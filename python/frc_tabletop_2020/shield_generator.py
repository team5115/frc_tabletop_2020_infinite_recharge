import pygame
import copy
from colors import *
from units import *

from pygame.math import Vector2



 
#####################################################################
class Shield_generator(pygame.sprite.Sprite):

    def __init__(self, x, y,angle=0):

        # Call the parent's constructor
        super(Shield_generator,self).__init__()

        self.verbosity=0

        #angle=22.5
        #angle=0
        width=14*ft_+0.75*in_
        height=13*ft_+1.5*in_

        width=int(width)
        height=int(height)

        use_png=True
        
        if use_png:
            picture = pygame.image.load('./resources/shield_generator.png')
            picture=pygame.transform.scale(picture, (width,height))
            picture= pygame.transform.rotate(picture,angle)
            self.image=picture

        else:
            picture=pygame.Surface((width,height), pygame.SRCALPHA)
            color=GREEN
            picture.fill(color)
            picture= pygame.transform.rotate(picture,angle)
            self.image = picture




        self.image_original=self.image
        self.rect_original=self.image_original.get_rect()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        
