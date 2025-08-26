import random
pisteet = int(input("Anna pisteiden määrä:"))
määrä = 1
sisällä =0

while määrä < pisteet:
    x = float(random.uniform(1,-1))
    y = float(random.uniform(1,-1))

    if (x**2) + (y**2) <1:
        sisällä +=1

    määrä+=1

pi = sisällä * 4 / pisteet
print(f"pi:n likiarvo: {pi}")