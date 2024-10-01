import time
from typing import Union
from fastapi import FastAPI 
import Routes.auth.auth as auth
import Services.Database.dbsqlite as db







app = FastAPI()
app.db = db.DBSqlite("database.db")

auth.Auth(app)

