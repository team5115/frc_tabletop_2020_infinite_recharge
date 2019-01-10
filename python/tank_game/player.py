import pygame
import player
from colors import *

from pygame.math import Vector2

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
        self.bounding_box = self.image.get_rect()
        self.bounding_box.x = x
        self.bounding_box.y = y

        # -- Attributes
        # Set speed vector
        self.vx = 0
        self.vy = 0

        #self.pointing_x=0
        #self.pointing_y=0
        #self.delta_angle=0
        #self.angle=0

        self.position= Vector2(x,y)
        self.heading= Vector2(0,0)
        self.velocity= Vector2(0,0)
#        self.accel= Vector2(0,0)

    def changespeed(self, a_x, a_y):
         """ Change the speed of the player"""
         self.velocity.x += a_x
         self.velocity.y += a_y

    # def change_speed(self, acceleration):
    #     self.vel=self.vel+acceleration


    def update(self):
        dt=1;
        self.position = self.position+dt*self.velocity


        self.bounding_box.x = self.position.x
        self.bounding_box.y = self.position.y
        
        #if (self.delta_angle !=0):
        #    self.angle += self.delta_angle
        #    self.angle = self.angle % 360
        #    self.rotate_bounding_box(self.angle)
            
            
    def rotate_bounding_box(self,angle):
        """spin the monkey image"""
        center = self.bounding_box.center
        rotate = pygame.transform.rotate
        self.image = rotate(self.image, angle)
        self.bounding_box = self.image.get_rect(center=center)

    def rotate(self,delta_angle):
        self.delta_angle=delta_angle

        
