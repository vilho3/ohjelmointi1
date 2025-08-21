#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan
# leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi
# ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

leiviskä = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

luoti_paino=13.3
naula_paino=luoti_paino*32
leiviskä_paino=naula_paino*20
#lasketaan kiloina ja grammoina
grammoina = luoti * luoti_paino + naula * naula_paino + leiviskä * leiviskä_paino
kiloina = grammoina/1000

print("massa nykymittojen mukaan")
print(int(kiloina),"kg")
#grammoina
#grammat =grammoina/1000-int(kiloina)
grammat= grammoina % 1000
print(f"{grammat:.2f} grammaa")
# %1000 saa sen mitä jää jälelle