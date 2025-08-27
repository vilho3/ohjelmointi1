#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

lista= []
luku=input("Anna luku: ")
while luku != "":
    lista.append(luku)
    luku=input("Anna luku: ")
    lista=[int(i)for i in lista]
    lista.sort(reverse=True)

print(lista)
