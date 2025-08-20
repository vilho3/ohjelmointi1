#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
#Vihje: tutustu random.randint()-funktion käyttöön.
import random

luku1 = random.randint(0,9)
print("ensimmäinen luku: ",luku1)
luku2 = random.randint(0,9)
print("toinen luku: ",luku2)

luku3 = random.randint(0,6)
luku4 = random.randint(0,6)
luku5 = random.randint(0,6)
print("kolmenumeroisen koodi numerot ovat: ",luku3,luku4,luku5)
luku6 = random.randint(0,6)
luku7 = random.randint(0,6)
luku8 = random.randint(0,6)
luku9 = random.randint(0,6)
print("nelinumeroisen koodin luvut ovat: ", luku6,luku7,luku8,luku9)