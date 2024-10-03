from Services.Auth import Auth
import fastapi

class delete_pharmacy_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def delete_pharmacy(self, id, token):
        self.auth.isAuth(token)
        query = "DELETE FROM pharmacy WHERE id = ?"
        self.dbService.delete(query, (id,))
        if self.dbService.execute(query, (id,)):
            return {"status": "success"}
        else:
            raise fastapi.HTTPException(status_code=404, detail="Pharmacy not found")