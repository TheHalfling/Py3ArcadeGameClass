# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:43:35 2018

@author: Sherry

Quiz about the UK series Red Dwarf

"""

def quiz():
    correct = 0
    questions = 0
    #question 1
    prob1 = int(input("What year was Red Dwarf first Broadcast? "))
    questions += 1
    if prob1 == 1998:
        print("You are correct")
        correct += 1
    else:
        print ("You are wrong. The answer was 1998.")
    
    #question 2
    prob2 = int(input("How many seasons did the original BBC run last? "))
    questions += 1
    if prob2 == 8:
        print("You are correct")
        correct +=1
    else:
        print ("You are wrong. The answer was 8.")

    #question 3
    prob3 = input("What was the name of the ship they found Krytan on? ").lower()
    questions += 1
    if prob3 == 'nova v' or prob3 == 'nova 5':
        print("You are correct")
        correct += 1
    else:
        print ("You are wrong. The answer was Nova V.")
    
    #question 4
    prob4 = input("Who plays Dave Lister? ").lower()
    questions += 1
    if prob4 == 'craig charles' or prob4 == 'charles, craig':
        print("You are correct")
        correct += 1
    else:
        print ("You are wrong. The answer was Craig Charles.")

    #question 5
    prob5 = input("What was the name of the cat Lister smuggled on board? ").lower()
    questions += 1
    if prob5 == 'frankenstein':
        print("You are correct")
        correct += 1
    else:
        print ("You are wrong. The answer was Frankenstein.")
 
    #print Results
    p = (correct/questions)*100
    print()
    print("You got {}".format(p) + "% correct.")

quiz()