from Models.Users import Users
from Services.Database.dbsqlite import DBSqlite

db = DBSqlite("database.db")
db.execute(Users.makeTableSqlite())