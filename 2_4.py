#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

eka = float(input("Anna ensimmäinen numero: "))
toka = float(input("Anna toinen numero: "))
kolmas = float(input("Anna kolmas numero: "))

summa = eka+toka+kolmas
tulo = eka*toka*kolmas
keskiarvo =(eka+toka+kolmas)/3
print(f"lukujen summa on: {summa:.2f}")
print(f"lukujen tulo on: {tulo:.2f}")
print(f"lukujen keskiarvo on: {keskiarvo:.2f}")
