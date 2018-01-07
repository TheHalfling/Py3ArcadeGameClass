# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 23:17:29 2018

@author: Sherry

Lab 6: Loopy Lab
"""

#Part 1

#Create a number pyramid
"""



for i in range(10, 55):
    for j in range(10, i, 1 ):
        print (j, end = "\t")
    print ("\n")
"""

#Part 2


def createBox():
    #get length of sides of square
    n = int(input("Enter a whole number: "))
    
    #print top
    print("o"*n)
    
    #print sides
    for i in range(0,n-2):
        #print("j is {}".format(j))
        print("o"+" "*(n-2)+"o")

    #print bottom
    print("o"*n)

#Part 3
def numBox():
    #get input from user
    n = int(input("Enter a single digit number: "))    
    
    #create list
    row = []
    for i in range (1, (2*n), 2):
        row.append(i)
    for i in range(2*n-1, 0, -2):
        row.append(i)
    
    #print first row
    for i in row:
        print (i, end=" ")

# Part 4
"""
Pygame base template for opening a window

Sampl Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com
http://simpson.edu/computer-science/
"""

import pygame

def drawgrid():
    
    #define some colors
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    GREEN = (  0, 255,   0)
    
    pygame.init()
    
    #set width and height of the screen
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Grid")
    
    #loop until the user clicks the close button
    done = False
    
    #used to manage how fast the screen udpates
    clock = pygame.time.Clock()
    
    #----Main Program Loop----
    while not done:
        #---Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        #background        
        screen.fill(BLACK)
        
        #drawing
        for y_offset in range(0, 500, 7):    
            for x_offset in range(0, 700, 7):
                pygame.draw.rect(screen, GREEN, [0 + x_offset, 0 + y_offset, 3, 3], 0)
        
        #update screen
        pygame.display.flip()
        
        #limit to 60 frames per second
        clock.tick(60)
    
    pygame.quit()
    
createBox()
#numBox()
drawgrid()  