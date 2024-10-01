from fastapi import APIRouter, FastAPI
from Controllers.Auth.Login import Login_ctl
from Controllers.Auth.Register import registerctl
from fastapi import status, HTTPException



class Auth:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.registerctl = registerctl(app.db)
  self.loginctl = Login_ctl(app.db)
  
  
  @self.router.post("/login")
  async def login(email: str, password: str): 
    return self.loginctl.login( email, password)


    
  
  @self.router.post("/register" )
  async def register(email: str, password: str, first_name: str, last_name: str, phone_number: str, picture: str ):
    return self.registerctl.register( email, password, first_name, last_name, phone_number, picture)
  
  
  app.include_router( prefix="/auth", router=self.router) 

