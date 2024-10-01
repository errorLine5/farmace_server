import Models.Users as Users


class registerctl:
 
 def __init__(self, dbService):
  self.dbService = dbService



 def register( self, email, password, first_name, last_name, phone_number, picture):
  user = Users.Users(
   email = email,
   password = password,
   first_name = first_name,
   last_name = last_name,
   phone_number = phone_number,
   picture = picture
  )
  res = self.dbService.execute(f"INSERT INTO users VALUES ('{user.email}', '{user.password}', '{user.first_name}', '{user.last_name}', '{user.phone_number}', '{user.picture}' , NULL, NULL)")
  
  return 
 
