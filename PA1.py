# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 19:10:38 2023

@author: Evan Paddock
"""

#Main Start
def Main():
    from time import sleep 
    #Defining functions
    #Shows main menu choices
    def MainMenu():
        print("Welcome to Danish's Game")
        print("Please enter the number of the game you would like to play or '-1' to exit")
        print("1: Rock Paper Scissors")
        print("2: Draw shapes")
        print("3: Currency Calculator")
        return input()
    #
    def IsNotValid(menu, choice):
        if(choice == "-1"):
            return
        elif(menu == "Main"):
            if(choice == "1"):
                return
            if(choice == "2"):
                return
            if(choice == "3"):
                return
            else:
                return True
    #
    def RunChoice(menu, choice):
        #Runs Main Menu Options
        if(menu == "Main"):
            if(choice == "1"):
                # RPS()
                print("RPS")
            elif(choice == "2"):
                # DrawShapes()
                print("DrawShapes")
            else:
                #CurrencyCalculator()
                print("CurrencyCalculator")
                
    #Clears console
    def CLS():
        print('\n' * 50)
        
    #Rock Paper Scissors Game
    def RPS():
        return
    
    CLS() 
    
    choice = MainMenu()
    
    while IsNotValid("Main", choice):
        CLS() 
        
        print("Invalid option. Please choose again.\n")
        choice = MainMenu();
        
    while choice != "-1":
        CLS() 
        
        RunChoice("Main", choice)
        sleep(5)
        
        CLS()
        
        choice = MainMenu()
        
        while IsNotValid("Main", choice):
            CLS() 
            
            print("Invalid option. Please choose again.\n")
            choice = MainMenu();
        
    
    

Main()
        
        
        