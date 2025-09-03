#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan
# euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat
# ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
# (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math
def pizza(halkaisija,hinta_euro):
    halkaisija=halkaisija/100
    halkaisija=math.pi*(halkaisija/2)**2
    halkaisija = hinta_euro/halkaisija
    print(f"{halkaisija} €/m^2")
    return halkaisija, hinta_euro


if __name__ == '__main__':
    halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija cm: "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))
    halkaisija2 = float(input("Anna toisen pizzan halkaisija cm: "))
    hinta2 =float(input("Anna toisen pizzan hinta euroina: "))
    vastine = pizza(halkaisija1,hinta1)
    vastine2 = pizza(halkaisija2,hinta2)
    if vastine <vastine2:
        print("Ensimmäinen pizza on parempi vastine rahalle! ")
    elif vastine > vastine2:
        print("Toinen pizza on parempi vastine rahalle! ")
    else:
        print("Molemmat pizzat ovat yhtä hyvä vastine rahalle! ")

