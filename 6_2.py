#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random
tahkot=int(input("Anna tahkojen määrä: "))

def noppa():
    luku = random.randint(1,tahkot)
    return luku

silmäluku=0
while silmäluku != tahkot:
    silmäluku = noppa()
    print(silmäluku)
