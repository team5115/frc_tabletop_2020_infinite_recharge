import pygame
import player
from colors import *

from pygame.math import Vector2


# the rect element is used to blit the sprite

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y,color=BLUE, angle=2):

        # Call the parent's constructor
        super(Player,self).__init__()

        self.verbosity=0
        

        width=15
        length=38
        self.image = pygame.Surface((width,length), pygame.SRCALPHA)
        self.image.fill(color)


        self.image_original=self.image
        self.rect_original=self.image_original.get_rect()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
        
        self.position= Vector2(x,y)
        self.heading= Vector2(0,0)
        #self.velocity= Vector2(0,0)
        self.rotation_rate=0
        self.set_heading_angle(angle)
        self.forward_speed=0
        self.side_speed=0
        
    def set_heading_angle(self,theta):
        self.heading.from_polar([1,theta])
                       
    def get_heading_angle(self):
        return self.heading.as_polar()[1]
        
    def changespeed(self, a_x, a_y):
        if a_y !=0:
            self.change_forward_speed(a_y)
        elif a_x !=0:
            self.change_side_speed(a_x)        

    def change_forward_speed(self, dv):
        self.forward_speed+=dv

    def change_side_speed(self, dv):
        self.side_speed+=dv

    def update(self):
        dt=1;

        theta=self.get_heading_angle()

        velocity=Vector2(self.side_speed,self.forward_speed)
        velocity.rotate_ip(-theta)
#        velocity.from_polar(self.forward_speed,theta)
        
        self.position = self.position+dt*velocity

        delta_angle=self.rotation_rate*dt
        self.heading.rotate_ip(delta_angle)

        if self.verbosity > 5:
            print "center=",self.position,
            print "delta_angle=",delta_angle,
            print "heading_angle=",self.get_heading_angle()
        

        self.update_rect_heading_and_position()  

    def update_rect_heading_and_position(self):
        angle= self.get_heading_angle()
        rect_orig=self.image_original.get_rect()
        
        self.image = pygame.transform.rotate(self.image_original, angle)
        ### get the center from the original image
        self.rect = self.image.get_rect(center=rect_orig.center)

        #now translate the whole thing
        self.rect.move_ip(self.position.x,self.position.y)

    def rotate(self,delta_angle):
        self.rotation_rate+=delta_angle
        
        
        
