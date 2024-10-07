from fastapi import APIRouter, FastAPI
from Controllers.pharmacy.create import create_pharmacy_ctl 
from Controllers.pharmacy.delete import delete_pharmacy_ctl
from Controllers.pharmacy.edit import edit_pharmacy_ctl
from Controllers.pharmacy.searchByPos import SearchByPos_pharmacy_ctl
from Models.Pharmacy import Pharmacy
from uuid import uuid4 




class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.fill_ctl = create_pharmacy_ctl(app.db)
  self.delete_ctl = delete_pharmacy_ctl(app.db)
  self.edit_ctl = edit_pharmacy_ctl(app.db)
  self.SearchByPos = SearchByPos_pharmacy_ctl(app.db)

  

  @self.router.post("/addPharmacy")
  async def fill(name: str , address: str, phone_number: int, latitude: float, longitude: float, nocturn: str, email:str,sito_web: str,token: str, id:str = None):
     if id is None:
      id = str(uuid4())
     return self.fill_ctl.create_farmacy( id, name, address, phone_number, latitude, longitude, nocturn, sito_web, email, token)
  
  @self.router.post("/searchByPos")
  async def searchByPos(latitude: float, longitude: float,email: str, token: str ):
    return self.SearchByPos.search_by_pos(latitude, longitude, email, token)

  @self.router.delete("/deletePharmacy")
  async def deletePharmacy(id: str, email: str, token: str):
    return self.delete_ctl.delete_pharmacy(id, email, token)
  
  @self.router.post("/editPharmacy")
  async def editPharmacy( id:str,pharmacy:Pharmacy, email:str,token: str):
    print(pharmacy)

    return self.edit_ctl.edit_pharmacy( id, pharmacy, email, token)
  
  
  
  
  
  
  
  
  app.include_router( prefix="/pharmacy" ,tags=["pharmacy"], router=self.router)