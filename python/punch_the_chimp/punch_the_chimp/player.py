import pygame
import player
from colors import *


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y,color=BLUE):
        """Constructor function"""
        # Call the parent's constructor
        super(Player,self).__init__()

        # Set height, width
        width=15
        length=38
        
#        self.image = pygame.Surface([38, 15])
        self.image = pygame.Surface((width,length), pygame.SRCALPHA)
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

        #self.pointing_x=0
        #self.pointing_y=0
        self.delta_angle=0
        self.angle=0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y


    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if (self.delta_angle !=0):
            self.angle += self.delta_angle
            self.angle = self.angle % 360
            self.rotate_rect(self.angle)
            
            
    def rotate_rect(self,angle):
        """spin the monkey image"""
        center = self.rect.center
        rotate = pygame.transform.rotate
        self.image = rotate(self.image, angle)
        self.rect = self.image.get_rect(center=center)

    def rotate(self,delta_angle):
        self.delta_angle=delta_angle

        
