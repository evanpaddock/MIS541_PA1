# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 19:10:38 2023

@author: Evan Paddock
"""

#Main Start
def Main():
    #importing necessary items
    
    from time import sleep
    import random
    import math
    
    #***************************************** Defining Functions Start******************************************
    
    #Shows main menu choices and get choice
    def MainMenu():
        print("Welcome to Danish's Game")
        print("Please enter the number of the game you would like to play")
        print(" 1: Rock Paper Scissors")
        print(" 2: Draw shapes")
        print(" 3: Currency Calculator")
        print("-1: exit")
        return input()
    
    #Checks if the choice is valid for the given menu
    def IsNotValid(choice):
        if(choice == "-1"):
            return
        elif(choice == "1"):
            return
        elif(choice == "2"):
            return
        elif(choice == "3"):
            return
        else:
            return True
            
    
    #Main menu validation loop
    def MenuValidLoop():
        
        choice = MainMenu()
        
        while IsNotValid(choice):
            CLS()
            print("Invalid option. Please choose again.\n")
            choice = MainMenu()
        return choice
    
    #Runs choice depending on menu
    def RunChoice(choice):
        CLS()
        
        #Runs Main Menu Options
        if(choice == "1"):
            RPS()
        elif(choice == "2"):
            DrawShapes()
        elif(choice == "3"):
            CurrencyCalculator()
                
    #Clears console
    def CLS():
        print('\n' * 50)
        
    #Rock Paper Scissors Game
    def RPS():
        print("RPS")
    
    #Draws rectange by length and width and inverted right trianle by length
    def DrawShapes():
        
        #Draw Shapes Game Main Menu
        def MainMenu():
            print("Please choose a shape!")
            print(" 1. Rectangle")
            print(" 2. Right Triangle")
            print("-1. Go Back")
            return input("Selection: ")
        
        #Draw Shapes Main Menu Validation Loop
        def MenuValidLoop():
            CLS()
            
            choice = MainMenu()
            
            while IsNotValid(choice):
                print("Invalid option. Please choose again.\n")
                choice = MainMenu()
                
            return choice
        
        def IsNotValid(choice):
            if(choice == "-1"):
                return
            elif(choice == "1"):
                return
            elif(choice == "2"):
                return
            else:
                return True
        
        def RunChoice(choice):
            CLS()
            
            if(choice == "1"):
                Rectangle()
            elif(choice == "2"):
                RightTriangle()
        
        #Takes a length and width and draws a triangle
        def Rectangle():
            length = int(input("What would you like the length to be?\nANS:"))
            CLS()
            width = int(input("What would you like the width to be?\nANS:"))
            
            CLS();
            print(f"Rectangle Specs: length={length} width={width}\n")
            for x in range(length):
                for y in range(width):
                    print("*", end=" ")
                    
                print()
                
            sleep(5)
            
        #Gets side length and prints triangle in reverse length order
        def RightTriangle():
            side = int(input("What would you like the side length to be?\nANS:"))
            
            CLS()
            print(f"Triangle Specs: left={side} top={side} right={round(math.sqrt(2) * side, 2)}\n")
            for x in range(side, 0, -1):
                for y in range(x):
                    print("*", end="")
                print()
                
            sleep(5)
        
        choice = MenuValidLoop()
        
        while choice != "-1":
            RunChoice(choice)
            
            choice = MenuValidLoop()
            
        Main()
        
    
    #Shows currency by dollars to pennies
    def CurrencyCalculator():
        print("CurrencyCalculator")
        
    #***************************************** Defining Main Functions End ******************************************
    

    #***************************************** Main Function Start ******************************************
    
    CLS() 
    
    choice = MenuValidLoop()
        
    while choice != "-1":
        CLS() 
        
        RunChoice(choice)
        sleep(5)
        
        CLS()
        
        choice = MenuValidLoop()
        
    CLS()
    print("Thank you for playing Danish's games! Bye Bye!")
    sleep(3)
    CLS()
        
    #***************************************** Main Function End ******************************************
    
#***************************************** Program Start *****************************************#      
    
Main()
        
        
        