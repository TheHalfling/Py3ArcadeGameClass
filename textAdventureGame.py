# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:31:20 2018

@author: Sherry

A text based adventure game
"""

#set variables
room_list = [["The library is well appointed with many books lining the walls. There are doors to the North and East.", 3, 1, None, None],
        ["The hallway is dimly lit with oil sconces on the walls and a tattered rug on the floor. There are doors to the North, West and East.", 4, 2, None, 0],
        ["The dining room has a lard table set for 10 with the finest china covered in a thin layer of dust. There are doors to the North and West.", 5, None, None, 1],
        ["The bedroom has a huge four poster bed with the curtains drawn and several dressers. There are doors to the West and South", None, 4, 0, None],
        ["The hallway has old and worn tapestries on the walls and only a single flickering light from the chandelier. There are doors in all directions.", 6, 5, 1, 3],
        ["The kitchen reeks of long forgotten food, and the scurry of rodents is obvious as you enter. There are doors to the South and West.", None, None, 2, 4],
        ["The balcony looks down over the gardens, the railing is crumbling from decay. The only exit is to the South.", None, None, 4, None]]

current_room = 1
done = False

while done == False:
    #print text
    print()
    print(room_list[current_room][0])
    
    #get user input
    choice = input("What direction do you want to go? ").lower()
    
    #move north
    if choice[0] == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print ("You can't go that way")
        else:
            current_room = next_room
    
    #move east        
    elif choice[0] == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print ("You can't go that way")
        else:
            current_room = next_room
    
    #move south
    elif choice[0] == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print ("You can't go that way")
        else:
            current_room = next_room
    
    #move west
    elif choice[0] == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print ("You can't go that way")
        else:
            current_room = next_room
    
    #quit game
    elif choice[0] == "q":
        print ("Thank you for playing")
        done = True
    
    #other
    else:
        "You picked an incorrect direction. Try again"
        

