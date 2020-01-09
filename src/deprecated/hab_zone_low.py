import pygame
import player
import copy
from colors import *

from pygame.math import Vector2



 
#####################################################################
class Hab_zone(pygame.sprite.Sprite):

    def __init__(self, x, y,color=GREEN,angle=0):

        # Call the parent's constructor
        super(Hab_zone,self).__init__()

        self.verbosity=0

        width=3*12
        height=3*12*3

        if True:
            picture = pygame.image.load('./data/hab_zone.png')
            picture= pygame.transform.rotate(picture,angle)
            self.image=pygame.transform.scale(picture, (width,height))
        else:        
            self.image = pygame.Surface((width,height), pygame.SRCALPHA)
            self.image.fill(color)


        self.image_original=self.image
        self.rect_original=self.image_original.get_rect()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = y

        if (angle==180):
            self.rect.x=x-width
