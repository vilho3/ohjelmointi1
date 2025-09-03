#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain
# nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka
# , kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.


def bensiini (benzin):
    litra=benzin*3.785
    if benzin>0:
        print(f"se on {litra} litraa")
    return benzin
ohjelma=True
while ohjelma == True:
    gallonat = int(input("Anna gallonat: "))
    bensiini(gallonat)
    if gallonat < 0:
        ohjelma = False


