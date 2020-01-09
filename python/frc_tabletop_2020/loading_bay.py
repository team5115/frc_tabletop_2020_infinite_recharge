import pygame
import copy
from colors import *
from units import *
import sprite_rect
from pygame.math import Vector2

WIDTH=2*ft_
HEIGHT=2*ft_+0.25*in_

 
#####################################################################
class Loading_bay(sprite_rect.Sprite_rect):

    def __init__(self, r_origin,color=GREEN,flip_y=False):

        
        #width=12*in_
        #height=12*in_
        
        angle=0

        if flip_y:
            angle=180
            
        use_png=False
        png_file='./resources/loading_bay.png'
        
        # Call the parent's constructor
        super(Loading_bay,self).__init__(r_origin,WIDTH,HEIGHT,angle,color,use_png,png_file)


        self.color=color
        self.flip_y=flip_y

    def draw_triangle(self,screen):
        triangle_width=1*ft_

        if self.flip_y:
            x1=self.rect.left
            y1=self.rect.top
            
            x3=x1
            y3=self.rect.bottom
        
            x2=x1-triangle_width
            y2=(y3-y1)/2+y1
        else:
            x1=self.rect.right
            y1=self.rect.top
        
            x3=x1
            y3=self.rect.bottom
            
            x2=x1+triangle_width
            y2=(y3-y1)/2+y1



        line_width=3
        pygame.draw.line(screen, self.color, (x1,y1), (x2, y2), line_width)
        pygame.draw.line(screen, self.color, (x2, y2), (x3,y3), line_width)
