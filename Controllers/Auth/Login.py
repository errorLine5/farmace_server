import datetime
import json
import re

import fastapi
from Services.Sanification import sanitize
from Controllers.Auth.TokenAuth import Token
from tools.Query import BuildQuery
from Models.Users import Users



class Login_ctl:
 def __init__(self, dbService):
  self.dbService = dbService
  self.token = Token()


 def login( self, email, password):
  email, password = sanitize(email), sanitize(password)
  
  token = self.token.generateToken()
  now = str(datetime.datetime.now()+datetime.timedelta(days=10))
  
  query = BuildQuery(Users).select(['token', 'token_expiration']).where([f"email = '{email}' AND password = '{password}'"]).build()
  result = self.dbService.selectRAW(query)

  if len(result) == 0:
   raise fastapi.HTTPException(status_code=404, detail="User not found")
  
  
  
  query = "UPDATE users SET token = ?, token_expiration = ? WHERE email = ?" #update is not available in query builder
  self.dbService.execute(query, (token, now, email))
  return {"token": token, "token_expiration": now}
 
 def tokenCheck(self,email, token):
  email, token = sanitize(email), sanitize(token)
  #"SELECT * FROM users WHERE email = ? AND token = ?"
  query =  BuildQuery(Users).select(['token', 'token_expiration']).where([f"email = '{email}' AND token = '{token}'"]).build()
  print (query)
  result = self.dbService.selectRAW(query)
  

  print (result)
  token_expiration = result[0][1]
  now = str(datetime.datetime.now())
  if len(result) == 0:
   raise fastapi.HTTPException(status_code=404, detail="Token not valid")
  if token_expiration < now:
   raise fastapi.HTTPException(status_code=404, detail="Token expired")

  
  return {"token": token, "token_expiration": token_expiration}