import datetime
import json
import re
from uuid import uuid4
from Models.Items import Items
from Services.Sanification import sanitize
import fastapi
from Services.FieldValidation import FieldValidation
from Services.Auth import Auth
from tools.Query import BuildQuery

class create_items_ctl:
 def __init__(self, dbService):
  self.dbService = dbService
  self.auth = Auth(dbService)

  def create_items(self, id, item_name , description_item, id_pharmacy, price, email, token):
    id = sanitize(id)
    item_name = sanitize(item_name)
    description_item = sanitize(description_item) 
    id_pharmacy = sanitize(id_pharmacy)
    price = sanitize(price)

    self.auth.isAuth(email=email, token=token)

    if id is None:
        id = str(uuid4())

    queryItems ='SELECT id FROM Pharmacy WHERE id =? '

    resultItems = self.dbService.select(queryItems, (id_pharmacy,))

    if not resultItems:
            raise fastapi.HTTPException(status_code=404, detail="Items not found")
    
    newItems = Items(
        id = id,
        item_name= item_name,
        description_item=  description_item,
        id_pharmacy = id_pharmacy,
        price = price
    )

    query=BuildQuery(newItems).insert_into().build()
    self.dbService.executeRAW(query)

    return {"status": "success", "id_items": id}


     