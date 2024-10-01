from fastapi import FastAPI, APIRouter
from Controllers.testProtected import TestProtected

class Route:
 def __init__(self, app : FastAPI):
  self.router  = APIRouter( ) #create an instance of the router
  self.testProtected = TestProtected(app.db) #create an instance of the controller
  
  @self.router.post("/test") #create a route
  async def test(email:str, token:str, data: str): #
    return self.testProtected.getUserInfo(email, token)

  app.include_router( prefix="/protected" ,tags=["protected"], router=self.router) 
