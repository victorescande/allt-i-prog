#1
"""
Detta 
är
modul
2
"""

#2
x = 10
y = 20

print (y + x)
print (y - x)
print (y / x)
print (y // x)
print (y ** x)


#3
"""
x = input("Hej och välkommen vad heter du?: ")
print("hej " + x,"!")
lol = input("vad är din favoritfärg? ")

age = input("hur gammal är du? ")

print(x)
print(age)

print("\nhej", x, "stämmer det att du är", age, "år gammal, och att du gillar färgen", lol + "?"), 
o = input(":")
if o == "ja":
    print("perfekt")
elif o != "ja":
    print ("fan också")
"""    
"""
#4
tal1 = int(input("tal1:"))
tal2 = int(input("tal1:"))

print (tal1 * tal2)

#5

print("Dethär är en BMI kalkylator. Låt oss börja med din")
weight = int(input("vikt:"))
length = int(input("och sen din längd:"))
length = length/100
length = length*2
BMI = weight / length
print ("Din BMI är", BMI)
"""
#6
"""
print("Dethär är ett program som ska berätta hur många veckor du har levt")
years = int(input("börja med att skriva in hur många år du är "))
years = years*52
print ("du har levt i ungefär", years, "veckor")
"""

#7

print("Detta är ett program som ska omvandla viktenheter (kg, lbs")
enhet = input("Vilken enhet vill du omvanla ifrån ")
if enhet == "kg":
    kg = int(input("skriv in din vikt i kg: "))
    kg = kg*2.2
    print(kg, "lbs")
if enhet == "lbs":
    lbs = int(input("skriv in din vikt i lbs "))
    lbs = lbs/2.2
    print(lbs, "kg")



