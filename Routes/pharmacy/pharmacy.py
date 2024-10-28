from fastapi import APIRouter, FastAPI
from Controllers.pharmacy.create import create_pharmacy_ctl 
from Controllers.pharmacy.delete import delete_pharmacy_ctl
from Controllers.pharmacy.edit import edit_pharmacy_ctl
from Controllers.pharmacy.searchByPos import SearchByPos_pharmacy_ctl
from Controllers.pharmacy.ricerca_range import ricerca_ctl
from Controllers.pharmacy.ricerca_orari import ricerca_orari_ctl
from Controllers.pharmacy.ricerca_range_orari import ricerca_range_orari_ctl
from Models.Pharmacy import Pharmacy
from Models.Users import authParameters
from uuid import uuid4 




class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.fill_ctl = create_pharmacy_ctl(app.db)
  self.delete_ctl = delete_pharmacy_ctl(app.db)
  self.edit_ctl = edit_pharmacy_ctl(app.db)
  self.SearchByPos = SearchByPos_pharmacy_ctl(app.db)
  self.ricerca_ctl = ricerca_ctl(app.db)
  self.ricerca_orari_ctl = ricerca_orari_ctl(app.db)
  self.ricerca_range_orari_ctl = ricerca_range_orari_ctl(app.db)
  

  @self.router.post("/addPharmacy")
  async def fill(pharmacy: Pharmacy, authParams : authParameters):
     id = pharmacy.id
     nome = pharmacy.nome_farmacia
     indirizzo = pharmacy.indirizzo
     lat = pharmacy.lat
     lng = pharmacy.lng
     orari = pharmacy.orari
     turni = pharmacy.turni
     numeri = pharmacy.numeri
     sito_web = pharmacy.sito_web
     email = authParameters.email
     token = authParameters.token
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
  
  @self.router.post("/ricerca_orari")
  async def ricerca_orari(giorno:str, orario_corrente:str):
    return self.ricerca_orari_ctl.ricerca_farmacia_aperta(giorno,orario_corrente)
  
  
  @self.router.post("/ricerca_range_orari")
  async def ricerca_range_orari(user_lat: float, user_lng: float, range: float,giorno: str, orario_corrente: str):
    return self.ricerca_range_orari_ctl.ricerca_range_orari(user_lat, user_lng, range,giorno, orario_corrente)
  
  
  
  
  app.include_router( prefix="/pharmacy" ,tags=["pharmacy"], router=self.router)