# Beolvasunk 3 számot és eldöntjük, hogy szerkeszthető-e belőle 3 szög
a = int(input("Adj meg az a oldalt: "))
b = int(input("Adj meg a b oldalt: "))
c = int(input("Adj meg a c oldalt: "))

if (a + b > c and a + c > b and b+c > a):
    print("Szerkezthető!")
else:
    print("Nem szerkezthető!")
    
# Derékszögű e?
a = int(input("Adj meg az a oldalt: "))
b = int(input("Adj meg a b oldalt: "))
c = int(input("Adj meg a c oldalt: "))

if (a*a+b == c*c or a**2 + c**2 == b**2 or c**2+b**2==a**2):
    print("Derékszögű")
else:
    print("Nem derékszögű")
    
#Teljesen jó verzió
a = int(input("Adj meg az a oldalt: "))
b = int(input("Adj meg a b oldalt: "))
c = int(input("Adj meg a c oldalt: "))

if (a + b > c and a + c > b and b+c > a) (a*a+b == c*c or a**2 + c**2 == b**2 or c**2+b**2==a**2) :
    print("Szerkezthető!")
else:
    print("Nem szerkezthető!")