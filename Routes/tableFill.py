from fastapi import APIRouter, FastAPI
from Controllers.controllerTableFill import Fill_ctl 
from fastapi import status, HTTPException



class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.fill_ctl = Fill_ctl(app.db)

  

  @self.router.post("/fill")
  async def fill(id: str, name: str, address: str, phone_number: int, latitude: float, longitude: float, nocturn: str):
     return self.fill_ctl.fill( id, name, address, phone_number, latitude, longitude, nocturn)
  

  app.include_router( prefix="/tableFill" ,tags=["tableFill"], router=self.router)