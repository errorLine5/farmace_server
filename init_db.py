from Models.Users import Users
from Models.Pharmacy import Pharmacy
from Services.Database.dbsqlite import DBSqlite

db = DBSqlite("database.db")

db.executeRAW(Users.makeTableSqlite())
db.executeRAW(Pharmacy.makeTableSqlite())