from Services.Auth import Auth
from Services.Sanification import sanitize
from Services.FieldValidation import FieldValidation
from tools.Query import BuildQuery
from Models.Pharmacy import Pharmacy
from Services.Database.dbsqlite import DBSqlite
import fastapi

class edit_items_ctl:
    def __init__(self, dbService:DBSqlite):
        self.dbService = dbService
        self.auth = Auth(dbService)

    def edit_items(self, id, id_pharmacy, email, token):
        id = sanitize(id)
        id_pharmacy = sanitize(id_pharmacy)

        self.auth.isAuth(email=email, token=token)