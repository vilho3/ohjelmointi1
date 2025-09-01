'''
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
 Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin. geopy kirjasto
'''
import geopy
import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    user="vilho1",
    password="Saunakilpikonna",
    port=3306,
    database="flight_game",
    autocommit=True
)

def lentokenttä(kysymys):
    sql=f'select name from airport where ident ="{kysymys}";'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if kursori.rowcount>0:
        for rivi in tulos:
            print(rivi)
    return
''' 
def etäisyys(x,y):



'''



if __name__ == '__main__':
    kysymys1=input("Anna lentokentän ICAO-koodi: ")
    lentokenttä(kysymys1)

    '''
    kysymys2=input("Anna toisen lentokentän ICAO-koodi: ")
    lentokenttä(kysymys2)
    etäisyys(kysymys1,kysymys2)
    '''
