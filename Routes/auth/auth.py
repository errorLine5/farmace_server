from fastapi import APIRouter, FastAPI
from Controllers.Auth.Login import Login_ctl
from Controllers.Auth.Register import registerctl
from fastapi import status, HTTPException
from Models.Users import Users



class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.registerctl = registerctl(app.db)
  self.loginctl = Login_ctl(app.db)
  
  
  
  @self.router.post("/login")
  async def login(email: str, password: str): 
    return self.loginctl.login( email, password)

  @self.router.post("/token_test")
  async def token_test(email:str, token:str):
    return self.loginctl.tokenCheck(email, token)
  
  
  @self.router.post("/register" )
  async def register( email: str, username: str, password: str, first_name: str, last_name: str, phone_number: str, picture: str):
    return self.registerctl.register( email, username, password, first_name, last_name, phone_number, picture)
  
  @self.router.post("/verifyemail")
  async def verifyEmail(email: str, email_token: str):
    return self.registerctl.verifyEmail( email, email_token)


  app.include_router( prefix="/auth", router=self.router)
  
  
