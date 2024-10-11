from Models.Pharmacy import Pharmacy
from Services.Sanification import sanitize
from Services.FieldValidation import FieldValidation
from Services.Auth import Auth
from tools.Query import BuildQuery
import fastapi  


class SearchByPos_pharmacy_ctl:

    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)


    def search_by_pos(self, latitude, longitude, email, token):
        
        self.auth.isAuth(email=email, token=token)

        query=BuildQuery(Pharmacy).select(["id"]).where([f"lat= {latitude} and lng = {longitude}"]).build()
        print(query)
        if self.dbService.executeRAW(query):
             return {"status": "success", "id_pharmacy": query[0][0]}
        else:
             raise fastapi.HTTPException(status_code=404, detail="Pharmacy not found")
   