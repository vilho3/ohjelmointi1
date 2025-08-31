'''
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
 hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
 ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
 Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
 Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
 Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
Löydät koodeja helposti selaimen avulla.)
'''

asemat = {}
def valinta():
    print("\nValitse toiminto")
    print("Syötä uusi lentoasema = 1")
    print("Hae lentoasema tietoja = 2")
    print("Jos haluat lopettaa syötä enter")
    kysymys=input("Toimintosi: ")
    return kysymys

def lisää_lentoasema(asemat):
    icao = input("Anna lentoaseman ICAO-koodi: ").upper()
    nimi = input("Anna lentoaseman nimi: ")
    if icao in asemat:
        print(f"ICAO-koodi on jo tallennettu nimellä {icao} ja {asemat[icao]}")
        return
    asemat[icao] = nimi
    print("Nimi tallennettu")

def hae_lentoasema(asemat):
    icao = input("Anna lentoaseman icao: ").upper()
    if icao in asemat:
        print(f"{icao}: {asemat[icao]}")
    else:
        print(f"Ei löytynyt koodiilla: {icao}")

def main():
    while True:
        valitseminen = valinta()
        if valitseminen =="1":
            lisää_lentoasema(asemat)
        elif valitseminen =="2":
            hae_lentoasema(asemat)
        elif valitseminen == "":
            print("Ohjelma lopettaa")
            break
        else:
            print("Virheellinen toiminto")


if __name__ == "__main__":
    main()

