from Services.Auth import Auth
from Services.Sanification import sanitize
from Services.FieldValidation import FieldValidation
import fastapi

class delete_pharmacy_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)



    def delete_pharmacy(self, id, email, token):
        
        id = sanitize(id)
        
        self.auth.isAuth(email=email, token=token)

        query=f'SELECT * FROM pharmacy WHERE id = ?'
        result= self.dbService.selectRAW(query, (id,))
        if result == 0:
            raise fastapi.HTTPException(status_code=404, detail="Pharmacy not found")
        
        try:
            query = f'DELETE FROM pharmacy WHERE id = ?'
            self.dbService.execute(query, (id,))
        except Exception as e:
            raise fastapi.HTTPException(status_code=404, detail=f"Error deleting pharmacy: " + str(e))
        
        return {"status": "success","deleted_pharmacy_id": id}