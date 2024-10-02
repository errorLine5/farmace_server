from fastapi import APIRouter, FastAPI
from Controllers.pharmacy.create import create_pharmacy_ctl 

from uuid import uuid4 




class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.fill_ctl = create_pharmacy_ctl(app.db)

  

  @self.router.post("/addPharmacy")
  async def fill(name: str , address: str, phone_number: int, latitude: float, longitude: float, nocturn: str, email:str,token: str, id:str = None):
     if id is None:
      id = str(uuid4())
     return self.fill_ctl.create_farmacy( id, name, address, phone_number, latitude, longitude, nocturn,email, token)
  
  @self.router.post("/searchByPos")
  async def searchByPos(latitude: float, longitude: float, token: str ):
    return self.fill_ctl.searchByPos(latitude, longitude)

  app.include_router( prefix="/pharmacy" ,tags=["pharmacy"], router=self.router)

  @self.router.delete("/deletePharmacy")
  async def deletePharmacy(id: str, token: str):
    return self.fill_ctl.deletePharmacy(id, token)