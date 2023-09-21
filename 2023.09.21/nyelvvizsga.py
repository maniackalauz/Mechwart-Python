# Nyelvvzsga írásbeli 100 pont, szóbeli 50 pont csak akkor van meg, ha mind mindkettőből 60%-ot szerez
# Százalék számítás: valami 60%-a azt jelenti, hogy szorzom 60-al és osztom 100-al (*0,6)
# Kérjük be az írásbeli és szóbeli eredményét, majd írjuk ki, hogy átment e?

irasbeli = int(input("Írd be az írásbeli eredményedet: "))
szobeli = int(input("Írd be a szóbeli eredményedet: "))
if irasbeli >=100*0.6 and szobeli>= 50*0.6:
    print("Átment!")
else:
    print("Nem ment át!")