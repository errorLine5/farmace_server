from Services.Auth import Auth
from Services.Sanification import sanitize
from Services.FieldValidation import FieldValidation
import fastapi

class delete_items_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)
        
    def delete_items(self, id, email, token):

        id = sanitize (id)

        self.authisAuth(email=email, token=token)

        query='SELECT id FROM Items Where id=?'
        result= self.dbService.selectRAW(query, (id,))
        if not result:
            raise fastapi.HTTPException(status_code=404, detail="Items not found")
            
        try:
            query='DELETE FROM items WHERE id=?'
            self.dbService.execute(query, (id,))

        except Exception as e :
                raise fastapi.HTTPException(status_code=404, detail=f"Error deleting items: " + str(e))
            
        return {"status": "success","deleted_items_id": id}