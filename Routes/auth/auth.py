from fastapi import APIRouter, FastAPI
from Controllers.Auth.Login import Login_ctl
from Controllers.Auth.Register import registerctl
from fastapi import status, HTTPException
from Models.Users import Users
from Models.Users import authParameters



class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.registerctl = registerctl(app.db)
  self.loginctl = Login_ctl(app.db)
  
  
  
  @self.router.post("/login")
  async def login(authParams:authParameters):
    email = authParams.email
    password = authParams.password 
    return self.loginctl.login( email, password)

  @self.router.post("/token_test")
  async def token_test(authParams:authParameters):
    email = authParams.email
    token = authParams.token
    return self.loginctl.tokenCheck(email, token)
  
  
  @self.router.post("/register" )
  async def register( user: Users):
    email = user.email
    username = user.username
    password = user.password
    first_name = user.first_name
    last_name = user.last_name
    phone_number = user.phone_number
    picture = user.picture
    return self.registerctl.register( email, username, password, first_name, last_name, phone_number, picture)
  
  @self.router.post("/verifyemail")
  async def verifyEmail(authParams:authParameters):
    email = authParams.email
    email_token = authParams.email_token
    return self.registerctl.verifyEmail( email, email_token)


  app.include_router( prefix="/auth", router=self.router)
  
  
