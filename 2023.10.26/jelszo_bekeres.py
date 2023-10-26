# Írjunk egy jelszóbekérő programot

jelszo = ""

while jelszo != "Dezső":
    jelszo = input("Add meg a jelszót: ")
    
print("Jó jelszót adtál meg!")


("\n******* feladat 2. módszer ********")

jelszo = True

while jelszo:
    nev = input("Add meg a jelszót: ")
    if nev == "Dezső":
        jelszo = False
print("Megint jó jelszót írtál be!")
