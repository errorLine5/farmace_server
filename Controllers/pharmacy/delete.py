from Services.Auth import Auth


class delete_pharmacy_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def delete_pharmacy(self, id, token):
        self.auth.isAuth(token)
        query = "DELETE FROM pharmacy WHERE id = ?"
        self.dbService.delete(query, (id,))

        return {"status": "success"}