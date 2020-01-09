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



