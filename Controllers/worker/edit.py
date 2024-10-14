import fastapi
from Services.Auth import Auth
from Services.Sanification import sanitize
from tools.Query import BuildQuery
from Models.Worker import Worker


class edit_worker_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def edit_worker(self, id, worker:Worker,email, token):
        id = sanitize(id)

        self.auth.isAuth(email=email, token=token)

        query = 'SELECT * FROM Worker Where id=?'

        result = self.dbService.select(query, (id,))
        if not result:
            raise fastapi.HTTPException(status_code=404, detail="Worker not found")

        try:
            query = 'UPDATE Worker SET   id_pharmacy=?, permission=? WHERE id=?'

            self.dbService.execute(query, ( worker.id_pharmacy, worker.permission,id))

        except Exception as e:
            raise fastapi.HTTPException(status_code=404, detail=f"Error editing worker: " + str(e))

        return {"status": "success", "edited_worker_id": id}