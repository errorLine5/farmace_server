import sqlite3
from sqlite3 import Error

class DBSqlite:
  def __init__(self, dbname):
    self.dbname = dbname
    self.conn = None
    try:
      self.conn = sqlite3.connect(self.dbname)
    except Error as e:
      print(e)
      exit()

  def __del__(self):
    if self.conn:
      self.conn.close()
      
  def execute(self, sql):
    try:
      cur = self.conn.cursor()
      cur.execute(sql)
      self.conn.commit()
      
    except Error as e:
      print(e)
      exit()

  def select(self, sql):
    try:
      cur = self.conn.cursor()
      cur.execute(sql)
      return cur.fetchall()
    except Error as e:
      print(e)
      exit()