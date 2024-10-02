import sqlite3
from sqlite3 import Error
from fastapi import HTTPException

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
      
  def executeRAW(self, sql):
    try:
      cur = self.conn.cursor()
      cur.execute(sql)
      self.conn.commit()
      
    except Error as e:
      print(e)
      exit()
      
  def execute(self,query, params):
    try:
      self.conn.execute(query, params)
    except Error as e:
      raise HTTPException(status_code=404, detail=str(e))
    self.conn.commit()

  def select(self, query, params):
    try:
      cur = self.conn.cursor()
      cur.execute(query, params)
      return cur.fetchall()
    except Error as e:
      raise HTTPException(status_code=404, detail=str(e))
      exit()