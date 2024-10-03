import sqlite3
import json

def ottieni_info_farmacia(id_farmacia):
    try:
        conn = sqlite3.connect('database.db')  
        cursor = conn.cursor()

        cursor.execute("""
        SELECT nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web
        FROM Pharmacy
        WHERE id = ?
        """, (id_farmacia,))
        farmacia = cursor.fetchone()

        if farmacia:
            info_farmacia = {
                "Nome": farmacia[0],
                "Indirizzo": farmacia[1],
                "Latitudine": farmacia[2],
                "Longitudine": farmacia[3],
                "Orari": farmacia[4],
                "Turni": farmacia[5],
                "Numero di telefono": farmacia[6],
                "Sito web": farmacia[7]
            }

            print(json.dumps(info_farmacia, indent=4))
            for chiave, valore in info_farmacia.items():
                print(f"{chiave}: {valore}")

            return info_farmacia
        else:
            print(f"Nessuna farmacia trovata con ID {id_farmacia}.")

    except sqlite3.Error as e:
        print(f"Errore durante l'ottenimento delle informazioni della farmacia: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    id_farmacia = int(input("Inserisci l'ID della farmacia da visualizzare: "))
    ottieni_info_farmacia(id_farmacia)
