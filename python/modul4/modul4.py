import math
import random
import os 

#1
os.system("cls")



print("Välkommen till grönalund, nu ska vi kolla om du är tillräckligt lång för att åka")

length = int(input("Skriv hur lång du är: "))
if length >= 140:
    print("ok du får åka")
elif length <=140:
    print("du får bara åka barn grejer")


#2

x = input("Hej och välkommen vad heter du?: ")
print("hej " + x +"!")
colour = input("vad är din favoritfärg? ")
while True:
    try:
        age = int(input("hur gammal är du? "))
        break
    except:
        print("fel")





print("\nhej", x, "stämmer det att du är", age, "år gammal, och gillar färgen", colour + "?"), 
o = input(":")
if o == "ja":
    print("perfekt")


#3

print("Dethär är en BMI kalkylator. Låt oss börja med din")
while True:
    try:
        weight = int(input("vikt:"))
        break
    except:
        print("fel")
while True: 
    try:
        length = float(input("och sen din längd:"))
        break
    except:
        print("fel")

length = length/100
length = length*2
BMI = weight / length
print ("Din BMI är", BMI)

#4
pi = math.pi
while True:
    try:
        r = float(input("Skriv in radien: "))
        break
    except:
        print("skriv in en radie med siffror")

r = r*r*pi
round(r)
print("Arean på din cirkel", round(r))

#5

print("Det här är en miniräknare")
while True:
    calc_method = input("börja med att skiva in ditt räknesätt (+, -, *, /) (eller skirv 'S' för att avsluta): ").upper()
    if calc_method in ("+", "-", "*", "/"):
        pass
    elif calc_method == "S":
        break
    else:
        print ("invalid input")
        continue
    
    if calc_method == "+":
        while True:
            try:
                number1 = float(input("Skriv in det första talet du vill addera med: "))
                break
            except:
                print("invalid input")
        while True:
            try:
                number2 = float(input("Skriv in det andra talet du vill addera med det första talet: "))
                break
            except:
                print("invalid input")
        finalnumber1 = number1 + number2
        print(round(finalnumber1))

    elif calc_method == "-":
        while True:
            try:
                number1 = float(input("Skriv in det första talet du vill subtrahera med: "))
                break
            except:
                print ("invalid input")
        while True:
            try:
                number2 = float(input("Skriv in det andra talet du vill subtrahera med det första talet: "))
                break
            except:
                print("invalid input")
        finalnumber1 = number1-number2
        print(round(finalnumber1))

    elif calc_method == "*":
        while True:
            try:
                number1 = float(input("Skriv in det första talet du vill multiplicera med: "))
                break
            except:
                print("invalid input")
        while True:
            try:
                number2 = float(input("Skriv in det andra talet du vill multiplicera med det första talet: "))
                break
            except:
                print("invalid input")

        finalnumber1 = number1*number2
        print(round(finalnumber1))

    elif calc_method == "/":
        while True:
            try:
                number1 = float(input("Skriv in det första talet du vill dividera med: "))
                break
            except:
                print("invalid input")
        while True:
            try:
                number2 = float(input("Skriv in det andra talet du vill dividera med det första talet: "))
                break
            except:
                print("invalid input")
        finalnumber1 = number1/number2
        print(round(finalnumber1))
        break


#6

print (random.randint(1, 6))

#7
while True:
    try:
        amount = int(input("skirv in hur många gågner du vill slå din tärning "))
        break
    except:
        print("invalid input")
for i in range(amount):
	print (random.randint(1, 6))


        
