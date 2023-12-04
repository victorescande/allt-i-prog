import random
import os
from colors import bcolors
import math

while True:
    os.system("cls")
    rand=(random.randint(1, 100)) 
    print(bcolors.BOLD + bcolors.DEFAULT + "-----------------Gissa Talet (1-100)-----------------") 
    i = 0
    while i in range(7):
        try:
            guess = int(input(bcolors.BLUE + "Skriv in din gissning (0 för att avsluta) "))
        except:
            print(bcolors.RED + "\nInvalid input\n")
            continue
        
        attempts = 6 - i
        if guess  == rand:
            print(bcolors.GREEN + "\nGrattis du hittade rätt tal på " + str(abs(attempts - 7) ) +" gissningar!!!\n")
            break
        elif guess == 0:
            print(bcolors.DEFAULT)
            exit()
        elif guess >= rand:
            print(bcolors.PURPLE + "\nFörsök ett lägre tal \n")
            i = i+1
        elif guess <= rand:
            print(bcolors.PURPLE + "\nFörsök ett högre tal \n")
            i = i+1
        if attempts >= 5:
            print (bcolors.DEFAULT + "\nDu har " + bcolors.GREEN + str(attempts) + bcolors.DEFAULT + " gissningar kvar\n")
        elif attempts >2:
            print (bcolors.DEFAULT + "\nDu har " + bcolors.YELLOW + str(attempts) + bcolors.DEFAULT + " gissningar kvar\n")
        elif attempts >=1:
            print (bcolors.DEFAULT + "\nDu har " + bcolors.RED + str(attempts) + bcolors.DEFAULT + " gissningar kvar\n")

        
        if attempts == 0:
            print (bcolors.RED + "\nDu förlorade, du hittade inte det gömda talet som var", rand)
            
        
        
    
    while True:
        answer = input(bcolors.YELLOW + "\nVill du fortsätta spela? (Y/N) ").upper()
        print(bcolors.DEFAULT)


        if answer == "Y":
            break
        elif answer == "N":
            exit()
        else:
            print("Invalid input")
            pass

            



    

    
