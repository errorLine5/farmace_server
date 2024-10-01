import time
from typing import Union
from fastapi import FastAPI 

import Services.Database.dbsqlite as db







app = FastAPI()
app.db = db.DBSqlite("database.db")



import importlib
import os


__all__ = []
files = []

#find all .py files recursively in the Routes folder
for (dirpath, dirnames, filenames) in os.walk("Routes"):
 for file in filenames:
  if file == "__init__.py" or file == "_init_.py":
   continue
  if file.endswith(".py"):
   print (file)

   file = os.path.join(dirpath, file)
   file = file.replace("/", ".") 
   file = file.replace(".py", "")
   module = importlib.import_module(file)
   module.Route(app)
  

