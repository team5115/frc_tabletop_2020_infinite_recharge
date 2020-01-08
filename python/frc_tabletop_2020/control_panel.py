import pygame
import copy
from colors import *
from units import *

from pygame.math import Vector2



 
#####################################################################
class Control_panel(pygame.sprite.Sprite):

    def __init__(self, x, y,color=GREEN,flip_y=False):

        # Call the parent's constructor
        super(Control_panel,self).__init__()

        self.verbosity=0

        width=4*ft_+8*in_
        height=2*ft_+6*in_

        width=int(width)
        height=int(height)

        if True:
            picture = pygame.image.load('./resources/control_panel.png')
                
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

