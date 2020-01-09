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
       

trench_height=4*ft_+7.5*in_
trench_width=18*ft_


def draw_vertical_line(screen,x,color):

        line_width=2*in_

        pygame.draw.line(screen, color, (x, min_y), (x, max_y), line_width)



def draw_horizontal_line(screen,y,color):

       
        line_width=2*in_

        pygame.draw.line(screen, color, (min_x, y), (max_x, y), line_width)

def draw_rectangle(screen,x1,y1,x2,y2,color):

        
        line_width=2*in_

        pygame.draw.line(screen, color, (min_x, y), (max_x, y), line_width)

def draw_trench_runs(screen):

       
        thickness=5
        

        width=trench_width
        height=trench_height
        trench_run_red_xo=mid_x-trench_width/2
        trench_run_red_yo=min_y

        trench_run_blue_xo=trench_run_red_xo
        trench_run_blue_yo=max_y-trench_height
      
        x=trench_run_blue_xo
        y=trench_run_blue_yo

        pygame.draw.rect(screen, BLUE, (trench_run_blue_xo,trench_run_blue_yo,width,height), thickness)
        pygame.draw.rect(screen, RED, (trench_run_red_xo,trench_run_red_yo,width,height), thickness)


