import pydantic

from typing import Optional
import sqlite3

Sqlite = {
 
 "str" : "TEXT",
 "int" : "INTEGER",
 "float" : "FLOAT",
 "bool" : "BOOLEAN",
 
 "SELECT": "SELECT <columns>",
 "FROM": "FROM <table>",
 "WHERE": "WHERE <condition>",
 "ORDER BY": "ORDER BY <column>",
 "LIMIT": "LIMIT <limit>",
 
 "INSERT INTO": "INSERT INTO <table> (<columns>) VALUES (<values>)",
 "UPDATE": "UPDATE <table> SET <column> = <value>",
 "DELETE": "DELETE FROM <table>",
 
 "AND": "AND <condition>",
 "OR": "OR <condition>",
 
 "IN": "IN (<values>)",
 "NOT IN": "NOT IN (<values>)",
 
 "IS NULL": "IS NULL",
 "IS NOT NULL": "IS NOT NULL",
 
 "LIKE": "LIKE <value>",
 "NOT LIKE": "NOT LIKE <value>",
 
 "BETWEEN": "BETWEEN <value> AND <value>",
 "NOT BETWEEN": "NOT BETWEEN <value> AND <value>",
 
 "EXISTS": "EXISTS (<subquery>)",
 "NOT EXISTS": "NOT EXISTS (<subquery>)",
 
 "UNION": "UNION (<subquery>)",
 "EXCEPT": "EXCEPT (<subquery>)",
 "INTERSECT": "INTERSECT (<subquery>)",
 
 "AS": "AS <alias>",
 "COUNT": "COUNT(<column>)",
 "SUM": "SUM(<column>)",
 "AVG": "AVG(<column>)",
 "MIN": "MIN(<column>)",
 "MAX": "MAX(<column>)",
 
 "SET": "SET <column> = <value>",
 "DELETE FROM": "DELETE FROM <table>",
 "CREATE TABLE": "CREATE TABLE <table> (<columns>)",
 "DROP TABLE": "DROP TABLE <table>",
 
 "JOIN": "JOIN <table> ON <condition>",
 "LEFT JOIN": "LEFT JOIN <table> ON <condition>",
 "RIGHT JOIN": "RIGHT JOIN <table> ON <condition>",
 "FULL JOIN": "FULL JOIN <table> ON <condition>",

}


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




class BuildQuery:
 
 def __init__(self, Model: pydantic.BaseModel, structure = Sqlite):
  print ("init")
  self.model = Model
  self.structure = structure
  self.values = []
  self.out = ""
  
  
  #if model contains values 

  try:
   self.populate()
  except:
   print ("no values or not instance of BaseModel with values")
   pass
 
  print ("init -- end")

 def populate(self):
     print ("oor: ")
     if self.values == []:
      values = []
      for field in self.model.model_fields:
       values.append(self.model.__getattribute__(field))
      self.values = values


 def select (self, columns = ["*"], tables = [], ):
  if len(tables) == 0:
   tables = [self.model.__name__]
  query= self.structure["SELECT"].replace("<columns>", ", ".join(columns))
  query= f"{query} {self.structure['FROM']}".replace("<table>", ", ".join(tables))
  self.out = query
  return self
 
 def where (self, conditions = []):
  query = self.out
  if len(conditions) == 0:
   conditions = ["TRUE"]
  query = f"{query} {self.structure['WHERE']} ".replace("<condition>", " AND ".join(conditions))
  self.out = query
  return self
 
 def order_by (self, columns = []):
  query = self.out
  if len(columns) == 0:
   raise Exception("No columns to order by")
  query = f"{query} {self.structure['ORDER BY']} ".replace("<column>", ", ".join(columns))
  self.out = query
  return self
 
 def limit (self, limit = 0):
  query = self.out
  query = f"{query} {self.structure['LIMIT']} ".replace("<limit>", str(limit))
  self.out = query
  return self
 

 


 def insert_into (self, columns = [], values = []):
  table = self.model.model_json_schema()["title"]
  print ("table name: ", table)
  query = self.out
  if len(columns) == 0:
   columns = self.model.model_fields.keys()
   print (columns)
  if len(values) == 0:
   values = self.values

  if len(columns) != len(values):
   print (len(columns), len(values))
   raise Exception("Columns and values must have the same length")
  #fix values format 
  for i in range(len(values)):
   values[i] = f"'{values[i]}'"

  #end fix
  query = f"{query} {self.structure['INSERT INTO']} ".replace("<table>", table)
  query =query.replace("<columns>", ", ".join(columns))
  query=query.replace("<values>", ", ".join(values))
  self.out = query
  return self

 def addValues (self, model: pydantic.BaseModel):
  values = []
  for field in model.model_fields:
   values.append(model.__getattribute__(field))
  self.values = values
  print ("\n",self.values, "\n")
 
 def build (self):
  print (self.out)
  return self.out
 











if __name__ == "__main__":
 db = sqlite3.connect("database.db")
 
 user = Users(
  id = "1",
  first_name = "John",
  last_name = "Doe",
  email = "a@a.com",
  username = "johndoe",
  password = "1234",
  phone_number = "123456789",
  picture = "a.png",
  verified = True,
  can_own = False
 )
 
 
 # bq = BuildQuery(Users)
 # bq.addValues(user)
 # querytest = bq.insert_into().build()
 # print (querytest, "\n\n")
 # db.execute(querytest)
 # db.commit()
 try:
  bqu = BuildQuery(user)
  query = bqu.insert_into().build()
  print (query , "\n\n")
  db.execute(query)
  db.commit()
 except Exception as e:
  print (e)
 
 bqu2 = BuildQuery(Users)
 query2 = bqu2.select().build()
 print ("query:", query2, "\n\n")
 print (db.execute(query2).fetchall())
 db.commit()
 
 
 
