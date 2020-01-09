import pygame
import copy
from colors import *
from units import *
import sprite_rect
from pygame.math import Vector2


left_margin=50
right_margin=50
bottom_margin=50
top_margin=50

field_width=52*ft_+5.25*in_;
field_height=26*ft_+11.25*in_;


screen_width=left_margin+field_width+right_margin
screen_height=top_margin+field_height+bottom_margin


min_x=left_margin
min_y=top_margin

        
max_x=field_width+min_x
max_y=field_height+min_y

mid_x=field_width/2.0+min_x
mid_y=field_height/2.0+min_y



initiation_line_blue_x=min_x+10*ft_;
initiation_line_red_x=max_x-10*ft_;
       






# #####################################################################
# class Loading_bay(sprite_rect.Sprite_rect):

#     def __init__(self, r_origin,color=GREEN):

        
#         #width=12*in_
#         #height=12*in_
#         angle=0
        
#         use_png=True
#         png_file='./resources/loading_bay.png'
        
#         # Call the parent's constructor
#         super(Loading_bay,self).__init__(r_origin,WIDTH,HEIGHT,angle,color,use_png,png_file)



