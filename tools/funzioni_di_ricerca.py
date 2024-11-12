import math
import json
from Models.Pharmacy import Pharmacy
from datetime import datetime

def haversine_formula(lat1, lng1, lat2, lng2)->float:
    
    R = 6371  # Raggio della terra in km  

    lat1, lng1, lat2, lng2 = map(math.radians, [lat1, lng1, lat2, lng2]) #conversione da float a radianti, servira poi per la formula completa

    dlat=lat2-lat1   #delta tra le due latitudini, differenza

    dlng=lng2-lng1   #delta tra le due longitudini, differenza

    #formula dell'haversine

    a=math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlng/2)**2 

    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    distanza=R*c

    return distanza



def pharmacy_is_open(orari_farmacia, giorno, orario_corrente)->bool:
    #orari_farmacia è il parametro di tipo LISTA della classe farmacia che corrisponde a orari
    #GIORNO è il nome del giorno corrente che serve per controllare se la farmacia è chiusa
    #orario_corrente è il parametro di tipo stringa che corrisponde all'orario attuale
    orari_farmacia=json.loads(orari_farmacia)
    
    orario_corrente_dt=datetime.strptime(orario_corrente, '%H:%M')
    print(orario_corrente_dt)

    giorni_settimana={"lunedi":0, "martedi":1, "mercoledi":2, "giovedi":3, "venerdi":4, "sabato":5, "domenica":6}

    index_giorno=giorni_settimana.get(giorno.lower())
    if index_giorno is None:
        return False
    
    orari_giorno=orari_farmacia[index_giorno]
    print (orari_giorno)

    for fascia_oraria in orari_giorno:
        apertura,chiusura=fascia_oraria
        if apertura is None or chiusura is None:
            continue

        apertura_dt=datetime.strptime(apertura, '%H:%M')
        chiusura_dt=datetime.strptime(chiusura, '%H:%M')

        if apertura_dt <= orario_corrente_dt <= chiusura_dt:
            return True

    return False

#   FORMATO ORARI
#  '''orari_settimanali = [
#     [ ["09:00", "12:30"], ["15:30", "18:00"]],  # Lunedì
#     [ ["09:00", "12:30"], ["15:30", "18:00"]],  # Martedì
#     [ ["09:00", "12:30"], ["15:30", "18:00"]],  # Mercoledì
#     [ ["09:00", "12:30"], ["15:30", "18:00"]],  # Giovedì
#     [ ["09:00", "12:30"], ["15:30", "18:00"]],  # Venerdì
#     [ ["09:00", "13:00"], ["15:30", "18:00"]],   # Sabato
#     [ [None, None], [None, None]]               # Domenica
# ]'''

def pharmacy_in_range(pharmacy_lat:float, pharmacy_lng:float,user_lat:float, user_lng:float, range:float):
    distanza=haversine_formula(user_lat,user_lng,pharmacy_lat,pharmacy_lng)
    if distanza<=range:
        return True
