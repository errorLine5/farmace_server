import Models.Users as Users
import Services.Sanification as Sanification
from Services.FieldValidation import FieldValidation


class registerctl:
 
 def __init__(self, dbService):
  self.dbService = dbService



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
         INSERT INTO users (email, password, first_name, last_name, phone_number, picture, token, token_expiration) 
         VALUES (?, ?, ?, ?, ?, ?, NULL, NULL)
     """
     
     # Execute the query with parameters
     self.dbService.execute(query, (email, password, first_name, last_name, phone_number, picture))

     return {"status": "success"}
  
