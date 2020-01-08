import pygame
import copy
from colors import *
from units import *

from pygame.math import Vector2


# TRENCH RUN: a 4 ft. 7 1/2 in. (~141 cm) wide, 18 ft. (~549 cm) deep,
# infinitely tall volume that is bounded by the guardrail, the edge of
# the TRENCH vertical support closest to the center of the FIELD, and
# ALLIANCE colored tape. The TRENCH RUN includes the ALLIANCE colored
# tape.

 
#####################################################################
class Trench_run(pygame.sprite.Sprite):

    def __init__(self, x, y,color=YELLOW,flip_y=False):

        # Call the parent's constructor
        super(Trench_run,self).__init__()

        self.verbosity=0

        height=4*ft_+7.5*in_
        width=18*ft_
        angle=0

        width=int(width)
        height=int(height)

        
        if True:

            if color==BLUE_HAB0:
                picture = pygame.image.load('./data/hab_zone_ramp_blue.png')
            else:
                picture = pygame.image.load('./data/hab_zone_ramp_red.png')
                
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

#        if (flip_x==True):
 #           self.rect.x=x-width
