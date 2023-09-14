# Kérjük be egy hordó átmérőjét és magasságát majd számoljuk ki, hogy hány literes

atmero = float(input("Add meg az átmérőt: "))
magassag = float(input("Add meg a magasságot: "))
v = ((atmero/2)**2)*3,14 * magassag # v=sugár
print(f"A hordó {v*1000} literes")

# Háromszög területe, ha ismerjük az oldalakat 345 (HERON KÉPLETE)
a = 3
b = 4
c = 5
s = (a+b+c)/2