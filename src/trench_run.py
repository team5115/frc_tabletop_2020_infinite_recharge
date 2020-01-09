import pygame
import copy
from colors import * 
import loader_utils
from colors import *
from units import *

from pygame.math import Vector2


# TRENCH RUN: a 4 ft. 7 1/2 in. (~141 cm) wide, 18 ft. (~549 cm) deep,
# infinitely tall volume that is bounded by the guardrail, the edge of
# the TRENCH vertical support closest to the center of the FIELD, and
# ALLIANCE colored tape. The TRENCH RUN includes the ALLIANCE colored
# tape.

 




class Trench_run(pygame.sprite.Sprite):
    """ Trench_run the player can run into. """
    def __init__(self, x, y,color):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super(Trench_run,self).__init__()


        height=4*ft_+7.5*in_
        width=18*ft_
        
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
