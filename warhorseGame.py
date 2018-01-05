# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 19:23:22 2018

@author: Sherry

#The warhorse game
"""
import random

#print the game introduction
def intro():
    print("Welcome to Warhorse")
    print("You have stolen a Warhorse to make your way across the great Estalov Forest.")
    print("The knights want their warhorse back and are chasing you down!")
    print("Survive your forest trek and outrun the knights.")

#print out the choices for the player
def choices():
    print("A. Drink from your canteen")
    print("B. Ahead moderate speed")
    print("C. Ahead full speed")
    print("D. Stop and rest")
    print("E. Status check")
    print("Q. Quit")

def gamePlay():
    #set variable start points
    milesTraveled = 0
    thirst = 0
    horse_tiredness = 0
    knights_lag = -20
    canteen_drinks = 10
    done = False
    
    #game play loop
    while not done:
        #print choices
        choices()
        
        #get player input
        playerChoice = input("Your choice? ").lower()
        
        #handle choices
        if playerChoice == "q":
            print("Thank you for playing.")
            done = True
        elif playerChoice == "e":
            print("Miles traveled: {}".format(milesTraveled))
            print("Drinks in canteen: {}".format(canteen_drinks))
            print("The knights are {}".format(knights_lag) + " miles behind you")
        elif playerChoice == "d":
            horse_tiredness = 0
            print("The Warhorse is happy.")
            knights_lag += random.randint(7,10)
        elif playerChoice == "c":
            travel = random.randint(10,20)
            milesTraveled += travel
            print ("You traveled {}".format(travel) + " miles.")
            knights_lag += random.randint(7,14)
            thirst += 1
            horse_tiredness += random.randint(1,3)
        elif playerChoice == "b":
            travel = random.randint(5,12)
            milesTraveled += travel
            print ("You traveled {}".format(travel) + " miles.")
            knights_lag += random.randint(7,14)
            thirst += 1
            horse_tiredness += 1
        elif playerChoice == "a":
            if canteen_drinks > 1:
                canteen_drinks -= 1
                thirst = 0
            else:
                print("Your canteen is empty")
        print()
        #check thirst
        if thirst > 6 and not done:
            print("You died of thirst")
            print("Game over")
            done = True
        elif thirst > 4 and not done:
            print("You are thirsty")
            print()
        
        #check horse tiredness
        if horse_tiredness > 8 and not done:
            print("The Warhorse perished")
            print("Game over")
            done = True
        elif horse_tiredness > 5 and not done:
            print("The Warhorse is tired")
            print()
        
        #check knight location
        if knights_lag >= milesTraveled and not done:
            print("The knights have caught you.")
            print("Game over")
            done = True
        elif milesTraveled - knights_lag < 15 and not done:
            print("The knights are getting close!")
            print()
        
        #check for win
        if milesTraveled >= 200 and not done:
            print("You have successfully stolen the Warhorse.")
            print("You won!")
            done = True
            
        #random encounter
        x = random.randint(1,20)
        if x == 1:
            print("You found an oasis and refill your canteen and rest your horse")
            print()
            horse_tiredness = 0
            thirst = 0
            canteen_drinks = 10

#execute code
intro()
gamePlay()