import pygame
import player
from colors import *

from pygame.math import Vector2


# the rect element is used to blit the sprite

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y,color=BLUE, angle=45):
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
        self.vx = 0
        self.vy = 0

        self.position= Vector2(x,y)
        self.heading= Vector2(0,0)
        self.velocity= Vector2(0,0)
#        self.accel= Vector2(0,0)

#        self.heading.from_polar([1,angle])

        self.set_heading_angle(angle)
        
    def set_heading_angle(self,theta):
        self.heading.from_polar([1,theta])
        self.rotate_rect(self.get_heading_angle())
               
    def get_heading_angle(self):
        return self.heading.as_polar()[1]
        
    def changespeed(self, a_x, a_y):
         """ Change the speed of the player"""
         self.velocity.x += a_x
         self.velocity.y += a_y

    def update(self):
        dt=1;
        self.position = self.position+dt*self.velocity
        self.update_rect()  
        
    def update_rect(self):
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        
        #if (self.delta_angle !=0):
        #    self.angle += self.delta_angle
        #    self.angle = self.angle % 360
        # self.rotate_rect(self.get_heading_angle())

            
            
    def rotate_rect(self,angle):
        """spin the monkey image"""
        center = self.rect.center
        rotate = pygame.transform.rotate
        self.image = rotate(self.image, angle)
        self.rect = self.image.get_rect(center=center)

    def rotate(self,delta_angle):
        self.delta_angle=delta_angle

        
