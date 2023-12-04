import random
import os
from colors import bcolors


while True:
    os.system("cls")

    print(bcolors.YELLOW + """
    Gissa Talet  1-100
    """)

    number = (random.randint(1, 100)) 
    tot_guess = 0

    while tot_guess <= 7:
        try:
            attempt = int(input(bcolors.YELLOW + "skriv in din gissning "))
        except:
            print(bcolors.RED + "invalid input \n")
            continue
        tot_guess = tot_guess + 1

        if attempt < number:
            print(bcolors.RED + "För lågt")
        elif attempt > number:
            print(bcolors.RED + "för högt")
        elif attempt == number:
            print(bcolors.GREEN + "Rätt!! Du hittade det hemliga talet", number, "på", tot_guess, "försök")
            break
        print(bcolors. PURPLE + "du har",7 - tot_guess, "gissningar kvar")


        if tot_guess >=7:
            print(bcolors.RED + "du hittade inte talet som var", number)
            break
    while True:
        answer = input(bcolors.YELLOW + "Vill du spela igen (Y/N)").upper()
        if answer == "N":
            print("hejdå")
            exit()
        elif answer == "Y":
            break
        else:
            print("invalid input")
            pass

