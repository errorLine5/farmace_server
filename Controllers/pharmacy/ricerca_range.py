from Models.Pharmacy import Pharmacy
from Services.Auth import Auth
import fastapi
from tools.funzioni_di_ricerca import haversine_formula, pharmacy_in_range



class ricerca_ctl():

    def __init__(self, dbservice):
        self.dbService = dbservice
        self.auth = Auth(dbservice)

    def ricerca(self, user_lat, user_lng, range)->list[Pharmacy]:
        query='''SELECT * FROM Pharmacy'''

        pharmacies=self.dbService.selectRAW(query)
        
        pharmacyList=[]
        for pharmacy in pharmacies:
            id, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web = pharmacy
            if pharmacy_in_range(lat, lng, user_lat, user_lng, range):
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
                })

        return pharmacyList