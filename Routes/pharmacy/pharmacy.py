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
  async def fill(nome: str , indirizzo: str, lat: float, lng:float, orari:str, turni:str, numeri:str, sito_web: str,  email:str, worker_id: str, token: str, id: str = None):
     if id is None:
      id = str(uuid4())
     return self.fill_ctl.create_farmacy( id, nome, indirizzo, lat, lng, orari, turni, numeri, sito_web, email, worker_id, token)
  
  @self.router.post("/searchByPos")
  async def searchByPos(latitude: float, longitude: float,email: str, token: str ):
    return self.SearchByPos.search_by_pos(latitude, longitude, email, token)

  @self.router.delete("/deletePharmacy")
  async def deletePharmacy(id: str, email: str, token: str):
    return self.delete_ctl.delete_pharmacy(id, email, token)
  
  @self.router.post("/editPharmacy")
  async def editPharmacy( id:str, nome_farmacia: str, indirizzo: str, lat:  float, lng: float, orari: str, turni: str, numeri:str, sito_web: str, email:str, token: str):

    return self.edit_ctl.edit_pharmacy( id, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web, email, token)
  
  
  
  app.include_router( prefix="/pharmacy" ,tags=["pharmacy"], router=self.router)