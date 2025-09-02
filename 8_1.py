'''Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
 Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan
kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
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

def lentokenttä():
    icao = input("Anna lentokentän icao-koodi: ")
    sql=f'select name from airport where ident like "{icao}";'
    #print(sql)
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if kursori.rowcount>0:
        for rivi in tulos:
            print(rivi)
    return

if __name__ == '__main__':
    lentokenttä()