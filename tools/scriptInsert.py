import json
import sqlite3

db_name = 'db.db'
json_file = 'FRM_FARMA_5_20241025.json'

def upsert_pharmacy_data(db_name, json_file):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    with open(json_file, 'r') as file:
        data = json.load(file)

    for item in data:
        cursor.execute('''
            INSERT INTO Pharmacy (
                id, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                nome_farmacia = excluded.nome_farmacia,
                indirizzo = excluded.indirizzo,
                lat = excluded.lat,
                lng = excluded.lng,
                orari = excluded.orari,
                turni = excluded.turni,
                numeri = excluded.numeri,
                sito_web = excluded.sito_web
        ''', (
            item['id'], item['nome_farmacia'], item['indirizzo'], item['lat'], item['lng'], json.dumps(item['orari']), 
            json.dumps(item['turni']), item['numeri'], item['sito_web']
        ))

    conn.commit()
    conn.close()
    
upsert_pharmacy_data(db_name, json_file)
