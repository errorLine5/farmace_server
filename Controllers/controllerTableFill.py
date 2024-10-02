import datetime
import json
import re
from Services.Sanification import sanitize
import fastapi
from Services.FieldValidation import FieldValidation



class Fill_ctl:
 def __init__(self, dbService):
  self.dbService = dbService

 def fill(self, id, name, address, phone_number, latitude, longitude, nocturn):
     id = sanitize(id)
     name = sanitize(name)
     address = sanitize(address)
     nocturn = sanitize(nocturn)

     

     query = "INSERT INTO pharmacy (id, name, address, phone_number, latitude, longitude, nocturn) VALUES (?, ?, ?, ?, ?, ?, ?)"

     self.dbService.execute(query, (id, name, address, phone_number, latitude, longitude, nocturn))

     return {"status": "success"}