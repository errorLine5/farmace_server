import datetime
import json
import re
from uuid import uuid4
from Models.Pharmacy import Pharmacy
from Models.Worker import Worker
from Services.Sanification import sanitize
import fastapi
from Services.FieldValidation import FieldValidation
from Services.Auth import Auth
from tools.Query import BuildQuery


class create_pharmacy_ctl:
 def __init__(self, dbService):
  self.dbService = dbService
  self.auth = Auth(dbService)

 def create_farmacy(self, id, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web,  email ,  token):
     id = (id)
     if id is None:
         id = str(uuid4())
     nome_farmacia = sanitize(nome_farmacia)
     indirizzo = sanitize(indirizzo)
     turni= sanitize(turni)
     sito_web = sanitize(sito_web)
     
     print ({id, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web,  email ,  token}, end="\n\n" )
     print (email, token , end="\n\n" )
     self.auth.isAuth(email=email, token=token)

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
     
     id_query="SELECT id FROM Users WHERE email = ?"
     result= self.dbService.execute(id_query, (email,))
     id_user=result.fetchone()[0]
     
     newWorker=Worker(
        id=str(uuid4()),
        id_pharmacy=id,
        id_user=str(id_user),
        permission=2
      )

     query = BuildQuery(newWorker).insert_into().build()
     self.dbService.executeRAW(query)

     return {"status": "success", "id_pharmacy": id}