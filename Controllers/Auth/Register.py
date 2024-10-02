import Models.Users as Users
import Services.Sanification as Sanification
from Services.FieldValidation import FieldValidation
from Controllers.Auth.TokenAuth import Token


class registerctl:
 
 def __init__(self, dbService):
  self.dbService = dbService
  self.token = Token()




 def register(self, email, password, first_name, last_name, phone_number, picture):
     # Sanitize input data
     email = Sanification.sanitize(email)
     password = Sanification.sanitize(password)
     first_name = Sanification.sanitize(first_name)
     last_name = Sanification.sanitize(last_name)
     phone_number = Sanification.sanitize(phone_number)
     picture = Sanification.sanitize(picture)

     # Validate input data
     FieldValidation(email).isEmail()
     FieldValidation(password).isPassword()

     # Prepare the SQL statement using parameterized queries
     query = """
         INSERT INTO users (email, password, first_name, last_name, phone_number, picture, token, token_expiration, verified, email_token) 
         VALUES (?, ?, ?, ?, ?, ?, NULL, NULL, FALSE, ?)
     """
     
     email_verification_token =  self.token.generateToken()
     
     # Execute the query with parameters
     self.dbService.execute(query, (email, password, first_name, last_name, phone_number, picture, email_verification_token))

     return {"status": "success"}
  
 def verifyEmail(self, email, email_token):
  email, email_token = Sanification.sanitize(email), Sanification.sanitize(email_token)
  query = "UPDATE users SET verified = TRUE, email_token = NULL WHERE email = ? AND email_token = ?"
  self.dbService.execute(query, (email, email_token))
  return {"status": "success"}
 
