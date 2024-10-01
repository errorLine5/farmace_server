import json
import random
import unittest
import requests

baseURL = "http://127.0.0.1:8000"


#generate data for tests

def generate_data():
 random_int = random.randint(1000, 9999)
 data= {
  "email": "test"+str(random_int)+"@me.com",
  "password": "testpassword",
  "first_name": "test",
  "last_name": "test",
  "phone_number": "213" + str(random_int),
  "picture": "test"
  }
 return data
 
 
 

class TestRegister(unittest.TestCase):
 def test_test(self):
  self.url = baseURL+"/docs"
  self.response = requests.get(self.url)
  self.assertEqual(self.response.status_code, 200)
  
 def test_register(self):
  endpoint = "/auth/register"
  self.url = baseURL + endpoint
  print (self.url)
  self.params = generate_data()
 
  
  self.response = requests.post(self.url, params=self.params)
  self.assertEqual(self.response.status_code, 200)
  
 
 def test_registerlogin(self):
  endpointreg = "/auth/register"
  endpointlog = "/auth/login"
  self.url = baseURL + endpointreg
  self.params = generate_data()
  self.response = requests.post(self.url, params=self.params)
  print (self.response)
  print (self.response.text)
  self.assertEqual(self.response.status_code, 200)
  self.url = baseURL + endpointlog
  print (self.url)
 
  newparams = { "email": self.params["email"], "password": self.params["password"]}
  self.response = requests.post(self.url, params=newparams)
  print (self.response)
  print (self.response.text)
  self.assertEqual(self.response.status_code, 200)
  
  
 def test_token(self):
   
   #register user
   endpointreg = "/auth/register"
   self.url = baseURL + endpointreg
   self.params = generate_data()
   self.response = requests.post(self.url, params=self.params)
   print (self.response)
   print (self.response.text)
   self.assertEqual(self.response.status_code, 200)
   
   #login user
   endpointlog = "/auth/login"
   self.url = baseURL + endpointlog
   print (self.url)
   newparams = { "email": self.params["email"], "password": self.params["password"]}
   self.response = requests.post(self.url, params=newparams)
   print (self.response)
   print (self.response.text)
   self.assertEqual(self.response.status_code, 200)
   
   token = json.loads(self.response.text)["token"]
   
   #test token
   endpointlog = "/auth/token_test"
   self.url = baseURL + endpointlog
   print (self.url)
   newparams = { "email": self.params["email"], "token": token}
   self.response = requests.post(self.url, params=newparams)
   print (self.response)
   print (self.response.text)
   self.assertEqual(self.response.status_code, 200)
   self.assertEqual(json.loads(self.response.text)["token"], token)

