"""
def print_name(name): #name är en parameter
    print(name)


print_name("Johan")    #"Johan" är ett argument

def calc(x,y):
    ans = x*y
    return ans

print(calc(1,5))
"""


def calculate(x,y,op):
    if op == 1:
        return x+y
    elif op == 2:
        return x-y
    elif op == 3:
        return x*y
    elif op == 4:
        return x/y

while True:
    try:
        tal = int(input("x: "))
        break
    except:
        print("Skriv in ett tal")
while True:
    try:
        tall = int(input("y: "))
        break
    except:
        print("skriv in ett tal")
while True:
    try:
        talll = int(input("op (1-4): "))
        break
    except:
        print("skirv in ett tal")
print(calculate(tal,tall,talll))



for i in range(10):
    print(calculate(tal,tall,talll))



my_list = ["Victor", "Johan", "Simon",]

def listins(pos):
    my_list.pop(pos)

def listitem2(edit):
        my_list[edit]=name

def listitem3(add):
    my_list.append(add)


while True: #huvut loop
    print(my_list)
    x = int(input("vill du redigera din lista(skriv 1 för att ta bort, 2 för att redigera 3 för att lägga till 0 för att avsluta)"))
    if x == 1:
        y= int(input("Vilken position vill du ta bort"))
        print(listins(y-1))
    elif x == 2:
        p=int(input("skriv in vilken pos du vill redigea"))
        name = input()
        print(listitem2(p-1))
    elif x == 3:
        newname = input("Skriv in ett nytt namn ")
        print(listitem3(newname))


