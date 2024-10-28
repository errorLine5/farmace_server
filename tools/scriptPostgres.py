import json
import psycopg2

db_name = 'db.db'
user = 'tuo_username'
password = 'tua_password'
host = 'localhost'
port = '5432'
json_file = 'FRM_FARMA_5_20241025.json'

def upsert_pharmacy_data(db_name, user, password, host, port, json_file):
    conn = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = conn.cursor()

    with open(json_file, 'r') as file:
        data = json.load(file)

    for item in data:
        cursor.execute('''
            INSERT INTO Pharmacy (
                id, nome_farmacia, cap, comune, provincia, regione, nazione,
                indirizzo, lat, lng, orari, turni, numeri, sito_web
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE SET
                nome_farmacia = EXCLUDED.nome_farmacia,
                cap = EXCLUDED.cap,
                comune = EXCLUDED.comune,
                provincia = EXCLUDED.provincia,
                regione = EXCLUDED.regione,
                nazione = EXCLUDED.nazione,
                indirizzo = EXCLUDED.indirizzo,
                lat = EXCLUDED.lat,
                lng = EXCLUDED.lng,
                orari = EXCLUDED.orari,
                turni = EXCLUDED.turni,
                numeri = EXCLUDED.numeri,
                sito_web = EXCLUDED.sito_web
        ''', (
            item['id'], item['nome_farmacia'], item['cap'], item['comune'], 
            item['provincia'], item['regione'], item['nazione'],
            item['indirizzo'], item['lat'], item['lng'], json.dumps(item['orari']), 
            json.dumps(item['turni']), item['numeri'], item['sito_web']
        ))

    conn.commit()
    cursor.close()
    conn.close()

upsert_pharmacy_data(db_name, user, password, host, port, json_file)
