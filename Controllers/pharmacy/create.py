import datetime
import json
import re
from uuid import uuid4
from Models.Pharmacy import Pharmacy
from Services.Sanification import sanitize
import fastapi
from Services.FieldValidation import FieldValidation
from Services.Auth import Auth
from tools.Query import BuildQuery


class create_pharmacy_ctl:
 def __init__(self, dbService):
  self.dbService = dbService
  self.auth = Auth(dbService)

 def create_farmacy(self, id, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web, email , worker_id, token):
     id = sanitize(id)
     if id is None:
         id = str(uuid4())
     nome_farmacia = sanitize(nome_farmacia)
     indirizzo = sanitize(indirizzo)
     orari = sanitize(orari)
     turni= sanitize(turni)
     sito_web = sanitize(sito_web)
     
     self.auth.isAuth(email=email, token=token)

     if self.auth.get_permission_level(worker_id)>1:

        newPharmacy = Pharmacy(
         id = id,
         nome_farmacia= nome_farmacia,
         indirizzo=  indirizzo,
         lat = lat,
         lng = lng,
         orari= orari,
         turni= turni,
         numeri = str(numeri),
         sito_web = sito_web
        )

        query = BuildQuery(newPharmacy).insert_into().build()
        self.dbService.executeRAW(query)

        return {"status": "success", "id_pharmacy": id}

     else:
         raise fastapi.HTTPException(status_code=403, detail="Permission denied")