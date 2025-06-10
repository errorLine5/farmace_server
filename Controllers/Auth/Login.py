import datetime
import json
import re

import fastapi
from Services.Auth import Auth
from Services.Sanification import sanitize
from Controllers.Auth.TokenAuth import Token
from tools.Query import BuildQuery
from Models.Users import Users
from prisma import Prisma



class Login_ctl:
 def __init__(self, dbService):
  self.dbService = dbService
  self.token = Token()
  self.auth = Auth(dbService)


 async def login(self, email, password):
  prisma = Prisma()
  await prisma.connect()
  print("login")
  email, password = sanitize(email), sanitize(password)

  user = await prisma.user.find_first(where={"email": email, "password": password})

  print("user:", user)
  print("user.id:", user.id)
  token = self.token.generateToken()
  now = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


  id_user = user.id
  session = await prisma.session.create(
    data={
     "id_user": id_user,
      "token": token,
      "token_expiration": now
    }
  )

  await prisma.disconnect()
  return {"token": session.token, "token_expiration": session.token_expiration, "email": user.email}
 
 async def tokenCheck(self,email, token):
  email, token = sanitize(email), sanitize(token)
  prisma = Prisma()
  await prisma.connect()

  print("tokenCheck")
  print("email:", email)
  print("token:", token)

  user = await prisma.user.find_first(where={"email": email})
  session = await prisma.session.find_first(where={"token": token, "id_user": user.id})

  if session is None:
   raise fastapi.HTTPException(status_code=404, detail="Token not valid")
  if session.token_expiration < datetime.datetime.now():
   raise fastapi.HTTPException(status_code=404, detail="Token expired")
  await prisma.disconnect()
  return {"token": token, "token_expiration": session.token_expiration}
  


 async def logout(self, email, token):
  prisma = Prisma()
  await prisma.connect()
  # require auth
  email, token = sanitize(email), sanitize(token)
  self.auth.isAuth(email=email, token=token)

  #query = "UPDATE users SET token = NULL, token_expiration = NULL WHERE email = ?"
  #self.dbService.execute(query, (email,))
  await prisma.user.update(where={"email": email}, data={"token": None, "token_expiration": None})
  await prisma.disconnect()
  return {"message": "Logout successful"}
 
 async def refreshToken(self, email, token):
  prisma = Prisma()
  await prisma.connect()
  email, token = sanitize(email), sanitize(token)
  self.auth.isAuth(email=email, token=token)
  
  now = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
  await prisma.user.update(
    where={"email": email},
    data={"token": token, "token_expiration": now}
  )
  await prisma.disconnect()
  return {"token": token, "token_expiration": now}
 
 async def getMe(self, email, token):
  prisma = Prisma()
  await prisma.connect()
  email, token = sanitize(email), sanitize(token)


  
  #self.auth.isAuth(email=email, token=token) #is borked
  print("auth:", email, token)
  
  user = await prisma.user.find_first(where={"email": email})

  await prisma.disconnect()
  
  if user is None:
    raise fastapi.HTTPException(status_code=404, detail="User not found")
    
  return user