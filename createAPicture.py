# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:44:07 2018

@author: Sherry

Lab 5: Create a picture

Pygame base template for opening a window
from Simpson College Computer Science used as a base 
for this project
"""

import pygame

# define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
BLUE =  (  0,   0, 255)
BROWN = (160,  82,  45)

PI = 3.141592653

pygame.init()

#set the width and height of the screen[w, h]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Lab 5 Create a Picture")

#Loop until the user click the close button
done = False
clock = pygame.time.Clock()

# used to manage how fast the screen udpates
clock = pygame.time.Clock()

# ---------Main Program Loop-----------
while not done:
    # -----Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #--------Game logic should go here
    
    
    # ---------Screen-clearing code goes here
    
    
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command
    screen.fill(BLUE)
    
    #draw trees
    for x_offset in range(0, 700, 125):
        pygame.draw.rect(screen, BLACK, [20 + x_offset, 100, 20, 400], 0)
        pygame.draw.ellipse(screen, GREEN, [0 + x_offset, 60, 75, 64], 0)
        
    #draw ground
    pygame.draw.rect(screen, BROWN, [0, 300, 700, 300] )
     
    #add title
    #select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    #render the text. "True" meand anti-aliased text
    text = font.render("The Forest", True, BLACK)
    
    #put the image of the text on the screen at 250x250
    screen.blit(text, [250, 0])
    
    
    #----------Go ahead and update the screen with what we've drawn
    pygame.display.flip()


    # -----Limit to 60 frames per second
    clock.tick(60)
    
# close the window and quit
pygame.quit()
