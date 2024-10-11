from Services.Auth import Auth
import fastapi

class delete_pharmacy_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def delete_pharmacy(self, id, email, token):
        
        self.auth.isAuth(email=email, token=token)

        query=f'SELECT * FROM pharmacy WHERE id = "{id}"'
        if len(self.dbService.selectRAW(query)) == 0:
            raise fastapi.HTTPException(status_code=404, detail="Pharmacy not found")
        
        try:
            query = f'DELETE FROM pharmacy WHERE id = "{id}"'
            self.dbService.execute(query)
        except Exception as e:
            return fastapi.HTTPException(status_code=404, detail="Error deleting pharmacy: " + str(e))
        
        return {"status": "success","deleted_pharmacy_id": id}