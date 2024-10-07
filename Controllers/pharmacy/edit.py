from Services.Auth import Auth
from Services.Sanification import sanitize
from Services.FieldValidation import FieldValidation
from tools.Query import BuildQuery
from Models.Pharmacy import Pharmacy
import fastapi

class edit_pharmacy_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def edit_pharmacy(self, id, name, address, phone_number, latitude, longitude, nocturn, email , token):
        
        print(id)
        self.auth.isAuth(email=email, token=token)
        
        query = BuildQuery(Pharmacy).select(['id']).where([f"id = '{id}'"]).build()

        if self.dbService.executeRAW(query):
            query = f"UPDATE pharmacy SET nome_farmacia = ?, indirizzo = ?, numeri = ?, lat = ?, lng = ?, turni = ?, orari = ?, sito_web = ? WHERE id = {id}"

        else:
            raise fastapi.HTTPException(status_code=404, detail="Pharmacy not found")

        self.dbService.execute(query, (name, address, phone_number, latitude, longitude, nocturn))
        
        return {"status": "success","edited_pharmacy_id": id}
