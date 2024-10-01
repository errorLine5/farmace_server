import datetime
import re

import fastapi
from Controllers.Auth.TokenAuth import Token

def sanitize(value): #allow @ and . - ! _ and numbers and letters
 sanitized = re.sub('[^A-Za-z0-9.@_-]', '', value)
 return sanitized


class Login_ctl:
 def __init__(self, dbService):
  self.dbService = dbService
  self.token = Token()


 def login( self, email, password):
  email = sanitize(email)
  password = sanitize(password)
  print (email, password)
  print (f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
  result = self.dbService.select(f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
  if len(result) == 0:
   raise fastapi.HTTPException(status_code=404, detail="User not found")
  token = self.token.generateToken()
  now = str(datetime.datetime.now()+datetime.timedelta(days=10))
 
  #update token
  self.dbService.execute(f"UPDATE users SET token = '{token}' , token_expiration = '{now}' WHERE email = '{email}'")

  
  return {"token": token, "token_expiration": now}