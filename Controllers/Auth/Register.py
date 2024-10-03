from plistlib import UID
from uuid import uuid4
import Models.Users as Users
import Services.Sanification as Sanification
from Services.FieldValidation import FieldValidation
from tools.Query import BuildQuery
from Controllers.Auth.TokenAuth import Token


class registerctl:
 
 def __init__(self, dbService):
  self.dbService = dbService
  self.token = Token()




 def register(self, email, username, password, first_name, last_name, phone_number, picture):
     # Sanitize input data
     email = Sanification.sanitize(email)
     username = Sanification.sanitize(username)
     password = Sanification.sanitize(password)
     first_name = Sanification.sanitize(first_name)
     last_name = Sanification.sanitize(last_name)
     phone_number = Sanification.sanitize(phone_number)
     picture = Sanification.sanitize(picture)

     # Validate input data
     FieldValidation(email).isEmail()
     FieldValidation(password).isPassword()


     
     
     #generate uuid for user id
     new_user_id = str(uuid4())
     
     email_verification_token =  str(self.token.generateToken())
     
     user=Users.Users( 
      id = new_user_id,
      first_name = first_name,
      last_name = last_name,
      email = email,
      username = username,
      password = password,
      phone_number = phone_number,
      picture = picture,
      token = None,
      token_expiration = None,
      verified = False,
      can_own = False,
      email_token = email_verification_token
     )
     


     # Prepare the SQL statement using parameterized queries
    #  query = """
    #      INSERT INTO Users (id, password_user, email, username, first_name, last_name, phone_number, picture, verified, token, token_expiration, can_own, email_token) 
    #      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    #  """
     
     query = BuildQuery(user).insert_into().build()
     print (query)
     
     # Execute the query with parameters
     # self.dbService.execute(query, (user.id, user.password, user.email, user.username, user.first_name, user.last_name, user.phone_number, user.picture, user.verified, user.token, user.token_expiration, user.can_own, user.email_token))

     self.dbService.executeRAW(query)
    
     return {"status": "success"}
  
 def verifyEmail(self, email, email_token):
  email, email_token = Sanification.sanitize(email), Sanification.sanitize(email_token)
  query = "UPDATE users SET verified = TRUE, email_token = NULL WHERE email = ? AND email_token = ?"
  self.dbService.execute(query, (email, email_token))
  return {"status": "success"}
 
