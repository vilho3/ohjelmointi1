'''
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
 Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin. geopy kirjasto
'''
import geopy
import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    user="vilho1",
    password="Saunakilpikonna",
    port=3306,
    database="flight_game",
    autocommit=True
)

def lentokenttä(kysymys):
    sql=f'select name, latitude_deg, longitude_deg from airport where ident ="{kysymys}";'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if kursori.rowcount>0:
        for rivi in tulos:
            print(rivi)
    return rivi

def etäisyys(x,y):
    etäisyys_km=geodesic(x,y).km
    print(f"{etäisyys_km:.2f} kilometriä")
    return



if __name__ == '__main__':
    kysymys1=input("Anna lentokentän ICAO-koodi: ")
    a =lentokenttä(kysymys1)
    kysymys2=input("Anna toisen lentokentän ICAO-koodi: ")
    b = lentokenttä(kysymys2)
    etäisyys(a[1:3],b[1:3])


#efhy
#efhk