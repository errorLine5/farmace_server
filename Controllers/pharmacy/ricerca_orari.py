from Models.Pharmacy import Pharmacy
from Services.Auth import Auth
import fastapi
from tools.funzioni_di_ricerca import pharmacy_is_open

class ricerca_orari_ctl:
    def __init__(self, dbservice):
        self.dbService = dbservice
        self.auth = Auth(dbservice)

    def ricerca_farmacia_aperta(self,giorno, orario_corrente)->list[Pharmacy]:

        query='''SELECT * FROM Pharmacy'''
        farmacie=self.dbService.selectRAW(query)

        farmacie_aperte=[]
        for farmacia in farmacie:
            id, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web = farmacia
            print(id)
            if pharmacy_is_open(orari, giorno, orario_corrente):
                farmacie_aperte.append({
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
        return farmacie_aperte
