from fastapi import APIRouter, FastAPI


from Controllers.worker.add_worker import Add_Worker_ctl



class Route:
    def __init__(self, app : FastAPI):
        self.router = APIRouter()
        self.addWorker_ctl = Add_Worker_ctl(app.db)

        @self.router.post("/addWorker")
        async def addWorker(id:str, id_pharmacy: str, id_user:str, permission: int, email: str, token: str):
            return self.addWorker_ctl.add_worker(id, id_pharmacy, id_user, permission, email, token)

        app.include_router(prefix="/worker", tags=["worker"], router=self.router)