#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin
# Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random

luku = random.randint(1,10)
#print(luku)
kysymys = int(input("Arvaa kokonaisluku: "))
while True:

    if kysymys == luku:
        print("Arvasit oikein")
        break
    if kysymys < luku:
        print("Liian pieni arvaus")
    if kysymys > luku:
        print("Liian suuri arvaus")
    kysymys = int(input("\nArvaa kokonaisluku: "))