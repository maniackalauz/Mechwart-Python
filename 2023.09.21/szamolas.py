#Be kérünk egy számot és döntse el hogy kisebb vagy nagyobb mint 10

szam = int(input("Adj meg egy számot: "))
if szam < 10:
    print(" A szám kisebb mint 10!!")
else:
    szam > 10
    print("A szám nagyobb mint 10!!")
    
#Az ELSE ág NEM KÖTELEZŐ!!! Ha nincs ott, akkor nem csinál semmit a program , hamis esetén nem ír ki semmit!

# Logikai operátorok 2 ÉS, jele "and" és csak akkor IGAZ, ha minden eleme igaz
# Ha csak egy HAMIS van közte, akkor az ÉS vége HAMIS
# Logikai operátorok 3 VAGY, a jele "or", csak akkor hamis, ha minden eleme hamis
# Ha csak egy IGAZ van, akkor a VAGY vége már igazS