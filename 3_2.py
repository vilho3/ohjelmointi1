#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
# (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.

#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

hytti = input("Anna laivan hyttiluokkasi (LUX, A, B, tai C): ")
if hytti=="LUX":
    print("sinulla on parvekkeellinen hytti yläkannella")
elif hytti=="A":
    print("hyttisi on ikkunallinen autokannen yläpuolella")
elif hytti=="B":
    print("hyttisi on ikkunaton autokannen yläpuolella")
elif hytti=="C":
    print("hyttisi on ikkunaton autokannen alapuolella")
else:
    print("virheellinen hyttiluokka")