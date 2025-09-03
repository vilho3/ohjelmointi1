'''
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
 Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
  Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
  Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
  Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
'''
import random

class Auto:
    def __init__(self,rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
    def kiihdytä(self, muutos):
        self.tämänhetkinen_nopeus+=muutos
        if self.tämänhetkinen_nopeus>self.huippunopeus:
            self.tämänhetkinen_nopeus=self.huippunopeus
        if self.tämänhetkinen_nopeus<0:
            self.tämänhetkinen_nopeus=0
    def kulje(self, tunti):
        self.kuljettu_matka+=tunti* self.tämänhetkinen_nopeus



def main():
    lista=[]
    for i in range(1,11):
        rekisteritunnus=f"ABC-{i}"
        huippunopeus=random.randint(100,200)
        auto=Auto(rekisteritunnus, huippunopeus)
        lista.append(auto)
#    for auto in lista:
#        print(auto)

    while True:
        if auto.kuljettu_matka >=10000:
            print(lista)


            break
        auto.kulje(1)
        auto.kiihdytä(+random.randint(-10,15))






main()