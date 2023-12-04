import pandas as pd
import os

os.system("cls")
print("------------------------SKRIV EN LISTA MED DINA VÄNNER------------------------")
my_list = []

def listadd(addition):
    my_list.append(addition)

def listremove(remove):
    my_list.pop(remove)

def listedit(edit, newname):
    my_list[edit] = newname

while True:  # huvudloop
    input_1 = input("\nSkriv in ett namn eller en position i listan för att förändra något i listan ")

    if input_1.lstrip('-').isdigit():
        select = int(input_1)
        if -len(my_list) <= select <= len(my_list):
            action = input("Vill du ta bort eller redigera? ").upper()
            if action == "TA BORT":
                listremove(select - 1 if select > 0 else select)
            elif action == "REDIGERA":
                newname = input(f"Skriv in det nya namnet för {my_list[abs(select)-1]}: ")
                listedit(abs(select) - 1, newname)
        else:
            print("Ogiltig position. Försök igen.")
    else:
        listadd(input_1)

    os.system("cls")
    print("--DIN LISTA--")
    for index, value in enumerate(my_list, start=1):
        print(f"{index}) {value}")

    print("Du har", len(my_list), "namn i din lista")
