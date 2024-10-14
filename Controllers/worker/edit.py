import fastapi
from Services.Auth import Auth
from Services.Sanification import sanitize
from tools.Query import BuildQuery
from Models.Worker import Worker


class edit_worker_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def edit_worker(self, id, id_pharmacy, id_user, permission, worker_id, email, token):
        id = sanitize(id)
        id_pharmacy = sanitize(id_pharmacy)
        id_user = sanitize(id_user)
        permission = sanitize(permission)

        self.auth.isAuth(email=email, token=token)

        if self.auth.get_permission_level(worker_id)>0:


            query = 'SELECT * FROM Worker Where id=?'

            result = self.dbService.select(query, (id,))
            if not result:
                raise fastapi.HTTPException(status_code=404, detail="Worker not found")

            editedWorker = Worker(
                id=id,
                id_pharmacy=id_pharmacy,
                id_user=id_user,
                permission=permission
            )
            try:
                query = 'UPDATE Worker SET   id_pharmacy=?, permission=? WHERE id=?'

                self.dbService.execute(query, ( editedWorker.id_pharmacy, editedWorker.permission,id))

            except Exception as e:
                raise fastapi.HTTPException(status_code=404, detail=f"Error editing worker: " + str(e))

            return {"status": "success", "edited_worker_id": id}

        else:
            raise fastapi.HTTPException(status_code=404, detail="permission denied")