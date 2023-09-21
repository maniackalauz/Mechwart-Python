# Eddig SZEKVENCIÁKAT NÉZTÜNK!!! Utasítások egymás után
# Most jöjjön a SZELEKCIÓ (elágazás) IF
# Általános alakja: IF; LOGIKAI FELTÉTEL:; UTASÍTÁSOK HA IGAZ A LOGIKAI FELTÉTEL; ELSE UTASÍTÁS HA NEM IGAZ A FELTÉTEL 
# lOGIKAI OPERÁTOROK: egyenlő ==; kisebb-nagyobb <, >; kisebb egyenlő, nagyobb egyenlő <=, >=

# Be kérünk egy nevet, ha név DEZSŐ, akkor írja ki, hogy szép a neved, ha nem Dezső, akkor miért nem vagy Dezső

nev = input("Add meg a neved: ")
if nev == "Dezső":
    print("Szép a neved!")
else:
    print("Miért nem vagy DEZSŐ???")
    
    
# Dezső program javítjuk
nev = input("Add meg a neved: ")
if nev == "Dezső" or nev =="Dezső":
    print("Jó a neved")
else:
    print("Nem jó a neved")