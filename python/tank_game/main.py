#!/usr/bin/python
#
#

"""
FRC robot sim
Team 5115 - Knight Riders

Author: Joe Adams
"""

import pygame, sys
from pygame.locals import *
from colors import *

import pygame
from robot import Robot
from cargo_ship import Cargo_ship
from rocket import Rocket


from hab_platform_level_1 import Hab_platform_level_1
from hab_platform_level_2 import Hab_platform_level_2
from hab_platform_level_3 import Hab_platform_level_3

from colors import *
from units import *


class Game:

    def __init__(self):
        # Call this function so the Pygame library can initialize itself
        pygame.init()

        # Create an 800x600 sized screen
        screen_size=[800,500]
        self.screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)
    
        # Set the title of the window
        pygame.display.set_caption('Test')


        ##############################################
        field_width=230*3
        field_height=133*3

        max_x=field_width;
        max_y=field_height;

        min_x=0
        min_y=0
        mid_x=max_x/2.0
        mid_y=max_y/2.0

        cargo_ship_xo=mid_x
        cargo_ship_yo=mid_y

        cargo_ship_1=Cargo_ship(cargo_ship_xo,cargo_ship_yo,GREEN)

        rocket_1_xo=229
        rocket_1_yo=0

        rocket_2_xo=rocket_1_xo
        rocket_2_yo=field_height-27

        rocket_3_xo=field_width-rocket_1_xo
        rocket_3_yo=rocket_1_yo

        rocket_4_xo=rocket_3_xo
        rocket_4_yo=rocket_2_yo

        rocket_1=Rocket(rocket_1_xo,rocket_1_yo,BLUE)
        rocket_2=Rocket(rocket_2_xo,rocket_2_yo,BLUE,180)
        rocket_3=Rocket(rocket_3_xo,rocket_3_yo,RED)
        rocket_4=Rocket(rocket_4_xo,rocket_4_yo,RED,180)

        x=min_x
        y=mid_y        
        blue_hab_platform_level_3=Hab_platform_level_3(x,y,HAB3,flip_x=False)

        x=min_x
        y=blue_hab_platform_level_3.rect.bottom
        blue_hab_platform_level_2b=Hab_platform_level_2(x,y,HAB2,flip_x=False,flip_y=False)

        x=min_x
        y=blue_hab_platform_level_3.rect.top
        blue_hab_platform_level_2a=Hab_platform_level_2(x,y,HAB2,flip_x=False,flip_y=True)

        x=blue_hab_platform_level_3.rect.right
        y=mid_y
        blue_hab_platform_level_1=Hab_platform_level_1(x,y,HAB1,flip_x=False)

        x=max_x
        y=mid_y        
        red_hab_platform_level_3=Hab_platform_level_3(x,y,HAB3,flip_x=True)

        x=max_x
        y=red_hab_platform_level_3.rect.bottom
        red_hab_platform_level_2b=Hab_platform_level_2(x,y,HAB2,flip_x=True,flip_y=False)

        x=max_x
        y=red_hab_platform_level_3.rect.top
        red_hab_platform_level_2a=Hab_platform_level_2(x,y,HAB2,flip_x=True,flip_y=True)
        
        x=red_hab_platform_level_3.rect.left
        y=mid_y        
        red_hab_platform_level_1=Hab_platform_level_1(x,y,HAB1,flip_x=True)


        # red_hab_platform_level_3=Hab_platform_level_3(max_x,mid_y,HAB3,0)
        # y=red_hab_platform_level_3.rect.bottom
        # red_hab_platform_level_2b=Hab_platform_level_2(min_x,y,HAB2,0)
        # y=red_hab_platform_level_3.rect.top
        # red_hab_platform_level_2a=Hab_platform_level_2(min_x,y,HAB2,180)
        # x=red_hab_platform_level_3.rect.right
        # red_hab_platform_level_1=Hab_platform_level_1(x,mid_y,HAB1,0)

        

        hab_zone_width=95
        red_x=hab_zone_width/2
        blue_x=field_width-(hab_zone_width/2)

        p1_y=field_height/4
        p2_y=p1_y*2
        p3_y=p1_y*3


        # Create the robot object
        self.robot1 = Robot(red_x, p1_y,RED1)
        self.robot2 = Robot(red_x, p2_y,RED2)
        self.robot3 = Robot(red_x, p3_y,RED3)

        self.robot4 = Robot(blue_x, p1_y, BLUE1)
        self.robot5 = Robot(blue_x, p2_y,BLUE2)
        self.robot6 = Robot(blue_x, p3_y,BLUE3)

        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(cargo_ship_1)
        self.all_sprites_list.add(rocket_1)
        self.all_sprites_list.add(rocket_2)
        self.all_sprites_list.add(rocket_3)
        self.all_sprites_list.add(rocket_4)
        self.all_sprites_list.add(blue_hab_platform_level_1)
        self.all_sprites_list.add(blue_hab_platform_level_2a)
        self.all_sprites_list.add(blue_hab_platform_level_2b)
        self.all_sprites_list.add(blue_hab_platform_level_3)
        self.all_sprites_list.add(red_hab_platform_level_1)
        self.all_sprites_list.add(red_hab_platform_level_2a)
        self.all_sprites_list.add(red_hab_platform_level_2b)
        self.all_sprites_list.add(red_hab_platform_level_3)

        self.all_sprites_list.add(self.robot1)
        self.all_sprites_list.add(self.robot2)
        self.all_sprites_list.add(self.robot3)
        self.all_sprites_list.add(self.robot4)
        self.all_sprites_list.add(self.robot5)
        self.all_sprites_list.add(self.robot6)

        self.clock = pygame.time.Clock()
        

    def redraw_screen(self):
        field_width=230*3
        field_height=133*3

        max_x=field_width;
        max_y=field_height;

        min_x=0
        min_y=0
        mid_x=max_x/2.0
        mid_y=max_y/2.0


        # draw on the surface object
        self.screen.fill(WHITE)
        pygame.draw.polygon(self.screen, GREY, ((0,0), (field_width, 0), (field_width,field_height), (0,field_height), (0, 0)))
    #    pygame.draw.line(self.screen, GREEN, (0,0), (field_width, 0), (field_width,field_height), (0,field_height), (0,0), 10)

        pygame.draw.line(self.screen, YELLOW, (mid_x, min_y), (mid_x, max_y), 2)
        pygame.draw.line(self.screen, YELLOW, (min_x, mid_y), (max_x, mid_y), 2)
    #    pygame.draw.line(self.screen, BLUE, (120, 60), (60, 120))
    #    pygame.draw.line(self.screen, BLUE, (60, 120), (120, 120), 4)
    #    pygame.draw.circle(self.screen, BLUE, (300, 50), 20, 0)
    #    pygame.draw.ellipse(self.screen, RED, (300, 250, 40, 80), 1)
    #    pygame.draw.rect(self.screen, RED, (200, 150, 100, 50))

    
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

                # Set the speed based on the key pressed
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.robot1.changespeed(-d_speed, 0)
                    elif event.key == pygame.K_d:
                        self.robot1.changespeed(d_speed, 0)
                    elif event.key == pygame.K_w:
                        self.robot1.changespeed(0, -d_speed)
                    elif event.key == pygame.K_s:
                        self.robot1.changespeed(0, d_speed)
                    elif event.key == pygame.K_q:
                        self.robot1.rotate(d_angle)
                    elif event.key == pygame.K_e:
                        self.robot1.rotate(-d_angle)

                # Reset speed when key goes up
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.robot1.changespeed(d_speed, 0)
                    elif event.key == pygame.K_d:
                        self.robot1.changespeed(-d_speed, 0)
                    elif event.key == pygame.K_w:
                        self.robot1.changespeed(0, d_speed)
                    elif event.key == pygame.K_s:
                        self.robot1.changespeed(0, -d_speed)
                    elif event.key == pygame.K_q:
                        self.robot1.rotate(-d_angle)
                    elif event.key == pygame.K_e:
                        self.robot1.rotate(d_angle)


            # This actually moves the robot block based on the current speed
            self.robot1.update(self.all_sprites_list)
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
    
