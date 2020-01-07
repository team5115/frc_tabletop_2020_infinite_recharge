#!/usr/bin/python
#
#

"""
FRC robot sim
Team 5115 - Knight Riders

Author: Joe Adams
 Email: joseph.s.adams@gmail.com
   URL: https://github.com/jsadams/frc_tabletop.git

version: 2

19/01/11 - multiple keymaps now working



"""

import pygame, sys
from pygame.locals import *
from colors import *

import pygame
from robot import Robot
from cargo_ship import Cargo_ship
from rocket import Rocket
from wall import Wall


from hab_platform_level_0 import Hab_platform_level_0
from hab_platform_level_1 import Hab_platform_level_1
from hab_platform_level_2 import Hab_platform_level_2
from hab_platform_level_3 import Hab_platform_level_3
from depot import Depot
from loading_station import LoadingStation

from colors import *
from units import *


class Game:

    def __init__(self):

        ##############################################
        #field_width=230*in_*3
        #field_height=133*in_*3

        self.field_width=54*ft_;
        self.field_height=27*ft_;

        self.hab_line_x=94.3*in_;
        # Call this function so the Pygame library can initialize itself
        pygame.init()

        # Create an 800x600 sized screen
        #screen_size=[800,600]
        screen_size=[self.field_width,int(self.field_height*1.20)]
        self.screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)
    
        # Set the title of the window
        pygame.display.set_caption('Test')


    
        
        
        max_x=self.field_width;
        max_y=self.field_height;

        min_x=0
        min_y=0
        mid_x=max_x/2.0
        mid_y=max_y/2.0


        wall_thickness=1*in_
        
        wall_1=Wall(min_x,min_y,width=self.field_width,height=wall_thickness,color=BLACK)
        wall_2=Wall(min_x,max_y,width=self.field_width,height=wall_thickness,color=BLACK)

        wall_3=Wall(min_x,min_y,width=wall_thickness,height=self.field_height,color=BLACK)
        wall_4=Wall(max_x,min_y,width=wall_thickness,height=self.field_height,color=BLACK)

        cargo_ship_xo=mid_x
        cargo_ship_yo=mid_y

        cargo_ship_1=Cargo_ship(cargo_ship_xo,cargo_ship_yo)

        rocket_1_xo=229*in_
        rocket_1_yo=min_y

        rocket_2_xo=rocket_1_xo
        rocket_2_yo=max_y

        rocket_3_xo=max_x-rocket_1_xo
        rocket_3_yo=rocket_1_yo

        rocket_4_xo=rocket_3_xo
        rocket_4_yo=rocket_2_yo

        rocket_1=Rocket(rocket_1_xo,rocket_1_yo,BLUE)
        rocket_2=Rocket(rocket_2_xo,rocket_2_yo,BLUE,flip_y=True)
        rocket_3=Rocket(rocket_3_xo,rocket_3_yo,RED)
        rocket_4=Rocket(rocket_4_xo,rocket_4_yo,RED,flip_y=True)

        x=min_x
        y=mid_y        
        blue_hab_platform_level_3=Hab_platform_level_3(x,y,BLUE_HAB3,flip_x=False)

        x=min_x
        y=blue_hab_platform_level_3.rect.bottom
        blue_hab_platform_level_2b=Hab_platform_level_2(x,y,BLUE_HAB2,flip_x=False,flip_y=False)

        x=min_x
        y=blue_hab_platform_level_3.rect.top
        blue_hab_platform_level_2a=Hab_platform_level_2(x,y,BLUE_HAB2,flip_x=False,flip_y=True)

        x=blue_hab_platform_level_3.rect.right
        y=mid_y
        blue_hab_platform_level_1=Hab_platform_level_1(x,y,BLUE_HAB1,flip_x=False)

        x=blue_hab_platform_level_3.rect.right
        y=mid_y
        blue_hab_platform_level_0=Hab_platform_level_0(x,y,BLUE_HAB0,flip_x=False)

        x=min_x
        y=blue_hab_platform_level_2b.rect.bottom
        blue_depot_a=Depot(x,y,ORANGE,flip_x=False,flip_y=False)

        x=min_x
        y=blue_hab_platform_level_2a.rect.top
        blue_depot_b=Depot(x,y,ORANGE,flip_x=False,flip_y=True)

        dy_loading_station=27*in_
        x=min_x
        y=min_y+dy_loading_station
        blue_loading_station_a=LoadingStation(x,y,ORANGE,flip_x=False,flip_y=False)

        x=min_x
        y=max_y-dy_loading_station
        blue_loading_station_b=LoadingStation(x,y,ORANGE,flip_x=False,flip_y=True)

        

        x=max_x
        y=mid_y        
        red_hab_platform_level_3=Hab_platform_level_3(x,y,RED_HAB3,flip_x=True)

        x=max_x
        y=red_hab_platform_level_3.rect.bottom
        red_hab_platform_level_2b=Hab_platform_level_2(x,y,RED_HAB2,flip_x=True,flip_y=False)

        x=max_x
        y=red_hab_platform_level_3.rect.top
        red_hab_platform_level_2a=Hab_platform_level_2(x,y,RED_HAB2,flip_x=True,flip_y=True)
        
        x=red_hab_platform_level_3.rect.left
        y=mid_y        
        red_hab_platform_level_1=Hab_platform_level_1(x,y,RED_HAB1,flip_x=True)

        x=red_hab_platform_level_3.rect.left
        y=mid_y        
        red_hab_platform_level_0=Hab_platform_level_0(x,y,RED_HAB0,flip_x=True)

        x=max_x
        y=red_hab_platform_level_2b.rect.bottom
        red_depot_a=Depot(x,y,ORANGE,flip_x=True,flip_y=False)

        x=max_x
        y=red_hab_platform_level_2a.rect.top
        red_depot_b=Depot(x,y,ORANGE,flip_x=True,flip_y=True)


        dy_loading_station=27*in_
        x=max_x
        y=min_y+dy_loading_station
        red_loading_station_a=LoadingStation(x,y,ORANGE,flip_x=True,flip_y=False)

        x=max_x
        y=max_y-dy_loading_station
        red_loading_station_b=LoadingStation(x,y,ORANGE,flip_x=True,flip_y=True)

        
        ############################################
        #  Robot starts
        #

        blue_x=blue_hab_platform_level_1.rect.centerx
        blue_y1=blue_hab_platform_level_1.rect.centery
        blue_y2=blue_y1+blue_hab_platform_level_1.rect.height/3
        blue_y3=blue_y1-blue_hab_platform_level_1.rect.height/3

        red_x=red_hab_platform_level_1.rect.centerx
        red_y1=red_hab_platform_level_1.rect.centery
        red_y2=red_y1+red_hab_platform_level_1.rect.height/3
        red_y3=red_y1-red_hab_platform_level_1.rect.height/3
        
       
        
        key_map_1={ pygame.K_w: "forward",
                    pygame.K_s: "backward",
                    pygame.K_a: "strafe_left", 
                    pygame.K_d: "strafe_right",
                    pygame.K_e: "rotate_right",
                    pygame.K_q:  "rotate_left" }


        key_map_2={ pygame.K_t: "forward",
                    pygame.K_g: "backward",
                    pygame.K_f: "strafe_left", 
                    pygame.K_h: "strafe_right",
                    pygame.K_r: "rotate_right",
                    pygame.K_y:  "rotate_left" }

        key_map_3={ pygame.K_i: "forward",
                    pygame.K_k: "backward",
                    pygame.K_j: "strafe_left", 
                    pygame.K_l: "strafe_right",
                    pygame.K_u: "rotate_right",
                    pygame.K_o:  "rotate_left" }


        key_map_4={ pygame.K_UP: "forward",
                    pygame.K_DOWN: "backward",
                    pygame.K_LEFT: "strafe_left", 
                    pygame.K_RIGHT: "strafe_right",
                    pygame.K_PAGEUP: "rotate_right",
                    pygame.K_PAGEDOWN:  "rotate_left" }

        key_map_5={ pygame.K_KP0: "forward",
                    pygame.K_KP1: "backward",
                    pygame.K_KP2: "strafe_left", 
                    pygame.K_KP3: "strafe_right",
                    pygame.K_KP4:  "rotate_right",
                    pygame.K_KP5: "rotate_left" }

        key_map_6={ pygame.K_0: "forward",
                    pygame.K_1: "backward",
                    pygame.K_2: "strafe_left", 
                    pygame.K_3: "strafe_right",
                    pygame.K_4: "rotate_right",
                    pygame.K_5: "rotate_left" }


        # Create the robot object
        self.robot1 = Robot(blue_x, blue_y1,BLUE1,angle=270,keymap=key_map_1, is_mecanum=True,team_name=5115,width=10*in_,length=45*in_)
        self.robot2 = Robot(blue_x, blue_y2,BLUE2,angle=270,keymap=key_map_2, is_mecanum=False,team_name=493)
        self.robot3 = Robot(blue_x, blue_y3,BLUE3,angle=270,keymap=key_map_3, is_mecanum=False,team_name=503)


        self.robot4 = Robot(red_x, red_y1,RED1,angle=90,keymap=key_map_4,is_mecanum=True,team_name=3361)
        self.robot5 = Robot(red_x, red_y2,RED2,angle=90,keymap=key_map_5,is_mecanum=False,team_name=3258)
        self.robot6 = Robot(red_x, red_y3,RED3,angle=90,keymap=key_map_6,is_mecanum=False,team_name=2106)


#        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.OrderedUpdates()

     
        self.all_sprites_list.add(wall_1)
        self.all_sprites_list.add(wall_2)
        self.all_sprites_list.add(wall_3)
        self.all_sprites_list.add(wall_4)
        
        self.all_sprites_list.add(cargo_ship_1)
        self.all_sprites_list.add(rocket_1)
        self.all_sprites_list.add(rocket_2)
        self.all_sprites_list.add(rocket_3)
        self.all_sprites_list.add(rocket_4)
        self.all_sprites_list.add(blue_hab_platform_level_0)
        self.all_sprites_list.add(blue_hab_platform_level_1)
        self.all_sprites_list.add(blue_hab_platform_level_2a)
        self.all_sprites_list.add(blue_hab_platform_level_2b)
        self.all_sprites_list.add(blue_hab_platform_level_3)
        self.all_sprites_list.add(blue_depot_a)
        self.all_sprites_list.add(blue_depot_b)
        self.all_sprites_list.add(blue_loading_station_a)
        self.all_sprites_list.add(blue_loading_station_b)


        self.all_sprites_list.add(red_hab_platform_level_0)
        self.all_sprites_list.add(red_hab_platform_level_1)
        self.all_sprites_list.add(red_hab_platform_level_2a)
        self.all_sprites_list.add(red_hab_platform_level_2b)
        self.all_sprites_list.add(red_hab_platform_level_3)
        self.all_sprites_list.add(red_depot_a)
        self.all_sprites_list.add(red_depot_b)
        self.all_sprites_list.add(red_loading_station_a)
        self.all_sprites_list.add(red_loading_station_b)

        self.all_sprites_list.add(self.robot1)
        self.all_sprites_list.add(self.robot2)
        self.all_sprites_list.add(self.robot3)
        self.all_sprites_list.add(self.robot4)
        self.all_sprites_list.add(self.robot5)
        self.all_sprites_list.add(self.robot6)


        
        self.solid_sprites_list = pygame.sprite.Group()
    
        self.solid_sprites_list.add(wall_1)
        self.solid_sprites_list.add(wall_2)
        self.solid_sprites_list.add(wall_3)
        self.solid_sprites_list.add(wall_4)

        self.solid_sprites_list.add(cargo_ship_1)
        self.solid_sprites_list.add(rocket_1)
        self.solid_sprites_list.add(rocket_2)
        self.solid_sprites_list.add(rocket_3)
        self.solid_sprites_list.add(rocket_4)
#        self.solid_sprites_list.add(blue_hab_platform_level_1)
        self.solid_sprites_list.add(blue_hab_platform_level_2a)
        self.solid_sprites_list.add(blue_hab_platform_level_2b)
        self.solid_sprites_list.add(blue_hab_platform_level_3)
        self.solid_sprites_list.add(blue_depot_a)
        self.solid_sprites_list.add(blue_depot_b)

 #       self.solid_sprites_list.add(red_hab_platform_level_1)
        self.solid_sprites_list.add(red_hab_platform_level_2a)
        self.solid_sprites_list.add(red_hab_platform_level_2b)
        self.solid_sprites_list.add(red_hab_platform_level_3)
        self.solid_sprites_list.add(red_depot_a)
        self.solid_sprites_list.add(red_depot_b)


        self.solid_sprites_list.add(self.robot1)
        self.solid_sprites_list.add(self.robot2)
        self.solid_sprites_list.add(self.robot3)
        self.solid_sprites_list.add(self.robot4)
        self.solid_sprites_list.add(self.robot5)
        self.solid_sprites_list.add(self.robot6)

        self.robots_list = pygame.sprite.Group()
        self.robots_list.add(self.robot1)
        self.robots_list.add(self.robot2)
        self.robots_list.add(self.robot3)
        self.robots_list.add(self.robot4)
        self.robots_list.add(self.robot5)
        self.robots_list.add(self.robot6)

        
        self.clock = pygame.time.Clock()



    def redraw_screen(self):
        

        max_x=self.field_width;
        max_y=self.field_height;

        min_x=0
        min_y=0
        mid_x=max_x/2.0
        mid_y=max_y/2.0

        line_width=2*in_

        # draw on the surface object
        self.screen.fill(WHITE)
        pygame.draw.polygon(self.screen, GREY, ((min_x,min_y), (max_x, min_y), (max_x,max_y), (min_x,max_y), (0, 0)))
        

        pygame.draw.line(self.screen, YELLOW, (min_x, mid_y), (max_x, mid_y), line_width)

        pygame.draw.line(self.screen, BLUE, (self.hab_line_x, min_y), (self.hab_line_x, max_y), line_width)
        pygame.draw.line(self.screen, RED, (max_x-self.hab_line_x, min_y), (max_x-self.hab_line_x, max_y), line_width)

        dx=9*in_
        mid_blue_x=mid_x-dx
        mid_red_x=mid_x+dx
        
        pygame.draw.line(self.screen, BLUE, (mid_blue_x, min_y), (mid_blue_x, max_y), line_width)
        pygame.draw.line(self.screen, RED, (mid_red_x, min_y), (mid_red_x, max_y), line_width)

     

        
    def run(self):
        d_angle=3
        d_speed=3
        done=False
        
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                elif event.type == pygame.VIDEORESIZE:
                    old_surface_saved = surface
                    surface = pygame.display.set_mode((event.w, event.h),
                                                      pygame.RESIZABLE)
                    # On the next line, if only part of the window
                    # needs to be copied, there's some other options.
                    surface.blit(old_surface_saved, (0,0))
                    del old_surface_saved     

                # # Set the speed based on the key pressed
                # elif event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_a:
                #         self.robot1.changespeed(-d_speed, 0)
                #     elif event.key == pygame.K_d:
                #         self.robot1.changespeed(d_speed, 0)
                #     elif event.key == pygame.K_w:
                #         self.robot1.changespeed(0, -d_speed)
                #     elif event.key == pygame.K_s:
                #         self.robot1.changespeed(0, d_speed)
                #     elif event.key == pygame.K_q:
                #         self.robot1.rotate(d_angle)
                #     elif event.key == pygame.K_e:
                #         self.robot1.rotate(-d_angle)

                # # Reset speed when key goes up
                # elif event.type == pygame.KEYUP:
                #     if event.key == pygame.K_a:
                #         self.robot1.changespeed(d_speed, 0)
                #     elif event.key == pygame.K_d:
                #         self.robot1.changespeed(-d_speed, 0)
                #     elif event.key == pygame.K_w:
                #         self.robot1.changespeed(0, d_speed)
                #     elif event.key == pygame.K_s:
                #         self.robot1.changespeed(0, -d_speed)
                #     elif event.key == pygame.K_q:
                #         self.robot1.rotate(-d_angle)
                #     elif event.key == pygame.K_e:
                #         self.robot1.rotate(d_angle)

                elif event.type == pygame.KEYDOWN:
                    for robot in self.robots_list:
                        robot.process_event(event)

                elif event.type == pygame.KEYUP:
                    for robot in self.robots_list:
                        robot.process_event(event)

            for robot in self.robots_list:
                robot.update(self.solid_sprites_list)
            # This actually moves the robot block based on the current speed
            #self.robot1.update(self.solid_sprites_list)
            #self.robot2.update()
            #self.robot3.update()
            #self.robot4.update()
            #self.robot5.update()
            #self.robot6.update()

            # -- Draw everything
            # Clear self.screen
            #self.screen.fill(WHITE)
            self.redraw_screen()

            # Draw sprites
            self.all_sprites_list.draw(self.screen)

            # Flip screen
            pygame.display.flip()

            # Pause
            self.clock.tick(60)

            #if self.robot1.is_collided_with(self.robot2):
            #    print "COLLISION"

        pygame.quit()

if __name__ == '__main__':

    the_game=Game()
    the_game.run();
    

