#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen
#, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.
kuha = float(input("Anna kuhan pituus: "))
if kuha <37 :
    print(f"kuhasi on alamittainen, laske kuha takaisin järveen, kuhan pitää olla {37-kuha} cm pidempi")
else:
    print("kuhasi on tarpeeksi iso, voit ottaa sen ")