#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein
# tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).
käyttäjätunnus = "python"
salasana = "rules"
arvaukset = 0
while True:
    kt = input("Anna käyttätunnus: ")
    sa = input("Anna salasana: ")
    if kt == käyttäjätunnus and sa == salasana:
        print("\nTervetuloa")
        break
    if kt != käyttäjätunnus or sa != salasana:
        arvaukset +=1
        print("\n väärin")
    if arvaukset == 5:
        print("\nPääsy evätty")
        break





