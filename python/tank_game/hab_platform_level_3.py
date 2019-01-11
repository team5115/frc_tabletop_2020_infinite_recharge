import pygame
import player
import copy
from colors import *
from units import *

from pygame.math import Vector2



 
#####################################################################
class Hab_platform_level_3(pygame.sprite.Sprite):

    def __init__(self, x, y,color=YELLOW,flip_x=False):

        # Call the parent's constructor
        super(Hab_platform_level_3,self).__init__()

        self.verbosity=0

        width=4*ft_
        depth=4*ft_

        if False:
            picture = pygame.image.load('./data/hab_zone.png')
            picture= pygame.transform.rotate(picture,angle)
            self.image=pygame.transform.scale(picture, (width,depth))
        else:        
            self.image = pygame.Surface((width,depth), pygame.SRCALPHA)
            self.image.fill(color)


        self.image_original=self.image
        self.rect_original=self.image_original.get_rect()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = y

        if (flip_x==True):
            self.rect.x=x-width
