import pygame
import copy
from colors import * 
import loader_utils

from pygame.math import Vector2







class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height,color=YELLOW):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super(Wall,self).__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
