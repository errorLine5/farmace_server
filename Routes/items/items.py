from fastapi import APIRouter, FastAPI
from Controllers.items.create import create_items_ctl 
from Controllers.items.delete import delete_items_ctl
from Controllers.items.edit import edit_items_ctl
from Models.Items import Items
from uuid import uuid4 


class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.fill_ctl = create_items_ctl(app.db)
  self.delete_ctl = delete_items_ctl(app.db)
  self.edit_ctl = edit_items_ctl(app.db)

  @self.router.post("/addItems")
  async def fill(id: str, item_name: str, description_item: str, id_pharmacy: int, price: float, email:str,sito_web: str,token: str ):
     if id is None:
      id = str(uuid4())
     return self.fill_ctl.create_items( id, item_name, description_item, id_pharmacy, price, email, token)

  @self.router.delete("/deletePharmacy")
  async def deleteItems(id: str, email: str, token: str):
    return self.delete_ctl.delete_items(id, email, token)
  
  @self.router.post("/editPharmacy")
  async def editItems( id:str, items:Items, email:str,token: str):
    print(items)

    return self.edit_ctl.edit_items( id, items, email, token)
  
  app.include_router( prefix="/items" ,tags=["items"], router=self.router)