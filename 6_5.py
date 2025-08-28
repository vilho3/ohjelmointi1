#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista
# paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
# ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def luku():
    lista=[]
    for x in luvut:
        if x %2==0:
            lista.append(x)
    return lista

if __name__=="__main__":
    luvut=[100,200,23,126,125,1]
    lista=luku()
    print(luvut)
    print(lista)