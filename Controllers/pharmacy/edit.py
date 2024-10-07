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
        id = sanitize(id)
        name = sanitize(name)
        address = sanitize(address)
        nocturn = sanitize(nocturn)
        self.auth.isAuth(email=email, token=token)
        
        query = BuildQuery(Pharmacy).select(['id']).where([f"id = '{id}'"]).build()

        if self.dbService.executeRAW(query):
            query = "UPDATE pharmacy SET name = ?, address = ?, phone_number = ?, latitude = ?, longitude = ?, nocturn = ? WHERE id = ?"

        else:
            raise fastapi.HTTPException(status_code=404, detail="Pharmacy not found")

        self.dbService.execute(query, (name, address, phone_number, latitude, longitude, nocturn, id))
        
        return {"status": "success","edited_pharmacy_id": id}
