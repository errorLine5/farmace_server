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
    #orari_farmacia è il parametro di tipo json della classe farmacia che corrisponde a orari
    #GIORNO è il nome del giorno corrente che serve per controllare se la farmacia è chiusa
    #orario_corrente è il parametro di tipo stringa che corrisponde all'orario attuale
    orari_farmacia=json.loads(orari_farmacia)
    
    orario_corrente_dt=datetime.strptime(orario_corrente, '%H:%M')
    print(orario_corrente_dt)
    orari_giorno=orari_farmacia.get(giorno.lower())
    print (orari_giorno)

    if orari_giorno:
        apertura=orari_giorno.get('apertura')
        chiusura=orari_giorno.get('chiusura')

        if apertura.lower() != 'chiuso' and chiusura.lower() != 'chiuso':
             apertura_dt=datetime.strptime(apertura, '%H:%M')
             chiusura_dt=datetime.strptime(chiusura, '%H:%M')

             if apertura_dt <= orario_corrente_dt <= chiusura_dt:
                 return True

# {
#     "lunedì": {"apertura": "08:00", "chiusura": "20:00"},
#     "martedì": {"apertura": "08:00", "chiusura": "20:00"},
#     "mercoledì": {"apertura": "08:00", "chiusura": "20:00"},
#     "giovedì": {"apertura": "08:00", "chiusura": "20:00"},
#     "venerdì": {"apertura": "08:00", "chiusura": "20:00"},
#     "sabato": {"apertura": "09:00", "chiusura": "13:00"},
#     "domenica": {"apertura": "Chiuso", "chiusura": "Chiuso"}
# }

def pharmacy_in_range(pharmacy_lat:float, pharmacy_lng:float,user_lat:float, user_lng:float, range:float):
    distanza=haversine_formula(user_lat,user_lng,pharmacy_lat,pharmacy_lng)
    if distanza<=range:
        return True
