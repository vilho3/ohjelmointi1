#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain
# nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka
# , kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.


def bensiini ():
    gallonat = int(input("Anna gallonat: "))
    litra= gallonat*3.785
    if gallonat>0:
        print(f"se on {litra} litraa")
    return gallonat
ohjelma=True
while ohjelma == True:
    gallonat = bensiini()
    if gallonat < 0:
        ohjelma = False
        break
    bensiini()

