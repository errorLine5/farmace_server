from fastapi import APIRouter, FastAPI

from Controllers.worker.add import add_worker_ctl

class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.add = add_worker_ctl(app.db)


  @self.router.post("/addWorker")
  async def add( id_pharmacy: str, id_user: str, permission: str, email: str, token: str, id: str =None):
    return self.add.add_worker(id, id_pharmacy, id_user, permission, email, token)
  





  app.include_router( prefix="/worker", tags=["worker"], router=self.router)
