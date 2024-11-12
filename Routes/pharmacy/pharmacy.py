from fastapi import APIRouter, FastAPI
from Controllers.pharmacy.create import create_pharmacy_ctl 
from Controllers.pharmacy.delete import delete_pharmacy_ctl
from Controllers.pharmacy.edit import edit_pharmacy_ctl
from Controllers.pharmacy.searchByPos import SearchByPos_pharmacy_ctl
from Controllers.pharmacy.ricerca_range import ricerca_ctl
from Controllers.pharmacy.ricerca_orari import ricerca_orari_ctl
from Controllers.pharmacy.ricerca_range_orari import ricerca_range_orari_ctl
from Models.Pharmacy import Pharmacy, Coordinates_Range, date_time
from Models.Users import authParameters
from Models.Worker import Worker
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
     print (pharmacy)
     id = pharmacy.id
     nome = pharmacy.nome_farmacia
     indirizzo = pharmacy.indirizzo
     lat = pharmacy.lat
     lng = pharmacy.lng
     orari = pharmacy.orari
     turni = pharmacy.turni
     numeri = pharmacy.numeri
     sito_web = pharmacy.sito_web
     image = pharmacy.image
     email = authParams.email
     token = authParams.token
     if id is None or id == "":
      print ("id is None")

      id = str(uuid4())
      print ("id is now " + id)

     return self.fill_ctl.create_farmacy( id, nome, indirizzo, lat, lng, orari, turni, numeri, sito_web, image, email, token)
  
  @self.router.post("/searchByPos")
  async def searchByPos( minCoord: Coordinates_Range, maxCoord: Coordinates_Range, authParams: authParameters):
    minLat= minCoord.lat
    minLng= minCoord.lng
    maxLat= maxCoord.lat
    maxLng= maxCoord.lng
    email = authParams.email
    token = authParams.token

    return self.SearchByPos.search_by_pos(minLat, maxLat, minLng, maxLng, email, token, )

  @self.router.delete("/deletePharmacy")
  async def deletePharmacy(pharmacy: Pharmacy, worker: Worker, authParams: authParameters):
    pharmacy_id = pharmacy.id
    worker_id = worker.id
    email = authParams.email
    token = authParams.token
    return self.delete_ctl.delete_pharmacy(pharmacy_id, worker_id, email, token)
  
  @self.router.post("/editPharmacy")
  async def editPharmacy( pharmacy: Pharmacy, worker:Worker, authParams: authParameters):
    id_pharmacy = pharmacy.id
    nome_farmacia = pharmacy.nome_farmacia
    indirizzo = pharmacy.indirizzo
    lat = pharmacy.lat
    lng = pharmacy.lng
    orari = pharmacy.orari
    turni = pharmacy.turni
    numeri = pharmacy.numeri
    sito_web = pharmacy.sito_web
    email = authParams.email
    token = authParams.token
    worker_id = worker.id

    return self.edit_ctl.edit_pharmacy( id_pharmacy, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web, worker_id, email, token)
  
  @self.router.post("/ricerca")
  async def ricerca(userCoord: Coordinates_Range):
    user_lat = userCoord.latitude
    user_lng = userCoord.longitude
    range = userCoord.range
    return self.ricerca_ctl.ricerca(user_lat, user_lng, range)
  
  @self.router.post("/ricerca_orari")
  async def ricerca_orari(orarioRicerca: date_time):
    giorno = orarioRicerca.giorno
    orario_corrente = orarioRicerca.orario_corrente
    return self.ricerca_orari_ctl.ricerca_farmacia_aperta(giorno,orario_corrente)
  
  
  @self.router.post("/ricerca_range_orari")
  async def ricerca_range_orari(userCoord: Coordinates_Range, orarioRicerca: date_time):
    user_lat = userCoord.latitude
    user_lng = userCoord.longitude
    range = userCoord.range
    giorno = orarioRicerca.giorno 
    orario_corrente = orarioRicerca.orario_corrente
    return self.ricerca_range_orari_ctl.ricerca_range_orari(user_lat, user_lng, range,giorno, orario_corrente)
  
  
  
  
  app.include_router( prefix="/pharmacy" ,tags=["pharmacy"], router=self.router)