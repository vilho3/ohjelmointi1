#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita
# ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

arpa = int(input("Anna arpakuutioiden lukumäärä: "))
summa =0
for n in range(arpa):
    luku = random.randint(1, 6)
    summa += luku
print(summa)
