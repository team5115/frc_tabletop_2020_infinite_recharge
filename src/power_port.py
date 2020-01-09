import pygame
import copy
from colors import *
from units import *
import sprite_rect
from pygame.math import Vector2

WIDTH=2*ft_
HEIGHT=2*ft_+10*in_

 
#####################################################################
class Power_port(sprite_rect.Sprite_rect):

    def __init__(self, r_origin,color=GREEN,flip_y=False):
        
        angle=0
        if flip_y:
            angle=180
            
        use_png=False
        png_file='./resources/power_port.png'
        
        # Call the parent's constructor
        super(Power_port,self).__init__(r_origin,WIDTH,HEIGHT,angle,color,use_png,png_file)
        self.color=color
        self.flip_y=flip_y

    def draw_triangle(self,screen):
        triangle_width=2*ft_+6*in_

        if self.flip_y:
            x1=self.rect.left
            x2=x1-triangle_width        
        else:
            x1=self.rect.right
            x2=x1+triangle_width


        y1=self.rect.top
        
        x3=x1
        y3=self.rect.bottom
        
        
        y2=(y3-y1)/2+y1



        line_width=3
        pygame.draw.line(screen, self.color, (x1,y1), (x2, y2), line_width)
        pygame.draw.line(screen, self.color, (x2, y2), (x3,y3), line_width)

