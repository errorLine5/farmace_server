


from typing import Optional
import pydantic




class Users(pydantic.BaseModel):
 first_name: str
 last_name: str
 email: str
 password: str
 phone_number: str
 picture: str
 token: Optional[str] = None
 token_expiration: Optional[str] = None
 verified: bool = False
 email_token: Optional[str] = None



 def makeTableSqlite ():
  return f"CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT, first_name TEXT, last_name TEXT, phone_number TEXT, picture TEXT, token TEXT, token_expiration TEXT, verified BOOLEAN, email_token TEXT)"
