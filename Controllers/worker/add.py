import fastapi
from Services.Auth import Auth
from Services.Sanification import sanitize
from Services.FieldValidation import FieldValidation
from Models.Worker import Worker
from tools.Query import BuildQuery
from uuid import uuid4



class add_worker_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)


    def add_worker(self, id, id_pharmacy, id_user, permission, email, token):
        id = sanitize(id)
        id_pharmacy = sanitize(id_pharmacy)
        id_user = sanitize(id_user)
        permission = sanitize(permission)

        self.auth.isAuth(email=email, token=token)
        if id is None:
            id=str(uuid4())

        #if self.auth.get_permission_level(worker_id)>0:

        

        queryPharmacy=f'SELECT id FROM Pharmacy WHERE id =? '

        resultPharmacy = self.dbService.select(queryPharmacy, (id_pharmacy,))

        if not resultPharmacy:
            raise fastapi.HTTPException(status_code=404, detail="Pharmacy not found")

        queryUser='''SELECT id FROM Users WHERE id =? '''

        result = self.dbService.select(queryUser, (id_user,))

        if not result:
            raise fastapi.HTTPException(status_code=404, detail="User not found")
        
        newWorker=Worker(
                id=id,
                id_pharmacy=id_pharmacy,
                id_user=id_user,
                permission=permission
        )

        query=BuildQuery(newWorker).insert_into().build()
        self.dbService.executeRAW(query)

        return {"status": "success", "id_worker": id}

        #else:
         #   raise fastapi.HTTPException(status_code=404, detail="permission denied")