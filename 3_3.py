#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen
# ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Anna biologinen sukupuolesi: ")
arvo = float(input("Anna hemoglobiiniarvosi g/l: "))

if sukupuoli == "mies" or "Mies" or "MIES":
    if arvo <134:
        print("hemoglobiiniarvosi on alhainen")
    elif arvo > 195:
        print("hemoglobiiniarvosi on korkea")
    else:
        print("hemoglobiiniarvosi on normaali")

elif sukupuoli == "nainen" or "Nainen" or "NAINEN":
    if arvo <117:
        print("hemoglobiiniarvosi on alhainen")
    elif arvo > 175:
        print("hemoglobiiniarvosi on korkea")
    else:
        print("hemoglobiiniarvosi on normaali")