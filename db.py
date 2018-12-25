from pymongo import MongoClient
import os
import requests
import json
import genqrcode as QR

try:
    import configparser
except:
    from six.moves import configparser
config = configparser.ConfigParser()
config.read('config.txt')

class DB():
    mongoUrl = os.environ['mongoUrl']
    print(mongoUrl)
    name = os.environ['name']
    password = os.environ['password']
    dbName = os.environ['dbName']
    collName = os.environ['collName']
    print(collName)

    client = None
    db = None
    coll = None

    def connect(self):
        self.client = MongoClient(self.mongoUrl) # host uri 
        self.db = self.client[self.dbName] # Select the database
        self.db.authenticate(name=self.name,password=self.password)
        self.coll = self.db[self.collName]

    def close(self):
        self.client.close()

class Member():
    name = None
    alias = None
    department = None
    email = None
    cuisine = None
    accompany = None

    def __init__(self, name, alias, department, email, cuisine, accompany):
        self.name = name
        self.alias = alias
        self.department = department
        self.email = email
        self.cuisine = cuisine
        self.accompany = accompany

class RegisterMail():
	mailServiceUrl = os.environ['mailServiceUrl']
	member = None
	msg = None

	def __init__(self, newMember):
		self.member = newMember

	def genMsg(self):
		return QR.genHtml(self.member.alias)

	def genReqBody(self):
		msg = self.genMsg()
		body = {
			"name": self.member.name,
			"alias": self.member.alias,
			"email": self.member.email,
			"message": msg
		}
		return json.dumps(body)

	def send(self):
		header = {'content-type': 'application/json'}
		jsonBody = self.genReqBody()
		requests.post(self.AzureMailService, headers = header, data = jsonBody)

class RegisterDB(DB):

	def __init__(self):
		self.connect()

	def register(self, name, alias, department, email, cuisine, accompany):
		newMember = Member(name, alias, department, email, cuisine, accompany)
		self.coll.insert(newMember.__dict__)
		mail = RegisterMail(newMember)
		mail.send()
		print('register done')

	def remove(self, alias):
		self.coll.remove({"alias": alias})

	def list(self):
		memberList = self.coll.find()
		for m in memberList: print(m)

"""
# test case
member = Member('real-aaa', 'aaa', 'bbb@mail.com', 'apple', 'onefriend')
rdb = RegisterDB()
rdb.add(member)
rdb.list()
print('end')
"""
