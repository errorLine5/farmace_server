from fastapi import APIRouter, FastAPI
from Controllers.pharmacy.create import create_pharmacy_ctl 
from Controllers.pharmacy.delete import delete_pharmacy_ctl
from Controllers.pharmacy.edit import edit_pharmacy_ctl

from uuid import uuid4 




class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.fill_ctl = create_pharmacy_ctl(app.db)
  self.delete_ctl = delete_pharmacy_ctl(app.db)
  self.edit_ctl = edit_pharmacy_ctl(app.db)
  #self.addWorker_ctl = add_Worker_ctl(app.db)

  

  @self.router.post("/addPharmacy")
  async def fill(name: str , address: str, phone_number: int, latitude: float, longitude: float, nocturn: str, email:str,token: str, id:str = None):
     if id is None:
      id = str(uuid4())
     return self.fill_ctl.create_farmacy( id, name, address, phone_number, latitude, longitude, nocturn,email, token)
  
  @self.router.post("/searchByPos")
  async def searchByPos(latitude: float, longitude: float, token: str ):
    return self.fill_ctl.searchByPos(latitude, longitude)

  @self.router.delete("/deletePharmacy")
  async def deletePharmacy(id: str, token: str):
    return self.delete_ctl.deletePharmacy(id, token)
  
  @self.router.post("/editPharmacy")
  async def editPharmacy(id: str, name: str , address: str, phone_number: int, latitude: float, longitude: float, nocturn: str, email:str,token: str):
    return self.edit_ctl.edit_pharmacy(id, name, address, phone_number, latitude, longitude, nocturn,email, token)
  
  # @self.router.post("/addWorker")
  # async def addWorker(id:str, id_pharmacy: str, id_user:str, permission: int, email: str, token: str):
  #  return self.addWorker_ctl.addWorker(id, id_pharmacy, id_user, permission, email, token)
  
  
  app.include_router( prefix="/pharmacy" ,tags=["pharmacy"], router=self.router)