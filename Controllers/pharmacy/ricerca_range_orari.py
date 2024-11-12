from Models.Pharmacy import Pharmacy
from Services.Auth import Auth
import fastapi
from tools.funzioni_di_ricerca import pharmacy_is_open, pharmacy_in_range

class ricerca_range_orari_ctl():
    def __init__(self, dbservice):
        self.dbService = dbservice
        self.auth = Auth(dbservice)

    def ricerca_range_orari(self, user_lat: float, user_lng: float, range: float,giorno: str, orario_corrente: str) -> list[Pharmacy]:

        query='''SELECT * FROM Pharmacy'''

        pharmacies=self.dbService.selectRAW(query)
        
        pharmacyList=[]
        for pharmacy in pharmacies:
            id, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web = pharmacy
            if pharmacy_in_range(lat, lng, user_lat, user_lng, range) and pharmacy_is_open(orari, giorno, orario_corrente):
                pharmacyList.append({
                    "id": id,
                    "nome_farmacia": nome_farmacia,
                    "indirizzo": indirizzo,
                    "lat": lat,
                    "lng": lng,
                    "orari": orari,
                    "turni": turni,
                    "numeri": numeri,
                    "sito_web": sito_web,
                    "image": image
                })
           
        return pharmacyList