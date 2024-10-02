from fastapi import APIRouter, FastAPI
from Controllers.controllerTableFill import Fill_ctl 
from fastapi import status, HTTPException
from uuid import uuid4 




class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.fill_ctl = Fill_ctl(app.db)

  

  @self.router.post("/addPharmacy")
  async def fill(name: str , address: str, phone_number: int, latitude: float, longitude: float, nocturn: str, email:str,token: str, id:str = None):
     if id is None:
      id = str(uuid4())
     return self.fill_ctl.fill( id, name, address, phone_number, latitude, longitude, nocturn,email, token)
  
  @self.router.post("/searchByPos")
  async def searchByPos(latitude: float, longitude: float, token: str ):
    return self.fill_ctl.searchByPos(latitude, longitude)

  app.include_router( prefix="/pharmacy" ,tags=["pharmacy"], router=self.router)