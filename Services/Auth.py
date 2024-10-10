

from Models import Pharmacy, Users, Works
from tools.Query import BuildQuery
from fastapi import FastAPI
import fastapi



class Auth:
 
 def __init__(self, dbService):
  self.dbService = dbService
  
 def isAuth(self,email, token):
  
  # Prepare the SQL statement using parameterized queries
  query = "SELECT * FROM users WHERE email = ? AND token = ?"
  # Execute the query with parameters
  result = self.dbService.select(query, (email, token))
  # Check if the token is valid
  if len(result) == 0:
   raise fastapi.HTTPException(status_code=404, detail="Token not valid")

  return self
 
 def isAuthorizedToCreate (self, email, token): ##TO BE TESTED
  query = BuildQuery(Users).select(['can_own']).where([f"email = '{email}' AND token = '{token}'"]).build()
  result = self.dbService.selectRAW(query)
  
  print ( result)
  if len(result) == 0:
   raise fastapi.HTTPException(status_code=404, detail="Token not valid")
  if result[0][0] == 0:
   raise fastapi.HTTPException(status_code=404, detail="User not authorized")
  return self
  
 def isAuthorizedToUpdate (self, email, token, pharmacy_id):
  query = BuildQuery(Users).select(['id']).where([f"email = '{email}' AND token = '{token}'"]).build()
  res = self.dbService.selectRAW(query)
  uid = res[0][0]
  query = BuildQuery(Works).select(['permission']).where([f"pharmacy_id = '{pharmacy_id}' AND user_id = '{uid}'"]).build()
  res = self.dbService.selectRAW(query)
  if len(res) == 0:
   raise fastapi.HTTPException(status_code=404, detail="User not authorized")
  if res[0][0] < 2:
   raise fastapi.HTTPException(status_code=404, detail="is not allowed to update")
  
  return self
  
  
 
 def isEmailVerified(self, email, token):

  # Prepare the SQL statement using parameterized queries
  query = "SELECT * FROM users WHERE email = ? AND token = ? AND verified = TRUE"
  # Execute the query with parameters
  result = self.dbService.select(query, (email, token))
  # Check if the token is valid
  if len(result) == 0:
   raise fastapi.HTTPException(status_code=404, detail="email not verified")

  return self