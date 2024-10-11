
from Services.Auth import Auth
from Services.FieldValidation import FieldValidation
from Services.Sanification import sanitize
import fastapi

class Add_Worker_ctl():
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def add_worker(self, id, id_pharmacy, id_user, permission, email, token):
        
       self.auth.isAuth(email, token)
       
       controllo_Pharmacy_User="SELECT * FROM works WHERE pharmacy_id = ? AND user_id = ?" 
       controllo_id_Worker="SELECT * FROM works WHERE id = ?"
       
       res=self.dbService.select(controllo_Pharmacy_User, [id_pharmacy, id_user])
       
       if len(res) == 0:
            raise fastapi.HTTPException(status_code=404, detail="Pharmacy or User not found")
            return {"status": "error", "detail": "Pharmacy or User not found"}
       
       res=self.dbService.select(controllo_id_Worker, [id])
       
       if len(res) != 0:
            raise fastapi.HTTPException(status_code=404, detail="Worker already exists")
            return {"status": "error", "detail": "Worker already exists"}
       
       else:
            
            query= "INSERT INTO works (id, pharmacy_id, user_id, permission) VALUES (?, ?, ?, ?)"
            self.dbService.execute(query, (id, id_pharmacy, id_user, permission))
            return {"status": "success"}