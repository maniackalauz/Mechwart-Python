# 1000-ig hány db 19-el osztható szám van?
x = 1
db = 0
while x < 1001:
    if x % 19 == 0:
         db += 1
         print(f"{db}. : {x}") #Ezt így nem használjuk
    x += 1
print(f"19-el osztható számok: {db}")