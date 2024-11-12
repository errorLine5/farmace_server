from uuid import uuid4 as GUID
from typing import Optional
import pydantic


class Users(pydantic.BaseModel):
 id: str
 first_name: str
 last_name: str
 email: str
 username: str
 password: str
 phone_number: str
 picture: str
 token: Optional[str] = None
 token_expiration: Optional[str] = None
 verified: bool = False
 can_own: bool = False
 email_token: Optional[str] = None


class authParameters(pydantic.BaseModel):
 email: str
 password:str
 token : str


'''
create table Users(
    id TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    picture TEXT NOT NULL,
    verified BOOLEAN NOT NULL DEFAULT FALSE,
    token TEXT ,
    token_expiration DATETIME ,
    can_own BOOLEAN DEFAULT FALSE,
    email_token TEXT 
);
'''

