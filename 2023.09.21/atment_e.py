#Kérj be 4.rész eredményt 

egy = int(input("Első feladrész pontszáma:"))
ketto = int(input("Második feladrész pontszáma:"))
harom = int(input("Harmadik feladrész pontszáma:"))
negy = int(input("Negyedik feladrész pontszáma:"))

if egy>= 20*0.85 or ketto>= 20*0.85 or harom>= 20*0.85 or negy>= 20*0.85:
    print("Átment!")
else:
    print("Megbukot!")