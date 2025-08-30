#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma
# tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.


kuukaudet= ("kevät","kesä","syksy","talvi")
arvot = 1, (2, 3), 4
kuukausi = int(input("Anna kuukauden numero 1-12: "))
tulostus = kuukaudet[kuukausi-1]
print("vuoden aika on: " + (tulostus))
