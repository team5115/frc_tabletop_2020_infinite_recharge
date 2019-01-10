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

d_angle=10

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1.changespeed(-3, 0)
            elif event.key == pygame.K_d:
                player1.changespeed(3, 0)
            elif event.key == pygame.K_w:
                player1.changespeed(0, -3)
            elif event.key == pygame.K_s:
                player1.changespeed(0, 3)
            elif event.key == pygame.K_q:
                player1.rotate(d_angle)
            elif event.key == pygame.K_e:
                player1.rotate(-d_angle)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player1.changespeed(3, 0)
            elif event.key == pygame.K_d:
                player1.changespeed(-3, 0)
            elif event.key == pygame.K_w:
                player1.changespeed(0, 3)
            elif event.key == pygame.K_s:
                player1.changespeed(0, -3)
            elif event.key == pygame.K_q:
                player1.rotate(0)
            elif event.key == pygame.K_e:
                player1.rotate(0)

        #     # Reset speed when key goes up
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         player1.changespeed(3, 0)
        #     elif event.key == pygame.K_RIGHT:
        #         player1.changespeed(-3, 0)
        #     elif event.key == pygame.K_UP:
        #         player1.changespeed(0, 3)
        #     elif event.key == pygame.K_DOWN:
        #         player1.changespeed(0, -3)

    # This actually moves the player block based on the current speed
    player1.update()
    player2.update()
    player3.update()
    player4.update()
    player5.update()
    player6.update()

    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)

    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()
