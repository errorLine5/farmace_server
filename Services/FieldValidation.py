import re
from fastapi import HTTPException
class FieldValidation:
 
 def __init__(self, value):
  self.value = value
  
 def isEmail(self):
  #email must be valid
  pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Email not valid")
  else:
   return True
 
 def isPassword(self):
  #password must be at least 8 characters and contains at least one uppercase letter, one lowercase letter, and one number
  pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Password Must be at least 8 characters and contains at least one uppercase letter, one lowercase letter, and one number")
  else:
   return True

 def isPhoneNumber(self): #MIGHT BE BROKEN
  #phone number must be valid
  pattern = r'^\+?\d{8,15}$'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Phone number not valid")
  else:
   return True
  
 def mustBeNumber(self):
  #must be a number
  pattern = r'^\d+$'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Must be a number")
  else:
   return True
  
 def mustBeLetter(self):
  #must be a letter
  pattern = r'^[a-zA-Z]+$'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Must be a letter")
  else:
   return True
  
 def mustBeAlphanumeric(self):
  #must be alphanumeric
  pattern = r'^[a-zA-Z0-9]+$'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Must be alphanumeric")
  else:
   return True
  
 def mustBeUppercase(self):
  #must be uppercase
  pattern = r'^[A-Z]+$'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Must be uppercase")
  else:
   return True
  
 def mustBeLowercase(self):
  #must be lowercase
  pattern = r'^[a-z]+$'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Must be lowercase")
  else:
   return True
  
 def mustContainSpecialCharacter(self):
  #must contain special character
  pattern = r'[^A-Za-z0-9]+'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Must contain special character")
  else:
   return True

 def mustBeValidDate(self):
  #must be valid date
  pattern = r'^\d{4}-\d{2}-\d{2}$'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Must be valid date")
  else:
   return True
 
 def isDate(self):
  #must be a date
  pattern = r'^\d{4}-\d{2}-\d{2}$'
  if re.match(pattern, self.value) is None:
   raise HTTPException(status_code=404, detail="Must be a date")
  else:
   return True
