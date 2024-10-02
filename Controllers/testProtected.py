from fastapi import FastAPI
from Services.Auth import Auth
from Services.Sanification import sanitize
from Services.FieldValidation import FieldValidation

class TestProtected:
 auth = None
 
 def __init__(self,  dbService): #create an instance of the controller with dbService
  self.dbService = dbService #create an instance of the service
  self.auth = Auth(dbService) #create an instance of the service
  

  
 def getUserInfo(self, email: str, token: str):
  email, token = sanitize(email), sanitize(token) #Sanification of inputs for security aka injections
  
  FieldValidation(email).isEmail()
  #check if token is valid and not expired, if not raise an error and skips the rest of the function below
  self.auth.isAuth(email, token).isEmailVerified(email, token)  # check if email is verified 
  
  
  #get user info from database WARNING THIS IS SQLITE QUERY
  query = "SELECT email, first_name, phone_number, verified, last_name FROM users WHERE email = ?"
  result = self.dbService.select(query, (email,))
  
  
  return result
  
  
  