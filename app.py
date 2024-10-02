import time
from typing import Union
from fastapi import FastAPI
import Services.Database.dbsqlite as db
import importlib
import os

app = FastAPI()
app.db = db.DBSqlite("database.db")

__all__ = []
files = []

# Find all .py files recursively in the Routes folder
for (dirpath, dirnames, filenames) in os.walk("Routes"):
    for file in filenames:
        if file == "__init__.py" or file == "_init_.py":
            continue
        if file.endswith(".py"):
            print(file)

            # Combine the path components using os.path.join
            file_path = os.path.join(dirpath, file)

            # Convert the file path to a Python module import path format
            # Ensure Windows backslashes are converted to dots for module import
            file_module = os.path.normpath(file_path).replace(os.path.sep, ".")

            # Remove the ".py" extension from the module import path
            file_module = file_module[:-3]

            # Dynamically import the module
            module = importlib.import_module(file_module)
            
            # Call the Route method of the module
            module.Route(app)
