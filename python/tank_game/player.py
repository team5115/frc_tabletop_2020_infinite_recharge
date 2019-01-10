import pygame
import player
from colors import *

from pygame.math import Vector2


# the rect element is used to blit the sprite

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y,color=BLUE, angle=2):
        """Constructor function"""
        # Call the parent's constructor
        super(Player,self).__init__()

        self.verbosity=0
        
        # Set height, width
        width=15
        length=38
      #  width=length
        
#        self.image = pygame.Surface([38, 15])
        self.image = pygame.Surface((width,length), pygame.SRCALPHA)
        self.image.fill(color)

        self.image_original=self.image
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rect_original=self.image_original.get_rect()
        
        self.position= Vector2(x,y)
        self.heading= Vector2(0,0)
        self.velocity= Vector2(0,0)
        self.rotation_rate=0
        self.set_heading_angle(angle)
        
    def set_heading_angle(self,theta):
        self.heading.from_polar([1,theta])
        #self.rotate_rect(self.get_heading_angle())
               
    def get_heading_angle(self):
        return self.heading.as_polar()[1]
        
    def changespeed(self, a_x, a_y):
         """ Change the speed of the player"""
         self.velocity.x += a_x
         self.velocity.y += a_y

    def update(self):
        dt=1;
        self.position = self.position+dt*self.velocity

        delta_angle=self.rotation_rate*dt
        self.heading.rotate_ip(delta_angle)

        if self.verbosity > 5:
            print "center=",self.position,
            print "delta_angle=",delta_angle,
            print "heading_angle=",self.get_heading_angle()
        

        self.update_rect_heading_and_position()  
#        self.update_rect_position()
        
#    def update_rect_position(self):
#        self.rect.x = self.position.x
#        self.rect.y = self.position.y

    def update_rect_heading_and_position(self):
        #center_old = self.rect.center
        #rotate = pygame.transform.rotate
        angle= self.get_heading_angle()
        rect_orig=self.image_original.get_rect()
        
        self.image = pygame.transform.rotate(self.image_original, angle)
        ### get the center from the original image
        self.rect = self.image.get_rect(center=rect_orig.center)

        #now translate the whole thing
        self.rect.move_ip(self.position.x,self.position.y)

  

    def rotate(self,delta_angle):
        self.rotation_rate+=delta_angle
        
        
        
