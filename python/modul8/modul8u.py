import os
from datetime import date as Date
from datetime import datetime
from time import sleep
import time
#1
"""x = datetime.now()
print(x)

#2

#3

while True:
    sleep(1)
    os.system("cls")
    x = datetime.now()
    print(x)
"""
#4

timer=0
start_time = time.time()
while True:
    os.system("cls")
    current_time=time.time()
    stopwatch = current_time-start_time
    elapsed_time_tuple = time.localtime(stopwatch)
    print(elapsed_time_tuple)
    form= time.strftime("%H:%M:%S:",elapsed_time_tuple)
    print(form)
    sleep(1)

"""#0 sten
#1 påse
#2 sax
import random
import os
wins=0
turns=0
losses=0
while True:
    turns=turns+1
    ai = random.randint(0,2)
    user = input("vad väljer du? ")
    os.system("cls")
    print(f"Du valde: {user}")
    
    if ai == 0:
        print("AI valde: sten\n")
    elif ai == 1:
        print("AI valde: påse\n")
    elif ai == 2:
        print("AI valde: sax\n")

    if user == "sten":
        if ai == 0:
            print("lika\n")
        elif ai == 1:
            print("ai vann\n")
            losses=losses+1
        elif ai == 2:
            print("du vann\n")
            wins = wins+1

    elif user == "sax":
        if ai == 0:
            print("ai vann\n")
            losses=losses+1
        elif ai == 1:
            print("du vann\n")
            wins = wins+1
        elif ai == 2:
            print("lika\n")

    elif user == "påse":
        if ai == 0:
            print("du vann\n")
            wins = wins+1
        elif ai == 1:
            print("lika\n")
        elif ai == 2:
            print("ai vann\n")
            losses=losses+1

    print(f"Wins{wins} Losses{losses} Turns{turns} ")
"""