# Háromszög területe, ha ismerjük az oldalakat (HERON KÉPLETE)
a = int(input("Add meg az A oldalt: "))
b = int(input("Add meg a B oldalt: "))
c = int(input("Add meg a C oldalt: "))
s = (a+b+c)/2
t = (s *(s - a)*(s - b) * (s - c))**(1/2)
print(t)