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

 def create_farmacy(self, id, name, address, phone_number, latitude, longitude, nocturn, sito_web, email , token):
     id = sanitize(id)
     name = sanitize(name)
     address = sanitize(address)
     nocturn = sanitize(nocturn)
     sito_web = sanitize(sito_web)
     
     self.auth.isAuth(email=email, token=token)

     if id is None:
         id = str(uuid4())

     newPharmacy = Pharmacy(
         id = id,
         nome_farmacia= name,
         indirizzo=  address,
         numeri = str(phone_number),
         lat = latitude,
         lng = longitude,
         turni= nocturn,
         orari= '[]',
        
         sito_web = sito_web
     )

     query = BuildQuery(newPharmacy).insert_into().build()
     self.dbService.executeRAW(query)

     return {"status": "success", "id_pharmacy": id}