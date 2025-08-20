#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.


kanta = float(input("anna suorakulmion kanta: "))
korkeus = float(input("anna suorakulmion korkeus: "))

ala = kanta * korkeus

print(f"pinta-ala  on {ala:.2f}")

piiri = kanta+kanta+korkeus+korkeus
print(f"piiri on {piiri:.2f}")