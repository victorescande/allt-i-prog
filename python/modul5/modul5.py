import os
os.system("cls")

"""
my_list = ["victor", "simon", "viktor"]
print(my_list)

my_list[0]="johan"
print(my_list)
my_list.append("Hannes")
print(my_list)
print(len(my_list))
my_list.pop(1)
print(my_list)
print(len(my_list))
"""
min_lista = []
while True:
    name=input("Skriv in ett namn ('avsluta' för att avsluta och 'Ta bort' för att ta bort) ")
    upper_name = name.upper()
    if upper_name =="AVSLUTA":
        exit()
    elif upper_name =="TA BORT":
        number = input("skriv in vilket platts namnet ligger på ")
        min_lista.pop(int(number)-1)
    else:
        min_lista.append(name)
    
    print(min_lista)

"""

namn1 = input("skirv in det första namnet ")
namn2 = input("skriv in det andra namnet ")
amount= int(input("skriv in hur många gånger det ska köras "))
list = [namn1,namn2]
for amount in range(amount):
    print(list)

"""


#skapa en lista listan ska fyllas i automatiskt från 1-100 skriv ut listan på nya rader
list = []
for i in range(100):
    list.append(i+1)

for i in list:
    print(i, end="-")