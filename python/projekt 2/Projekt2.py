#FILNAMN.PY: Bästa vänner lista

__author__  = "Victor Escande"
__version__ = "1.0.0"
__email__   = "Victor.escande@elev.ga.ntig.se"


import os
from colors import bcolors
os.system("cls")
print(bcolors.BOLD+"------------------------SKRIV EN LISTA MED DINA VÄNNER------------------------") #använde color för att styla
my_list=[]#definerade en lista


def listadd(addition): # definerade funktioner 
    my_list.append(addition)

def listremove(remove): # fler funktioner
    my_list.pop(remove)

def listedit(edit, newname): #en sista funktion
    my_list[edit]=newname


while True:    #huvudloop
    
#upper_name = name.upper()
    #if upper_name =="AVSLUTA":    
    
    input_1=(input(bcolors.DEFAULT+"\nSkirv in ett namn eller en position i listan för att förändra något i listan "))
    if input_1.isdigit():
        select=int(input_1)
        if select > 0 and select<=len(my_list):
            action = input("vill du ta bort eller redigera ")
            pos = action.upper()
            if pos == "TA BORT":
                listremove(select-1)
            elif pos == "REDIGERA":
                newname=input(f"Skriv in det nya namnet för {my_list[select-1]}: ")
                listedit(select-1, newname)
        os.system("cls")
        y=0
        print("--DIN LISTA--")
        for i in my_list:
            y+=1
            print(f"{y}) { i}")

        print("du har", len(my_list), "namn i din lista")
    else:
        (listadd(input_1))
            


        os.system("cls")
        y=0
        print("--DIN LISTA--")
        for i in my_list:
            y+=1
            print(f"{y}) { i}")
        print("du har", len(my_list), "namn i din lista")



