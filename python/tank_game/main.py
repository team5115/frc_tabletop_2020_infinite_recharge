"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

import pygame
from player import Player
from cargo_ship import Cargo_ship
from rocket import Rocket
from hab_zone import Hab_zone

from colors import *


        
# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Test')

def redraw_screen():
    field_width=230*3
    field_height=133*3

    max_x=field_width;
    max_y=field_height;

    min_x=0
    min_y=0
    mid_x=max_x/2.0
    mid_y=max_y/2.0

    
    # draw on the surface object
    screen.fill(WHITE)
    pygame.draw.polygon(screen, GREY, ((0,0), (field_width, 0), (field_width,field_height), (0,field_height), (0, 0)))
#    pygame.draw.line(screen, GREEN, (0,0), (field_width, 0), (field_width,field_height), (0,field_height), (0,0), 10)

    pygame.draw.line(screen, YELLOW, (mid_x, min_y), (mid_x, max_y), 2)
    pygame.draw.line(screen, YELLOW, (min_x, mid_y), (max_x, mid_y), 2)
#    pygame.draw.line(screen, BLUE, (120, 60), (60, 120))
#    pygame.draw.line(screen, BLUE, (60, 120), (120, 120), 4)
#    pygame.draw.circle(screen, BLUE, (300, 50), 20, 0)
#    pygame.draw.ellipse(screen, RED, (300, 250, 40, 80), 1)
#    pygame.draw.rect(screen, RED, (200, 150, 100, 50))

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

hab_zone_1=Hab_zone(min_x,mid_y,BLUE,0)
hab_zone_2=Hab_zone(max_x,mid_y,BLUE,180)

hab_zone_width=95
red_x=hab_zone_width/2
blue_x=field_width-(hab_zone_width/2)

p1_y=field_height/4
p2_y=p1_y*2
p3_y=p1_y*3


# Create the player object
player1 = Player(red_x, p1_y,RED1)
player2 = Player(red_x, p2_y,RED2)
player3 = Player(red_x, p3_y,RED3)

player4 = Player(blue_x, p1_y, BLUE1)
player5 = Player(blue_x, p2_y,BLUE2)
player6 = Player(blue_x, p3_y,BLUE3)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(cargo_ship_1)
all_sprites_list.add(rocket_1)
all_sprites_list.add(rocket_2)
all_sprites_list.add(rocket_3)
all_sprites_list.add(rocket_4)
all_sprites_list.add(hab_zone_1)
all_sprites_list.add(hab_zone_2)
all_sprites_list.add(player1)
all_sprites_list.add(player2)
all_sprites_list.add(player3)
all_sprites_list.add(player4)
all_sprites_list.add(player5)
all_sprites_list.add(player6)

clock = pygame.time.Clock()
done = False

d_angle=3
d_speed=3

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1.changespeed(-d_speed, 0)
            elif event.key == pygame.K_d:
                player1.changespeed(d_speed, 0)
            elif event.key == pygame.K_w:
                player1.changespeed(0, -d_speed)
            elif event.key == pygame.K_s:
                player1.changespeed(0, d_speed)
            elif event.key == pygame.K_q:
                player1.rotate(d_angle)
            elif event.key == pygame.K_e:
                player1.rotate(-d_angle)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player1.changespeed(d_speed, 0)
            elif event.key == pygame.K_d:
                player1.changespeed(-d_speed, 0)
            elif event.key == pygame.K_w:
                player1.changespeed(0, d_speed)
            elif event.key == pygame.K_s:
                player1.changespeed(0, -d_speed)
            elif event.key == pygame.K_q:
                player1.rotate(-d_angle)
            elif event.key == pygame.K_e:
                player1.rotate(d_angle)


    # This actually moves the player block based on the current speed
    player1.update(all_sprites_list)
    #player2.update()
    #player3.update()
    #player4.update()
    #player5.update()
    #player6.update()

    # -- Draw everything
    # Clear screen
    #screen.fill(WHITE)
    redraw_screen()
    
    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

    #if player1.is_collided_with(player2):
    #    print "COLLISION"
    
pygame.quit()
