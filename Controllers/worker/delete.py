import fastapi
from Services.Auth import Auth
from Services.Sanification import sanitize
from Models.Worker import Worker
from tools.Query import BuildQuery

class delete_worker_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def delete_worker(self, id, worker_id, email, token):

        id=sanitize(id)

        self.auth.isAuth(email=email, token=token)
       # if self.auth.get_permission_level(worker_id)>0:
        query='SELECT id FROM Worker Where id=?'

        result=self.dbService.select(query, (id,))

        if not result:
                raise fastapi.HTTPException(status_code=404, detail="Worker not found")

        try:
                query='DELETE FROM Worker WHERE id=?'
                self.dbService.execute(query, (id,))

        except Exception as e:
                raise fastapi.HTTPException(status_code=404, detail=f"Error deleting worker: " + str(e))

        return {"status": "success","deleted_worker_id": id}

        #else:
         #   raise fastapi.HTTPException(status_code=404, detail="permission denied")