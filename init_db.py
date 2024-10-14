import os
from Models.Users import Users
from Models.Pharmacy import Pharmacy
from Models.Worker import Worker
from Services.Database.dbsqlite import DBSqlite


sql_file = open("template_sqlite.sql", "r")
database_file = "database.db"


#delete database
if os.path.exists(database_file):
 os.remove(database_file)
db = DBSqlite(database_file)


commands = sql_file.read().split(";")
for command in commands:
 db.executeRAW(command)


# db.executeRAW(Users.makeTableSqlite())
# db.executeRAW(Pharmacy.makeTableSqlite())