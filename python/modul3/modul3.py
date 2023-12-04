"""
for i in range(0,10):
    print(str(i+1),"hello world")
"""

#1
"""
i = 0
while True:
    print("hejhej")
    i = i +1
    if i == 10:
"""


#2
"""
string = input("skriv något som du vill ska sägas 10 gånger ") 
for i in range(0,10):
    print(str(i+1), string)
"""

#3
"""
y = int(input("skriv in y "))
for i in range(0,y):
    print(str(i+1))
"""

#4

for table in range(1, 13):
    print(f"tabell {table}")
    for y in range(1, 11):
        print(f"{table} * {y} = {str(table*y)}")

