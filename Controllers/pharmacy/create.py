import datetime
import json
import re
from Services.Sanification import sanitize
import fastapi
from Services.FieldValidation import FieldValidation
from Services.Auth import Auth


class create_pharmacy_ctl:
 def __init__(self, dbService):
  self.dbService = dbService
  self.auth = Auth(dbService)

 def create_farmacy(self, id, name, address, phone_number, latitude, longitude, nocturn, email , token):
     id = sanitize(id)
     name = sanitize(name)
     address = sanitize(address)
     nocturn = sanitize(nocturn)
     
     self.auth.isAuth(email=email, token=token)

     

     query = "INSERT INTO pharmacy (id, name, address, phone_number, latitude, longitude, nocturn) VALUES (?, ?, ?, ?, ?, ?, ?)"

     self.dbService.execute(query, (id, name, address, phone_number, latitude, longitude, nocturn))

     return {"status": "success", "id_pharmacy": id}