import sqlite3

def trova_farmacia_per_coordinate(latitudine, longitudine, tolleranza=0.01):
    try:
        conn = sqlite3.connect('database.db')  
        cursor = conn.cursor()
        query = """
        SELECT id, nome_farmacia, indirizzo, lat, lng
        FROM Pharmacy
        WHERE lat BETWEEN ? AND ?
        AND lng BETWEEN ? AND ?
        """

        lat_min = latitudine - tolleranza
        lat_max = latitudine + tolleranza
        lng_min = longitudine - tolleranza
        lng_max = longitudine + tolleranza

        cursor.execute(query, (lat_min, lat_max, lng_min, lng_max))
        farmacie = cursor.fetchall()

        if farmacie:
            print(f"Farmacie trovate vicino alle coordinate ({latitudine}, {longitudine}):")
            for farmacia in farmacie:
                print(f"ID: {farmacia[0]}, Nome: {farmacia[1]}, Indirizzo: {farmacia[2]}, Lat: {farmacia[3]}, Lng: {farmacia[4]}")
        else:
            print(f"Nessuna farmacia trovata vicino alle coordinate ({latitudine}, {longitudine}).")

    except sqlite3.Error as e:
        print(f"Errore durante la ricerca delle farmacie: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    lat = float(input("Inserisci la latitudine: "))
    lng = float(input("Inserisci la longitudine: "))
    trova_farmacia_per_coordinate(lat, lng)
