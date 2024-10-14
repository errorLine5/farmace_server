from fastapi import APIRouter, FastAPI

from Controllers.worker.add import add_worker_ctl
from Controllers.worker.delete import delete_worker_ctl
from Controllers.worker.edit import edit_worker_ctl
from Models.Worker import Worker
class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.add = add_worker_ctl(app.db)
  self.delete= delete_worker_ctl(app.db)
  self.edit = edit_worker_ctl(app.db)

  @self.router.post("/addWorker")
  async def add( id_pharmacy: str, id_user: str, permission: str, email: str, token: str, id: str =None):
    return self.add.add_worker(id, id_pharmacy, id_user, permission, email, token)
  
  @self.router.delete("/deleteWorker")
  async def delete(id: str, email: str, token: str):
    return self.delete.delete_worker(id, email, token)  

  @self.router.post("/editWorker")
  async def edit( id:str, worker:Worker, email: str, token: str):
    return self.edit.edit_worker(id, worker, email, token) 



  app.include_router( prefix="/worker", tags=["worker"], router=self.router)
