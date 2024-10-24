from fastapi import APIRouter, FastAPI
from Controllers.pharmacy.create import create_pharmacy_ctl 
from Controllers.pharmacy.delete import delete_pharmacy_ctl
from Controllers.pharmacy.edit import edit_pharmacy_ctl
from Controllers.pharmacy.searchByPos import SearchByPos_pharmacy_ctl
from Controllers.pharmacy.ricerca import ricerca_ctl
from uuid import uuid4 




class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.fill_ctl = create_pharmacy_ctl(app.db)
  self.delete_ctl = delete_pharmacy_ctl(app.db)
  self.edit_ctl = edit_pharmacy_ctl(app.db)
  self.SearchByPos = SearchByPos_pharmacy_ctl(app.db)
  self.ricerca_ctl = ricerca_ctl(app.db)

  

  @self.router.post("/addPharmacy")
  async def fill(nome: str , indirizzo: str, lat: float, lng:float, orari:str, turni:str, numeri:str, sito_web: str, email:str,  token: str, id: str = None):
     if id is None:
      id = str(uuid4())
     return self.fill_ctl.create_farmacy( id, nome, indirizzo, lat, lng, orari, turni, numeri, sito_web, email, token)
  
  @self.router.post("/searchByPos")
  async def searchByPos(minLat: float, maxLat: float, minLng: float, maxLng: float,email: str, token: str ):
    return self.SearchByPos.search_by_pos(minLat, maxLat, minLng, maxLng, email, token)

  @self.router.delete("/deletePharmacy")
  async def deletePharmacy(pharmacy_id: str, worker_id: str, email: str, token: str):
    return self.delete_ctl.delete_pharmacy(pharmacy_id, worker_id, email, token)
  
  @self.router.post("/editPharmacy")
  async def editPharmacy( id_pharmacy: str, nome_farmacia: str, indirizzo: str, lat:  float, lng: float, orari: str, turni: str, numeri:str, sito_web: str, worker_id: str, email:str, token: str):

    return self.edit_ctl.edit_pharmacy( id_pharmacy, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web, worker_id, email, token)
  
  @self.router.post("/ricerca")
  async def ricerca(user_lat: float, user_lng: float, range: float):
    return self.ricerca_ctl.ricerca(user_lat, user_lng, range)
  
  app.include_router( prefix="/pharmacy" ,tags=["pharmacy"], router=self.router)