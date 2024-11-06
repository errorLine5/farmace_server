from Services.Auth import Auth
from Services.Sanification import sanitize
from Services.FieldValidation import FieldValidation
from tools.Query import BuildQuery
from Models.Items import Items
from Services.Database.dbsqlite import DBSqlite
import fastapi

class edit_items_ctl:
    def __init__(self, dbService:DBSqlite):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def edit_items(self, id, items: Items,  email, token):

        id = sanitize(id)
        
        
        self.auth.isAuth(email=email, token=token)

        query = f'SELECT * FROM pharmacy WHERE id = ?'
        result=self.dbService.selectRAW(query, (id,)) 
        if not result:
            raise fastapi.HTTPException(status_code=404, detail="Items not found")

        try:  
            query = f'UPDATE items SET item_name = ?, description_item = ?, id_pharmacy = ?, price = ?, WHERE id = ?'
            self.dbService.execute(query, (items.nome, items.description_item, items.id_pharmacy, items.price,  id))
        except Exception as e:
            raise fastapi.HTTPException(status_code=500, detail="Error editing pharmacy: " + str(e))
        
        return {"status": "success","edited_items_id": id}