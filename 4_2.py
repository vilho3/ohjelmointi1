#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes
# käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = float(input("Anna tuumat: "))

while tuuma >=0:
    sentit = tuuma *2.54
    print(f"{tuuma} tuumaa on {sentit} cm ")
    tuuma = float(input("Anna tuumat: "))