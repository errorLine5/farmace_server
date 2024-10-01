import Models.Users as Users
import Services.Sanification as Sanification
from Services.FieldValidation import FieldValidation


class registerctl:
 
 def __init__(self, dbService):
  self.dbService = dbService



 def register( self, email, password, first_name, last_name, phone_number, picture):
  email = Sanification.sanitize(email)
  password = Sanification.sanitize(password)
  first_name = Sanification.sanitize(first_name)
  last_name = Sanification.sanitize(last_name)
  phone_number = Sanification.sanitize(phone_number)
  picture = Sanification.sanitize(picture)

  FieldValidation(email).isEmail()
  FieldValidation(password).isPassword()
  
  user = Users.Users(
   email = email,
   password = password,
   first_name = first_name,
   last_name = last_name,
   phone_number = phone_number,
   picture = picture
  )
  res = self.dbService.execute(f"INSERT INTO users VALUES ('{user.email}', '{user.password}', '{user.first_name}', '{user.last_name}', '{user.phone_number}', '{user.picture}' , NULL, NULL)")
  
  return {"status": "success"}
 
