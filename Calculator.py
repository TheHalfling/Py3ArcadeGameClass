# -*- coding: utf-8 -*-
"""
Spyder Editor

Calculator from Chapter 1 of Program Arcade Games with Pygame
"""
def mpg():
    # miles per gallon
    print("This program calculates mpg.")
    
    # Get Miles driven from user
    miles_driven = float(input("Enter miles driven: "))
    
    #get gallons used from user
    gallons_used = float(input("Enter gallons used: "))
    
    #calculate mpg and display
    mpg = miles_driven / gallons_used
    print("Miles per gallon: {}".format(mpg))

def kinetic_energy():
    #Calculate Kinetic Energy
    print("This program calculates the kinetic energy of a moving object.")
    
    #Get Mass from user
    mass = float(input("Enter the object's mass in kilograms: "))
    
    #Get velocity from user
    velocity = float(input("Enter the object's speed in meters per second: "))
    
    #calculate and display kinetic energy
    energy = 0.5 * mass * velocity * velocity
    print("The object has {}".format(energy) + " joules of energy.")
    
def temp_conversion():
    #Calculates the temp conversion
    print("Thie program converts the temp from F to C")
    
    #Get user input
    f = float(input("What is the temperature in Farenheit? "))
    
    #convert and print
    c = (f-32)/1.8
    print("The temperature in Celcius is {}".format(c))

def trapezoid():
    #calculates the area of a trapezoid
    print("Area of a trapezoid")
    
    #get input
    h = int(input("Enter the height of the trapezoid: "))
    len_bottom = int(input("Enter the length of the bottom of the base: "))
    len_top = int(input("Enter the length of the top base:  "))
    
    #calculate and print results
    a = .5 * (len_bottom + len_top) * h
    print ("The area is: {}".format(a))
    
 
def run_calc():
    print("Which calculator do you wish to run?")
    choice = input("Enter mpg, energy, temp, or trapezoid: ")
    choice = choice.lower()
    if choice == "mpg":
        mpg()
    elif choice == "energy":
        kinetic_energy()
    elif choice == "temp":
        temp_conversion()
    elif choice == "trapezoid":
        trapezoid()
    else:
        print("You did not input an acceptable choice")

run_calc()