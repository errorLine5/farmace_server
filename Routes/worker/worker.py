from fastapi import APIRouter, FastAPI

from Controllers.worker.add import add_worker_ctl
from Controllers.worker.delete import delete_worker_ctl
from Controllers.worker.edit import edit_worker_ctl
from Models.Worker import Worker
from Models.Users import authParameters, Users
from Models.Pharmacy import Pharmacy
class Route:

 def __init__(self, app : FastAPI):
  self.router  = APIRouter()
  self.add = add_worker_ctl(app.db)
  self.delete= delete_worker_ctl(app.db)
  self.edit = edit_worker_ctl(app.db)

  @self.router.post("/addWorker")
  async def add(worker: Worker, authParams: authParameters):
    id = None
    id_pharmacy = worker.id_pharmacy
    id_user = worker.id_user
    permission = worker.permission
    email = authParams.email
    token = authParams.token
    return self.add.add_worker(id, id_pharmacy, id_user, permission,  email, token)
  
  @self.router.delete("/deleteWorker")
  async def delete(worker: Worker, authParams: authParameters):
    id = worker.id
    email = authParams.email
    token = authParams.token
    return self.delete.delete_worker(id, email, token)  

  @self.router.post("/editWorker")
  async def edit(worker:Worker, admin:Worker, authParams: authParameters):
    id = worker.id
    id_pharmacy = worker.id_pharmacy
    id_user = worker.id_user
    permission = worker.permission
    worker_id = admin.id
    email = authParams.email
    token = authParams.token
    return self.edit.edit_worker(id, id_pharmacy, id_user, permission, worker_id, email, token) 



  app.include_router( prefix="/worker", tags=["worker"], router=self.router)
