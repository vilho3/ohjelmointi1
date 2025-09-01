'''
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä
on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
'''

import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    user="vilho1",
    password="Saunakilpikonna",
    port=3306,
    database="flight_game",
    autocommit=True
)

def maa_koodi():
    koodi=input("Anna maakodi: ")
    sql=f'select type, count(*) from airport where iso_country ="{koodi}" group by type order by count(*) desc'
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos =kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(rivi)
    return
if __name__ == "__main__":
    maa_koodi()
