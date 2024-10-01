


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

  return True
