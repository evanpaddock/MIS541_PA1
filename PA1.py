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
    
    #Shows main menu choices and gets choice
    def MainMenu():
        print("Welcome to Danish's Game")
        print("Please enter the number of the game you would like to play")
        print("1: Rock Paper Scissors")
        print("2: Draw shapes")
        print("3: Currency Calculator")
        print("4: exit")
        return input()
    
    #Checks if the choice is valid for the given menu
    def IsNotValid(choice):
        if(choice == "1"):
            return
        elif(choice == "2"):
            return
        elif(choice == "3"):
            return
        elif(choice == "4"):
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
        def MainMenu():
            print("What do you choose?")
            print(" 1: Rock")
            print(" 2: Paper")
            print(" 3: Scissors")
            return input("Selection: ")
                
        def IsNotValid(choice):
            if(choice == "1"):
                return
            elif(choice == "2"):
                return
            elif(choice == "3"):
                return
            else:
                return True
                
        def MenuValidLoop():
            CLS()
            
            choice = MainMenu()
            
            while IsNotValid(choice):
                print("Invalid option. Please choose again.\n")
                choice = MainMenu()
                
            return choice
            
        choices = ["", "Rock", "Paper", "Scissors"]
            
        choice = int(MenuValidLoop())
        
        compChoice = random.randint(1, 3)
        
        if(choice == compChoice):
            print(f"You both chose {choices[choice]}. The game ties!")
        else:
            if(choice < compChoice and compChoice != choice + 1 or choice > compChoice and compChoice != choice - 2):
                print(f"You chose {choices[choice]} which beats your opponent that chose {choices[compChoice]}!")
            else:
                print(f"You chose {choices[choice]} which loses to your opponent that chose {choices[compChoice]}!")
                
        sleep(3)
        input("\nPress any key to continue")
    
    #Draws rectange by length and width and inverted right trianle by length
    def DrawShapes():
        
        #Draw Shapes Game Main Menu
        def MainMenu():
            print("Please choose a shape!")
            print("1. Rectangle")
            print("2. Isosceles Right Triangle")
            print("3. Go Back")
            return input("Selection: ")
        
        #Draw Shapes Main Menu Validation Loop
        def MenuValidLoop():
            CLS()
            
            choice = MainMenu()
            
            while IsNotValid(choice):
                CLS()
                print("Invalid option. Please choose again.\n")
                choice = MainMenu()
                
            return choice
        
        def IsNotValid(choice):
            if(choice == "1"):
                return
            elif(choice == "2"):
                return
            elif(choice == "3"):
                return
            else:
                return True
        
        def RunChoice(choice):
            CLS()
            
            if(choice == "1"):
                Rectangle()
            elif(choice == "2"):
                RightTriangle()
                
        #Tests if the given length or width is a valid response
        def TestIsNotValidInput(sideDistance):
                try:
                    if(int(sideDistance) >= 2):
                        return
                    else:
                        return True
                except ValueError:
                    return True
        
        #Reasks input while sideDistance is not valid, returns sideDistance once allowed       
        def InvalidResponseHandler(isNotValid, message):
            while isNotValid:
                CLS()
                print("Invalid response. Please try again.\n")
                sideDistance = input(message)
                isNotValid = TestIsNotValidInput(sideDistance)
            return sideDistance
                
        
        #Takes a length and width and draws a rectangle
        def Rectangle():
            
            length = input("What would you like the length to be?\nANS:")
            isNotValid = TestIsNotValidInput(length)
            
            length = int(InvalidResponseHandler(isNotValid, "What would you like the length to be?\nANS:"))
            
            CLS()
            width = input("What would you like the width to be?\nANS:")
            isNotValid = TestIsNotValidInput(width)
            
            width = int(InvalidResponseHandler(isNotValid, "What would you like the width to be?\nANS:"))
            
            CLS();
            print(f"Rectangle Specs: length={length} width={width}\n")
            for x in range(length):
                for y in range(width):
                    print("*", end=" ")
                    
                print()
                
            input("\nPress any key to continue")
            
        #Gets side length and prints triangle in reverse length order
        def RightTriangle():
            side = input("What would you like the side length to be?\nANS:")
            isNotValid = TestIsNotValidInput(side)
            
            side = int(InvalidResponseHandler(isNotValid, "What would you like the side length to be?\nANS:"))
            
            CLS()
            print(f"Triangle Specs: left={side} top={side} right={round(math.sqrt(2) * side, 5)}\n")
            for x in range(side, 0, -1):
                for y in range(x):
                    print("* ", end="")
                print()
                
            input("\nPress any key to continue")
        
        choice = MenuValidLoop()
        
        while choice != "3":
            RunChoice(choice)
            
            choice = MenuValidLoop()
            
        Main()
    
    #Shows currency by dollars to pennies
    def CurrencyCalculator():
        def TestIfValidAmount(amount):
            try:
                if(float(amount) > 0.00):
                    return
                else:
                    return True
            except Exception:
                return True
                
        def InvalidValueHandler(ValidityBool):
            while ValidityBool:
                CLS()
                print("Invalid amount. Enter a value greater than $0.00, in the format 0.00.\n")
                amount = input("How much money do you have? (Ex: 186.41 for $186.41)\nANS:")
                ValidityBool = TestIfValidAmount(amount)
            return amount   
        #Array slot for each currency from $100 to $0.01
        array = [0,0,0,0,0,0,0,0,0,0]
        
        amount = input("How much money do you have? (Ex: 186.41 for $186.41)\nANS:")
        
        ValidityBool = TestIfValidAmount(amount)
        
        amount = InvalidValueHandler(ValidityBool)
        
        message = "Your exact change is "
        
        if(amount >= 100.00):
            while amount >=100.00:
                array[0] += 1
                amount -= (100.00)
                amount = round(amount, 2)
            message += f"{array[0]} 100(s),"
        if(amount >= 50.00):
            while amount >=50.00:
                array[1] += 1
                amount -= (50.00)
                amount = round(amount, 2)
            message += f"{array[1]} 50(s),"
        if(amount >= 20.00):
            while amount >=20.00:
                array[2] += 1
                amount -= (20.00)
                amount = round(amount, 2)
            message += f"{array[2]} 20(s),"
        if(amount >= 10.00):
            while amount >=10.00:
                array[3] += 1
                amount -= (10.00)
                amount = round(amount, 2)
            message += f"{array[3]} 10(s),"
        if(amount >= 5.00):
            while amount >=5.00:
                array[4] += 1
                amount -= (5.00)
                amount = round(amount, 2)
            message += f"{array[4]} 5(s),"
        if(amount >= 1.00):
            while amount >=1.00:
                array[5] += 1
                amount -= (1.00)
                amount = round(amount, 2)
            message += f"{array[5]} 1(s),"
        if(amount >= 0.25):
            while amount >=0.25:
                array[6] += 1
                amount -= 0.25
                amount = round(amount, 2)
            message += f"{array[6]} quarter(s),"
        if(amount >= 0.10):
            while amount >=0.10:
                array[7] += 1
                amount -= 0.10
                amount = round(amount, 2)
            message += f"{array[7]} dime(s),"
        if(amount >= 0.05):
            while amount >=0.05:
                array[8] += 1
                amount -= 0.05
                amount = round(amount, 2)
            message += f"{array[8]} nickel(s),"
        if(amount >= 0.01):
            while amount >= 0.01:
                array[9] += 1
                amount -= 0.01
                amount = round(amount, 2)
            message += f"{array[9]} penny(s),"
        
        if(len(message) == 21):
            message += "nothing"
        else:
            message = message[:-1]
        
        print(message)
        input("\nPress any key to continue")
                
        
    #***************************************** Defining Main Functions End ******************************************
    

    #***************************************** Main Function Start ******************************************
    
    CLS() 
    
    choice = MenuValidLoop()
        
    while choice != "4":
        CLS() 
        
        RunChoice(choice)
        
        CLS()
        
        choice = MenuValidLoop()
        
    CLS()
    print("Thank you for playing Danish's games! Bye Bye!")
    sleep(3)
    CLS()
        
    #***************************************** Main Function End ******************************************
    
#***************************************** Program Start *****************************************#      
    
Main()
        
        
        