from Services.Auth import Auth
from Services.Sanification import sanitize
from Services.FieldValidation import FieldValidation
from tools.Query import BuildQuery
from Models.Pharmacy import Pharmacy
from Services.Database.dbsqlite import DBSqlite
import fastapi

class edit_pharmacy_ctl:
    def __init__(self, dbService:DBSqlite):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def edit_pharmacy(self, id, pharmacy:Pharmacy, email , token):
        print (id)
        
        self.auth.isAuth(email=email, token=token)
        
        query = f'SELECT * FROM pharmacy WHERE id = "{id}"' #this is not efficient
        if len( self.dbService.selectRAW(query)) == 0:
            raise fastapi.HTTPException(status_code=404, detail="Pharmacy not found")

        
        try:
            query = f'UPDATE pharmacy SET nome_farmacia = ?, indirizzo = ?, numeri = ?, lat = ?, lng = ?, turni = ?, orari = ?, sito_web = ? WHERE id = "{id}"'
            print(query)
            self.dbService.execute(query, (pharmacy.nome_farmacia, pharmacy.indirizzo, pharmacy.numeri, pharmacy.lat, pharmacy.lng, pharmacy.turni, pharmacy.orari, pharmacy.sito_web))
        except Exception as e:
            return fastapi.HTTPException(status_code=404, detail="Error editing pharmacy: " + str(e))
        
        return {"status": "success","edited_pharmacy_id": id}
