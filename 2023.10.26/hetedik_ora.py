#Előírt lépésszám FOR
#Elől tesztelő ciklus WHILE
#Addig fut a ciklus amig a WHILE utáni feltétel IGAZ!
#gondoskodni kell a ciklus változok változtatásáról
#ha nem változtatjuk meg vagy rosszul módositjuk, akkor végtelen ciklust írtunk
#Írjuk ki 1-től 10-ig a számokat egymás allá
#írjuk ki 1-től 10-ig egymás mellé vesszővel elválasztva
#Írjuk ki a kétjegyű páros számokat

print("***** 1 feladat ******")
x=1
while x<11:
    print(x)
    x= x+1
 
print("****** 2 feladat *******")
    
x=0
while x <10:
    x=x+1
    print(f"{x},", end="")
    
    
print("\n******* 3 feladat")

x=10
while x <100:
    print(x)
    x += 2
  
print("\n******* 3 feladat, 2. módszer ********")  

x = 10
while x < 100:
    if x % 2 == 0:
        print(x)
    x += 1
    

print("\n******* 3 feladat, 3. módszer ********")

x=0
while x < 100:
    if x % 2 == 0 and x > 9:
        print(x)
    x += 1 