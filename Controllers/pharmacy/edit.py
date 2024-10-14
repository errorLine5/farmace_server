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

    def edit_pharmacy(self, id, nome_farmacia, indirizzo, lat, lng,  orari, turni, numeri,sito_web, email , token):
        id = sanitize(id)
        
        self.auth.isAuth(email=email, token=token)
        
        query = f'SELECT * FROM pharmacy WHERE id = ?'
        result=self.dbService.select(query, (id,)) 
        if not result:
            
            raise fastapi.HTTPException(status_code=404, detail="Pharmacy not found")

        editedPharmacy=Pharmacy(
            id=id,
            nome_farmacia=nome_farmacia,
            indirizzo=indirizzo,
            lat=lat,
            lng=lng,
            orari=orari,
            turni=turni,
            numeri=numeri,
            sito_web=sito_web
        )
        print(editedPharmacy)
        try:
            query = f'UPDATE pharmacy SET nome_farmacia = ?, indirizzo = ?,  lat = ?, lng = ?, orari = ?, turni = ?, numeri = ?, sito_web = ? WHERE id = ?'
            
            self.dbService.execute(query, (editedPharmacy.nome_farmacia, editedPharmacy.indirizzo,  editedPharmacy.lat, editedPharmacy.lng, editedPharmacy.orari, editedPharmacy.turni, editedPharmacy.numeri, editedPharmacy.sito_web, id))
        except Exception as e:
            raise fastapi.HTTPException(status_code=500, detail="Error editing pharmacy: " + str(e))
        
        return {"status": "success","edited_pharmacy_id": id}
