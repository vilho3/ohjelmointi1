#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
luvut=[]

while True:
    luku = input("Anna luku: ")
    if " " in luku:
        print(f"suurin luku: {max(luvut)}")
        print(f"pienin luku: {min(luvut)}")
        break
    luvut.append(luku)

