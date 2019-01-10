"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

import pygame
from player import Player

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
    
    # draw on the surface object
    screen.fill(WHITE)
    pygame.draw.polygon(screen, GREY, ((0,0), (field_width, 0), (field_width,field_height), (0,field_height), (0, 0)))
#    pygame.draw.line(screen, GREEN, (0,0), (field_width, 0), (field_width,field_height), (0,field_height), (0,0), 10)
#    pygame.draw.line(screen, GREEN, (60, 60), (120, 60), 4)
#    pygame.draw.line(screen, BLUE, (120, 60), (60, 120))
#    pygame.draw.line(screen, BLUE, (60, 120), (120, 120), 4)
#    pygame.draw.circle(screen, BLUE, (300, 50), 20, 0)
#    pygame.draw.ellipse(screen, RED, (300, 250, 40, 80), 1)
#    pygame.draw.rect(screen, RED, (200, 150, 100, 50))



# Create the player object
player1 = Player(50, 50,RED)
player2 = Player(50, 150,RED)
player3 = Player(50, 250,RED)

player4 = Player(500, 50, BLUE)
player5 = Player(500, 150,BLUE)
player6 = Player(500, 250,BLUE)

all_sprites_list = pygame.sprite.Group()
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
    player1.update()
    player2.update()
    player3.update()
    player4.update()
    player5.update()
    player6.update()

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

pygame.quit()
