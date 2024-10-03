from Models.Users import Users
from Models.Pharmacy import Pharmacy
from Services.Database.dbsqlite import DBSqlite


#THIS WILL BE AN ACCIDENT WHILE PULLING IT IN MAIN
db = DBSqlite("database.db")

templateDBFile = open("template_sqlite.sql", "r")

#split by ;
instructions = templateDBFile.read().split(';')

for instruction in instructions:
 db.executeRAW(instruction)


# db.executeRAW(Users.makeTableSqlite())
# db.executeRAW(Pharmacy.makeTableSqlite())