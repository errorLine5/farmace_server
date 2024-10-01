


from fastapi import FastAPI
import fastapi



class Auth:
 
 def __init__(self, dbService):
  self.dbService = dbService
  
 def isAuth(self,email, token):
  result = self.dbService.select(f"SELECT * FROM users WHERE email = '{email}' AND token = '{token}'")
  if len(result) == 0:
   raise fastapi.HTTPException(status_code=404, detail="Token not valid")

  return True
