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
                CLS()
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
        def InvalidResponseHandler(isNotValid, message, sideDistance):
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
            
            length = int(InvalidResponseHandler(isNotValid, "What would you like the length to be?\nANS:", length))
            
            CLS()
            width = input("What would you like the width to be?\nANS:")
            isNotValid = TestIsNotValidInput(width)
            
            width = int(InvalidResponseHandler(isNotValid, "What would you like the width to be?\nANS:", width))
            
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
            
            side = int(InvalidResponseHandler(isNotValid, "What would you like the side length to be?\nANS:", side))
            
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
                
        def InvalidValueHandler(ValidityBool, amount):
            while ValidityBool:
                CLS()
                print("Invalid amount. Enter a value greater than $0.00, in the format 0.00.\n")
                amount = input("How much money do you have? (Ex: 186.41 for $186.41)\nANS:")
                ValidityBool = TestIfValidAmount(amount)
            return amount 
        #Array slot for each currency from $100 to $0.01
        countOfCurrencies = [0,0,0,0,0,0,0,0,0,0]
        
        #Parallel array for the name for each currency
        currencies = [100.00,50.00,20.00,10.00,5.00,1.00,0.25,0.10,0.05,0.01]
        
        currencyName = ["Hundred", "Fifty", "Twenty", "Ten", "Five", "One", "Quarter", "Dime", "Nickel", "Penny"]
        
        amount = input("How much money do you have? (Ex: 186.41 for $186.41)\nANS:")
        
        ValidityBool = TestIfValidAmount(amount)
        
        amount = float(InvalidValueHandler(ValidityBool, amount))
            
        message = "Your exact change is "
        
        count = 0
        
        CLS()
        
        print(f"Amount entered: ${amount}\n")
        
        # Loop for each currency choice
        for denomination in currencies:
            while amount >= denomination:
                amount -= denomination
                amount = round(amount, 2)
                countOfCurrencies[count] += 1
                
                # Changes the message output based on count per denomination
            if(countOfCurrencies[count] > 0):
                if(countOfCurrencies[count] > 1):
                    if(currencyName[count][len(currencyName[count]) - 1] == "y"):
                        # If currency name ends in a y changes it to an "ies" ending
                        message += f"{countOfCurrencies[count]} {currencyName[count][:-1]}ies, "
                    else:
                        # Else currency name ends in "s" ending
                        message += f"{countOfCurrencies[count]} {currencyName[count]}s, "
                else:
                    # If only one count of that denomination, doesn't add plural ending
                    message += f"{countOfCurrencies[count]} {currencyName[count]}, "
                
            count += 1    
        
        if(len(message) == 21):
            message += "nothing"
        else:
            # Removes the last comma and space
            message = message[:-2]
        
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
    sleep(1.5)
    CLS()
        
    #***************************************** Main Function End ******************************************
    
#***************************************** Program Start *****************************************#      
    
Main()

