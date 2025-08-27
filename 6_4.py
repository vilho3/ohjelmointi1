#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.

def summa(lista):
    lista = sum(lista)
    print(lista)
    return lista

if __name__=="__main__":
    luvut=[5,10,200,2]
    summa = summa(luvut)