import datetime
import json
import re
from Services.Sanification import sanitize
import fastapi
from Controllers.Auth.TokenAuth import Token



class Login_ctl:
 def __init__(self, dbService):
  self.dbService = dbService
  self.token = Token()


 def login( self, email, password):
  email, password = sanitize(email), sanitize(password)
  print (email, password)
  print (f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
  result = self.dbService.select(f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
  if len(result) == 0:
   raise fastapi.HTTPException(status_code=404, detail="User not found")
  token = self.token.generateToken()
  now = str(datetime.datetime.now()+datetime.timedelta(days=10))
 
  #update token
  query = "UPDATE users SET token = ?, token_expiration = ? WHERE email = ?"
  self.dbService.execute(query, (token, now, email))
  return {"token": token, "token_expiration": now}
 
 def tokenCheck(self,email, token):
  email, token = sanitize(email), sanitize(token)
  result = self.dbService.select(f"SELECT * FROM users WHERE email = '{email}' AND token = '{token}'")
  print (result)
  token_expiration = result[0][7]
  now = str(datetime.datetime.now())
  if len(result) == 0:
   raise fastapi.HTTPException(status_code=404, detail="Token not valid")
  if token_expiration < now:
   raise fastapi.HTTPException(status_code=404, detail="Token expired")

  
  return {"token": token, "token_expiration": token_expiration}